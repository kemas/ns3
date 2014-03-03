# -*- Mode: python; coding: utf-8 -*-
from __future__ import division
#from __future__ import with_statement

LAYOUT_ALGORITHM = 'neato' # ['neato'|'dot'|'twopi'|'circo'|'fdp'|'nop']
REPRESENT_CHANNELS_AS_NODES = 1
DEFAULT_NODE_SIZE = 3.0 # default node size in meters
DEFAULT_TRANSMISSIONS_MEMORY = 5 # default number of of past intervals whose transmissions are remembered
BITRATE_FONT_SIZE = 10

# internal constants, normally not meant to be changed
SAMPLE_PERIOD = 0.1
PRIORITY_UPDATE_MODEL = -100
PRIORITY_UPDATE_VIEW = 200

import platform
if platform.system() == "Windows":
    SHELL_FONT = "Lucida Console 9"
else:
    SHELL_FONT = "Luxi Mono 10"


import ns.core
import ns.network
import ns.visualizer
import ns.internet
import ns.mobility

import math
import os
import sys
import gobject
import time

try:
    import pygraphviz
    import gtk
    import pango
    import goocanvas
    import cairo
    import threading
    import hud
    #import time
    import cairo
    from higcontainer import HIGContainer
    gobject.threads_init()
    try:
        import svgitem
    except ImportError:
        svgitem = None
except ImportError, _import_error:
    import dummy_threading as threading
else:
    _import_error = None

try:
    import ipython_view
except ImportError:
    ipython_view = None

from base import InformationWindow, PyVizObject, Link, lookup_netdevice_traits, PIXELS_PER_METER
from base import transform_distance_simulation_to_canvas, transform_point_simulation_to_canvas
from base import transform_distance_canvas_to_simulation, transform_point_canvas_to_simulation
from base import load_plugins, register_plugin, plugins

# ipmort src/visualizer/visualizer/core
import core

PI_OVER_2 = math.pi/2
PI_TIMES_2 = math.pi*2

class SFVisualizer(core.Visualizer):
    INSTANCE = None

    def __init__(self):
        super(core.Visualizer, self).__init__():

        assert Visualizer.INSTANCE is None
        Visualizer.INSTANCE = self
        super(Visualizer, self).__init__()
        self.nodes =  {} # node index -> Node
        self.channels = {} # id(ns3.Channel) -> Channel
        self.window = None # toplevel window
        self.canvas = None # goocanvas.Canvas
        self.time_label = None # gtk.Label
        self.play_button = None # gtk.ToggleButton
        self.zoom = None # gtk.Adjustment
        self._scrolled_window = None # gtk.ScrolledWindow

        self.links_group = goocanvas.Group()
        self.channels_group = goocanvas.Group()
        self.nodes_group = goocanvas.Group()

        self._update_timeout_id = None
        self.simulation = SimulationThread(self)
        self.selected_node = None # node currently selected
        self.speed = 1.0
        self.information_windows = []
        self._transmission_arrows = []
        self._last_transmissions = []
        self._drop_arrows = []
        self._last_drops = []
        self._show_transmissions_mode = None
        self.set_show_transmissions_mode(ShowTransmissionsMode.ALL)
        self._panning_state = None
        self.node_size_adjustment = None
        self.transmissions_smoothing_adjustment = None
        self.sample_period = SAMPLE_PERIOD
        self.node_drag_state = None
        self.follow_node = None
        self.shell_window = None

        self.create_gui()

        for plugin in plugins:
            plugin(self)

    def set_show_transmissions_mode(self, mode):
        assert isinstance(mode, ShowTransmissionsMode)
        self._show_transmissions_mode = mode
        if self._show_transmissions_mode == ShowTransmissionsMode.ALL:
            self.simulation.set_nodes_of_interest(range(ns.network.NodeList.GetNNodes()))
        elif self._show_transmissions_mode == ShowTransmissionsMode.NONE:
            self.simulation.set_nodes_of_interest([])
        elif self._show_transmissions_mode == ShowTransmissionsMode.SELECTED:
            if self.selected_node is None:
                self.simulation.set_nodes_of_interest([])
            else:
                self.simulation.set_nodes_of_interest([self.selected_node.node_index])

    def _create_advanced_controls(self):
        expander = gtk.Expander("Advanced")
        expander.show()

        main_vbox = gobject.new(gtk.VBox, border_width=8, visible=True)
        expander.add(main_vbox)

        main_hbox1 = gobject.new(gtk.HBox, border_width=8, visible=True)
        main_vbox.pack_start(main_hbox1)

        show_transmissions_group = HIGContainer("Show transmissions")
        show_transmissions_group.show()
        main_hbox1.pack_start(show_transmissions_group, False, False, 8)

        vbox = gtk.VBox(True, 4)
        vbox.show()
        show_transmissions_group.add(vbox)

        all_nodes = gtk.RadioButton(None)
        all_nodes.set_label("All nodes")
        all_nodes.set_active(True)
        all_nodes.show()
        vbox.add(all_nodes)

        selected_node = gtk.RadioButton(all_nodes)
        selected_node.show()
        selected_node.set_label("Selected node")
        selected_node.set_active(False)
        vbox.add(selected_node)
        
        no_node = gtk.RadioButton(all_nodes)
        no_node.show()
        no_node.set_label("Disabled")
        no_node.set_active(False)
        vbox.add(no_node)

        def toggled(radio):
            if radio.get_active():
                self.set_show_transmissions_mode(ShowTransmissionsMode.ALL)
        all_nodes.connect("toggled", toggled)

        def toggled(radio):
            if radio.get_active():
                self.set_show_transmissions_mode(ShowTransmissionsMode.NONE)
        no_node.connect("toggled", toggled)

        def toggled(radio):
            if radio.get_active():
                self.set_show_transmissions_mode(ShowTransmissionsMode.SELECTED)
        selected_node.connect("toggled", toggled)

        
        # -- misc settings
        misc_settings_group = HIGContainer("Misc Settings")
        misc_settings_group.show()
        main_hbox1.pack_start(misc_settings_group, False, False, 8)
        settings_hbox = gobject.new(gtk.HBox, border_width=8, visible=True)
        misc_settings_group.add(settings_hbox)

        # --> node size
        vbox = gobject.new(gtk.VBox, border_width=0, visible=True)
        scale = gobject.new(gtk.HScale, visible=True, digits=2)
        vbox.pack_start(scale, True, True, 0)
        vbox.pack_start(gobject.new(gtk.Label, label="Node Size", visible=True), True, True, 0)
        settings_hbox.pack_start(vbox, False, False, 6)
        self.node_size_adjustment = scale.get_adjustment()
        def node_size_changed(adj):
            for node in self.nodes.itervalues():
                node.set_size(adj.value)
        self.node_size_adjustment.connect("value-changed", node_size_changed)
        self.node_size_adjustment.set_all(DEFAULT_NODE_SIZE, 0.01, 20, 0.1)

        # --> transmissions smooth factor
        vbox = gobject.new(gtk.VBox, border_width=0, visible=True)
        scale = gobject.new(gtk.HScale, visible=True, digits=1)
        vbox.pack_start(scale, True, True, 0)
        vbox.pack_start(gobject.new(gtk.Label, label="Tx. Smooth Factor (s)", visible=True), True, True, 0)
        settings_hbox.pack_start(vbox, False, False, 6)
        self.transmissions_smoothing_adjustment = scale.get_adjustment()
        self.transmissions_smoothing_adjustment.set_all(DEFAULT_TRANSMISSIONS_MEMORY*0.1, 0.1, 10, 0.1)

        return expander

    class _PanningState(object):
        __slots__ = ['initial_mouse_pos', 'initial_canvas_pos', 'motion_signal']

    def _begin_panning(self, widget, event):
        self.canvas.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.FLEUR))
        self._panning_state = self._PanningState()
        x, y, dummy = widget.window.get_pointer()
        self._panning_state.initial_mouse_pos = (x, y)
        x = self._scrolled_window.get_hadjustment().value
        y = self._scrolled_window.get_vadjustment().value
        self._panning_state.initial_canvas_pos = (x, y)
        self._panning_state.motion_signal = self.canvas.connect("motion-notify-event", self._panning_motion)

    def _end_panning(self, event):
        if self._panning_state is None:
            return
        self.canvas.window.set_cursor(None)
        self.canvas.disconnect(self._panning_state.motion_signal)
        self._panning_state = None
        
    def _panning_motion(self, widget, event):
        assert self._panning_state is not None
        if event.is_hint:
            x, y, dummy = widget.window.get_pointer()
        else:
            x, y = event.x, event.y

        hadj = self._scrolled_window.get_hadjustment()
        vadj = self._scrolled_window.get_vadjustment()
        mx0, my0 = self._panning_state.initial_mouse_pos
        cx0, cy0 = self._panning_state.initial_canvas_pos
        
        dx = x - mx0
        dy = y - my0
        hadj.value = cx0 - dx
        vadj.value = cy0 - dy
        return True

    def _canvas_button_press(self, widget, event):
        if event.button == 2:
            self._begin_panning(widget, event)
            return True
        return False

    def _canvas_button_release(self, dummy_widget, event):
        if event.button == 2:
            self._end_panning(event)
            return True
        return False
    
    def _canvas_scroll_event(self, dummy_widget, event):
        if event.direction == gtk.gdk.SCROLL_UP:
            self.zoom.value *= 1.25
            return True
        elif event.direction == gtk.gdk.SCROLL_DOWN:
            self.zoom.value /= 1.25
            return True
        return False

    def get_hadjustment(self):
        return self._scrolled_window.get_hadjustment()
    def get_vadjustment(self):
        return self._scrolled_window.get_vadjustment()

    def create_gui(self):
        self.window = gtk.Window()
        vbox = gtk.VBox(); vbox.show()
        self.window.add(vbox)

        # canvas
        self.canvas = goocanvas.Canvas()
        self.canvas.connect_after("button-press-event", self._canvas_button_press)
        self.canvas.connect_after("button-release-event", self._canvas_button_release)
        self.canvas.connect("scroll-event", self._canvas_scroll_event)
        self.canvas.props.has_tooltip = True
        self.canvas.connect("query-tooltip", self._canvas_tooltip_cb)
        self.canvas.show()
        sw = gtk.ScrolledWindow(); sw.show()
        self._scrolled_window = sw
        sw.add(self.canvas)
        vbox.pack_start(sw, True, True, 4)
        self.canvas.set_size_request(600, 450)
        self.canvas.set_bounds(-10000, -10000, 10000, 10000)
        self.canvas.scroll_to(0, 0)


        self.canvas.get_root_item().add_child(self.links_group)
        self.links_group.set_property("visibility", goocanvas.ITEM_VISIBLE)
        
        self.canvas.get_root_item().add_child(self.channels_group)
        self.channels_group.set_property("visibility", goocanvas.ITEM_VISIBLE)
        self.channels_group.raise_(self.links_group)

        self.canvas.get_root_item().add_child(self.nodes_group)
        self.nodes_group.set_property("visibility", goocanvas.ITEM_VISIBLE)
        self.nodes_group.raise_(self.channels_group)

        self.hud = hud.Axes(self)

        hbox = gtk.HBox(); hbox.show()
        vbox.pack_start(hbox, False, False, 4)

        # zoom
        zoom_adj = gtk.Adjustment(1.0, 0.01, 10.0, 0.02, 1.0, 0)
        self.zoom = zoom_adj
        def _zoom_changed(adj):
            self.canvas.set_scale(adj.value)
        zoom_adj.connect("value-changed", _zoom_changed)
        zoom = gtk.SpinButton(zoom_adj)
        zoom.set_digits(3)
        zoom.show()
        hbox.pack_start(gobject.new(gtk.Label, label=" Zoom:", visible=True), False, False, 4)
        hbox.pack_start(zoom, False, False, 4)
        _zoom_changed(zoom_adj)

        # speed
        speed_adj = gtk.Adjustment(1.0, 0.01, 10.0, 0.02, 1.0, 0)
        def _speed_changed(adj):
            self.speed = adj.value
            self.sample_period = SAMPLE_PERIOD*adj.value
            self._start_update_timer()
        speed_adj.connect("value-changed", _speed_changed)
        speed = gtk.SpinButton(speed_adj)
        speed.set_digits(3)
        speed.show()
        hbox.pack_start(gobject.new(gtk.Label, label="  Speed:", visible=True), False, False, 4)
        hbox.pack_start(speed, False, False, 4)
        _speed_changed(speed_adj)

        # Current time
        self.time_label = gobject.new(gtk.Label, label="  Speed:", visible=True)
        self.time_label.set_width_chars(20)
        hbox.pack_start(self.time_label, False, False, 4)

        # Screenshot button
        screenshot_button = gobject.new(gtk.Button,
                                       label="Snapshot",
                                       relief=gtk.RELIEF_NONE, focus_on_click=False,
                                       visible=True)
        hbox.pack_start(screenshot_button, False, False, 4)

        def load_button_icon(button, icon_name):
            try:
                import gnomedesktop
            except ImportError:
                sys.stderr.write("Could not load icon %s due to missing gnomedesktop Python module\n" % icon_name)
            else:
                icon = gnomedesktop.find_icon(gtk.icon_theme_get_default(), icon_name, 16, 0)
                if icon is not None:
                    button.props.image = gobject.new(gtk.Image, file=icon, visible=True)

        load_button_icon(screenshot_button, "applets-screenshooter")
        screenshot_button.connect("clicked", self._take_screenshot)

        # Shell button
        if ipython_view is not None:
            shell_button = gobject.new(gtk.Button,
                                           label="Shell",
                                           relief=gtk.RELIEF_NONE, focus_on_click=False,
                                           visible=True)
            hbox.pack_start(shell_button, False, False, 4)
            load_button_icon(shell_button, "gnome-terminal")
            shell_button.connect("clicked", self._start_shell)

        # Play button
        self.play_button = gobject.new(gtk.ToggleButton,
                                       image=gobject.new(gtk.Image, stock=gtk.STOCK_MEDIA_PLAY, visible=True),
                                       label="Simulate (F3)",
                                       relief=gtk.RELIEF_NONE, focus_on_click=False,
                                       use_stock=True, visible=True)
        accel_group = gtk.AccelGroup()
        self.window.add_accel_group(accel_group)
        self.play_button.add_accelerator("clicked", accel_group,
                                         gtk.keysyms.F3, 0, gtk.ACCEL_VISIBLE)
        self.play_button.connect("toggled", self._on_play_button_toggled)
        hbox.pack_start(self.play_button, False, False, 4)

        self.canvas.get_root_item().connect("button-press-event", self.on_root_button_press_event)

        vbox.pack_start(self._create_advanced_controls(), False, False, 4)
        
        self.window.show()

    def scan_topology(self):
        print "scanning topology: %i nodes..." % (ns.network.NodeList.GetNNodes(),)
        graph = pygraphviz.AGraph()
        seen_nodes = 0
        for nodeI in range(ns.network.NodeList.GetNNodes()):
            seen_nodes += 1
            if seen_nodes == 100:
                print "scan topology... %i nodes visited (%.1f%%)" % (nodeI, 100*nodeI/ns.network.NodeList.GetNNodes())
                seen_nodes = 0
            node = ns.network.NodeList.GetNode(nodeI)
            node_name = "Node %i" % nodeI
            node_view = self.get_node(nodeI)

            mobility = node.GetObject(ns.mobility.MobilityModel.GetTypeId())
            if mobility is not None:
                node_view.set_color("red")
                pos = mobility.GetPosition()
                node_view.set_position(*transform_point_simulation_to_canvas(pos.x, pos.y))
                #print "node has mobility position -> ", "%f,%f" % (pos.x, pos.y)
            else:
                graph.add_node(node_name)

            for devI in range(node.GetNDevices()):
                device = node.GetDevice(devI)
                device_traits = lookup_netdevice_traits(type(device))
                if device_traits.is_wireless:
                    continue
                if device_traits.is_virtual:
                    continue
                channel = device.GetChannel()
                if channel.GetNDevices() > 2:
                    if REPRESENT_CHANNELS_AS_NODES:
                        # represent channels as white nodes
                        if mobility is None:
                            channel_name = "Channel %s" % id(channel)
                            graph.add_edge(node_name, channel_name)
                        self.get_channel(channel)
                        self.create_link(self.get_node(nodeI), self.get_channel(channel))
                    else:
                        # don't represent channels, just add links between nodes in the same channel
                        for otherDevI in range(channel.GetNDevices()):
                            otherDev = channel.GetDevice(otherDevI)
                            otherNode = otherDev.GetNode()
                            otherNodeView = self.get_node(otherNode.GetId())
                            if otherNode is not node:
                                if mobility is None and not otherNodeView.has_mobility:
                                    other_node_name = "Node %i" % otherNode.GetId()
                                    graph.add_edge(node_name, other_node_name)
                                self.create_link(self.get_node(nodeI), otherNodeView)
                else:
                    for otherDevI in range(channel.GetNDevices()):
                        otherDev = channel.GetDevice(otherDevI)
                        otherNode = otherDev.GetNode()
                        otherNodeView = self.get_node(otherNode.GetId())
                        if otherNode is not node:
                            if mobility is None and not otherNodeView.has_mobility:
                                other_node_name = "Node %i" % otherNode.GetId()
                                graph.add_edge(node_name, other_node_name)
                            self.create_link(self.get_node(nodeI), otherNodeView)

        print "scanning topology: calling graphviz layout"
        graph.layout(LAYOUT_ALGORITHM)
        for node in graph.iternodes():
            #print node, "=>", node.attr['pos']
            node_type, node_id = node.split(' ')
            pos_x, pos_y = [float(s) for s in node.attr['pos'].split(',')]
            if node_type == 'Node':
                obj = self.nodes[int(node_id)]
            elif node_type == 'Channel':
                obj = self.channels[int(node_id)]
            obj.set_position(pos_x, pos_y)

        print "scanning topology: all done."
        self.emit("topology-scanned")

    def get_node(self, index):
        try:
            return self.nodes[index]
        except KeyError:
            node = Node(self, index)
            self.nodes[index] = node
            self.nodes_group.add_child(node.canvas_item)
            node.canvas_item.connect("button-press-event", self.on_node_button_press_event, node)
            node.canvas_item.connect("button-release-event", self.on_node_button_release_event, node)
            return node

    def get_channel(self, ns3_channel):
        try:
            return self.channels[id(ns3_channel)]
        except KeyError:
            channel = Channel(ns3_channel)
            self.channels[id(ns3_channel)] = channel
            self.channels_group.add_child(channel.canvas_item)
            return channel

    def create_link(self, node, node_or_channel):
        link = WiredLink(node, node_or_channel)
        self.links_group.add_child(link.canvas_item)
        link.canvas_item.lower(None)

    def update_view(self):
        #print "update_view"

        self.time_label.set_text("Time: %f s" % ns.core.Simulator.Now().GetSeconds())
        
        self._update_node_positions()

        # Update information 
        for info_win in self.information_windows:
            info_win.update()

        self._update_transmissions_view()
        self._update_drops_view()

        self.emit("update-view")

    def _update_node_positions(self):
        for node in self.nodes.itervalues():
            if node.has_mobility:
                ns3_node = ns.network.NodeList.GetNode(node.node_index)
                mobility = ns3_node.GetObject(ns.mobility.MobilityModel.GetTypeId())
                if mobility is not None:
                    pos = mobility.GetPosition()
                    x, y = transform_point_simulation_to_canvas(pos.x, pos.y)
                    node.set_position(x, y)
                    if node is self.follow_node:
                        hadj = self._scrolled_window.get_hadjustment()
                        vadj = self._scrolled_window.get_vadjustment()
                        px, py = self.canvas.convert_to_pixels(x, y)
                        hadj.value = px - hadj.page_size/2
                        vadj.value = py - vadj.page_size/2

    def center_on_node(self, node):
        if isinstance(node, ns.network.Node):
            node = self.nodes[node.GetId()]
        elif isinstance(node, (int, long)):
            node = self.nodes[node]
        elif isinstance(node, Node):
            pass
        else:
            raise TypeError("expected int, viz.Node or ns.network.Node, not %r" % node)
        
        x, y = node.get_position()
        hadj = self._scrolled_window.get_hadjustment()
        vadj = self._scrolled_window.get_vadjustment()
        px, py = self.canvas.convert_to_pixels(x, y)
        hadj.value = px - hadj.page_size/2
        vadj.value = py - vadj.page_size/2
        

    def update_model(self):
        self.simulation.lock.acquire()
        try:
            self.emit("simulation-periodic-update")
        finally:
            self.simulation.lock.release()

    def do_simulation_periodic_update(self):
        smooth_factor = int(self.transmissions_smoothing_adjustment.value*10)

        transmissions = self.simulation.sim_helper.GetTransmissionSamples()
        self._last_transmissions.append(transmissions)
        while len(self._last_transmissions) > smooth_factor:
            self._last_transmissions.pop(0)            

        drops = self.simulation.sim_helper.GetPacketDropSamples()
        self._last_drops.append(drops)
        while len(self._last_drops) > smooth_factor:
            self._last_drops.pop(0)

    def _get_label_over_line_position(self, pos1_x, pos1_y, pos2_x, pos2_y):
        hadj = self._scrolled_window.get_hadjustment()
        vadj = self._scrolled_window.get_vadjustment()
        bounds_x1, bounds_y1 = self.canvas.convert_from_pixels(hadj.value, vadj.value)
        bounds_x2, bounds_y2 = self.canvas.convert_from_pixels(hadj.value + hadj.page_size,
                                                               vadj.value + vadj.page_size)
        pos1_x, pos1_y, pos2_x, pos2_y = ns.visualizer.PyViz.LineClipping(bounds_x1, bounds_y1,
                                                                bounds_x2, bounds_y2,
                                                                pos1_x, pos1_y,
                                                                pos2_x, pos2_y)
        return (pos1_x + pos2_x)/2, (pos1_y + pos2_y)/2

    def _update_transmissions_view(self):
        transmissions_average = {}
        for transmission_set in self._last_transmissions:
            for transmission in transmission_set:
                key = (transmission.transmitter.GetId(), transmission.receiver.GetId())
                rx_bytes, count = transmissions_average.get(key, (0, 0))
                rx_bytes += transmission.bytes
                count += 1
                transmissions_average[key] = rx_bytes, count

        old_arrows = self._transmission_arrows
        for arrow, label in old_arrows:
            arrow.set_property("visibility", goocanvas.ITEM_HIDDEN)
            label.set_property("visibility", goocanvas.ITEM_HIDDEN)
        new_arrows = []

        k = self.node_size_adjustment.value/5

        for (transmitter_id, receiver_id), (rx_bytes, rx_count) in transmissions_average.iteritems():
            transmitter = self.get_node(transmitter_id)
            receiver = self.get_node(receiver_id)
            try:
                arrow, label = old_arrows.pop()
            except IndexError:
                arrow = goocanvas.Polyline(line_width=2.0, stroke_color_rgba=0x00C000C0, close_path=False, end_arrow=True)
                arrow.set_property("parent", self.canvas.get_root_item())
                arrow.props.pointer_events = 0
                arrow.raise_(None)
                
                label = goocanvas.Text(parent=self.canvas.get_root_item(), pointer_events=0)
                label.raise_(None)

            arrow.set_property("visibility", goocanvas.ITEM_VISIBLE)
            line_width = max(0.1, math.log(float(rx_bytes)/rx_count/self.sample_period)*k)
            arrow.set_property("line-width", line_width)

            pos1_x, pos1_y = transmitter.get_position()
            pos2_x, pos2_y = receiver.get_position()
            points = goocanvas.Points([(pos1_x, pos1_y), (pos2_x, pos2_y)])
            arrow.set_property("points", points)

            kbps = float(rx_bytes*8)/1e3/rx_count/self.sample_period
            label.set_properties(visibility=goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                                 visibility_threshold=0.5,
                                 font=("Sans Serif %f" % int(1+BITRATE_FONT_SIZE*k)))
            angle = math.atan2((pos2_y - pos1_y), (pos2_x - pos1_x))
            if -PI_OVER_2 <= angle <= PI_OVER_2:
                label.set_properties(text=("%.2f kbit/s →" % (kbps,)),
                                     alignment=pango.ALIGN_CENTER,
                                     anchor=gtk.ANCHOR_S,
                                     x=0, y=-line_width/2)
                M = cairo.Matrix()
                M.translate(*self._get_label_over_line_position(pos1_x, pos1_y, pos2_x, pos2_y))
                M.rotate(angle)
                label.set_transform(M)
            else:
                label.set_properties(text=("← %.2f kbit/s" % (kbps,)),
                                     alignment=pango.ALIGN_CENTER,
                                     anchor=gtk.ANCHOR_N,
                                     x=0, y=line_width/2)
                M = cairo.Matrix()
                M.translate(*self._get_label_over_line_position(pos1_x, pos1_y, pos2_x, pos2_y))
                M.rotate(angle)
                M.scale(-1, -1)
                label.set_transform(M)

            new_arrows.append((arrow, label))
            
        self._transmission_arrows = new_arrows + old_arrows


    def _update_drops_view(self):
        drops_average = {}
        for drop_set in self._last_drops:
            for drop in drop_set:
                key = drop.transmitter.GetId()
                drop_bytes, count = drops_average.get(key, (0, 0))
                drop_bytes += drop.bytes
                count += 1
                drops_average[key] = drop_bytes, count

        old_arrows = self._drop_arrows
        for arrow, label in old_arrows:
            arrow.set_property("visibility", goocanvas.ITEM_HIDDEN)
            label.set_property("visibility", goocanvas.ITEM_HIDDEN)
        new_arrows = []

        # get the coordinates for the edge of screen
        vadjustment = self._scrolled_window.get_vadjustment()
        bottom_y = vadjustment.value + vadjustment.page_size
        dummy, edge_y = self.canvas.convert_from_pixels(0, bottom_y)

        k = self.node_size_adjustment.value/5

        for transmitter_id, (drop_bytes, drop_count) in drops_average.iteritems():
            transmitter = self.get_node(transmitter_id)
            try:
                arrow, label = old_arrows.pop()
            except IndexError:
                arrow = goocanvas.Polyline(line_width=2.0, stroke_color_rgba=0xC00000C0, close_path=False, end_arrow=True)
                arrow.props.pointer_events = 0
                arrow.set_property("parent", self.canvas.get_root_item())
                arrow.raise_(None)
                
                label = goocanvas.Text()#, fill_color_rgba=0x00C000C0)
                label.props.pointer_events = 0
                label.set_property("parent", self.canvas.get_root_item())
                label.raise_(None)

            arrow.set_property("visibility", goocanvas.ITEM_VISIBLE)
            arrow.set_property("line-width", max(0.1, math.log(float(drop_bytes)/drop_count/self.sample_period)*k))
            pos1_x, pos1_y = transmitter.get_position()
            pos2_x, pos2_y = pos1_x, edge_y
            points = goocanvas.Points([(pos1_x, pos1_y), (pos2_x, pos2_y)])
            arrow.set_property("points", points)

            label.set_properties(visibility=goocanvas.ITEM_VISIBLE_ABOVE_THRESHOLD,
                                 visibility_threshold=0.5,
                                 font=("Sans Serif %i" % int(1+BITRATE_FONT_SIZE*k)),
                                 text=("%.2f kbit/s" % (float(drop_bytes*8)/1e3/drop_count/self.sample_period,)),
                                 alignment=pango.ALIGN_CENTER,
                                 x=(pos1_x + pos2_x)/2,
                                 y=(pos1_y + pos2_y)/2)

            new_arrows.append((arrow, label))
            
        self._drop_arrows = new_arrows + old_arrows
            
                
    def update_view_timeout(self):
        #print "view: update_view_timeout called at real time ", time.time()

        # while the simulator is busy, run the gtk event loop
        while not self.simulation.lock.acquire(False):
            while gtk.events_pending():
                gtk.main_iteration()
        pause_messages = self.simulation.pause_messages
        self.simulation.pause_messages = []
        try:
            self.update_view()
            self.simulation.target_time = ns.core.Simulator.Now ().GetSeconds () + self.sample_period
            #print "view: target time set to %f" % self.simulation.target_time
        finally:
            self.simulation.lock.release()

        if pause_messages:
            #print pause_messages
            dialog = gtk.MessageDialog(parent=self.window, flags=0, type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK,
                                       message_format='\n'.join(pause_messages))
            dialog.connect("response", lambda d, r: d.destroy())
            dialog.show()
            self.play_button.set_active(False)

        # if we're paused, stop the update timer
        if not self.play_button.get_active():
            self._update_timeout_id = None
            return False

        #print "view: self.simulation.go.set()"
        self.simulation.go.set()
        #print "view: done."
        return True

    def _start_update_timer(self):
        if self._update_timeout_id is not None:
            gobject.source_remove(self._update_timeout_id)
        #print "start_update_timer"
        self._update_timeout_id = gobject.timeout_add(int(SAMPLE_PERIOD/min(self.speed, 1)*1e3),
                                                      self.update_view_timeout,
                                                      priority=PRIORITY_UPDATE_VIEW)

    def _on_play_button_toggled(self, button):
        if button.get_active():
            self._start_update_timer()
        else:
            if self._update_timeout_id is not None:
                gobject.source_remove(self._update_timeout_id)

    def _quit(self, *dummy_args):
        if self._update_timeout_id is not None:
            gobject.source_remove(self._update_timeout_id)
            self._update_timeout_id = None
        self.simulation.quit = True
        self.simulation.go.set()
        self.simulation.join()
        gtk.main_quit()

    def _monkey_patch_ipython(self):
        # The user may want to access the NS 3 simulation state, but
        # NS 3 is not thread safe, so it could cause serious problems.
        # To work around this, monkey-patch IPython to automatically
        # acquire and release the simulation lock around each code
        # that is executed.

        original_runcode = __IPYTHON__.runcode
        def runcode(ip, *args):
            #print "lock"
            self.simulation.lock.acquire()
            try:
                return original_runcode(*args)
            finally:
                #print "unlock"
                self.simulation.lock.release()
        import types
        __IPYTHON__.runcode = types.MethodType(runcode, __IPYTHON__)                

    def autoscale_view(self):
        if not self.nodes:
            return
        self._update_node_positions()
        positions = [node.get_position() for node in self.nodes.itervalues()]
        min_x, min_y = min(x for (x,y) in positions), min(y for (x,y) in positions)
        max_x, max_y = max(x for (x,y) in positions), max(y for (x,y) in positions)
        min_x_px, min_y_px = self.canvas.convert_to_pixels(min_x, min_y)
        max_x_px, max_y_px = self.canvas.convert_to_pixels(max_x, max_y)
        dx = max_x - min_x
        dy = max_y - min_y
        dx_px = max_x_px - min_x_px
        dy_px = max_y_px - min_y_px
        hadj = self._scrolled_window.get_hadjustment()
        vadj = self._scrolled_window.get_vadjustment()
        new_dx, new_dy = 1.5*dx_px, 1.5*dy_px

        if new_dx == 0 or new_dy == 0:
            return

        self.zoom.value = min(hadj.page_size/new_dx, vadj.page_size/new_dy)

        x1, y1 = self.canvas.convert_from_pixels(hadj.value, vadj.value)
        x2, y2 = self.canvas.convert_from_pixels(hadj.value+hadj.page_size, vadj.value+vadj.page_size)
        width = x2 - x1
        height = y2 - y1
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        
        self.canvas.scroll_to(center_x - width/2, center_y - height/2)

        return False

    def start(self):
        self.scan_topology()
        self.window.connect("delete-event", self._quit)
        #self._start_update_timer()
        gobject.timeout_add(200, self.autoscale_view)
        self.simulation.start()

        try:
            __IPYTHON__
        except NameError:
            pass
        else:
            self._monkey_patch_ipython()

        gtk.main()


    def on_root_button_press_event(self, view, target, event):
        if event.button == 1:
            self.select_node(None)
            return True

    def on_node_button_press_event(self, view, target, event, node):
        if event.button == 1:
            self.select_node(node)
            return True
        elif event.button == 3:
            self.popup_node_menu(node, event)
            return True
        elif event.button == 2:
            self.begin_node_drag(node)
            return True
        return False

    def on_node_button_release_event(self, view, target, event, node):
        if event.button == 2:
            self.end_node_drag(node)
            return True
        return False

    class NodeDragState(object):
        def __init__(self, canvas_x0, canvas_y0, sim_x0, sim_y0):
            self.canvas_x0 = canvas_x0
            self.canvas_y0 = canvas_y0
            self.sim_x0 = sim_x0
            self.sim_y0 = sim_y0
            self.motion_signal = None

    def begin_node_drag(self, node):
        self.simulation.lock.acquire()
        try:
            ns3_node = ns.network.NodeList.GetNode(node.node_index)
            mob = ns3_node.GetObject(ns.mobility.MobilityModel.GetTypeId())
            if mob is None:
                return
            if self.node_drag_state is not None:
                return
            pos = mob.GetPosition()
        finally:
            self.simulation.lock.release()            
        x, y, dummy = self.canvas.window.get_pointer()
        x0, y0 = self.canvas.convert_from_pixels(x, y)
        self.node_drag_state = self.NodeDragState(x0, y0, pos.x, pos.y)
        self.node_drag_state.motion_signal = node.canvas_item.connect("motion-notify-event", self.node_drag_motion, node)

    def node_drag_motion(self, item, targe_item, event, node):
        self.simulation.lock.acquire()
        try:
            ns3_node = ns.network.NodeList.GetNode(node.node_index)
            mob = ns3_node.GetObject(ns.mobility.MobilityModel.GetTypeId())
            if mob is None:
                return False
            if self.node_drag_state is None:
                return False
            x, y, dummy = self.canvas.window.get_pointer()
            canvas_x, canvas_y = self.canvas.convert_from_pixels(x, y)
            dx = (canvas_x - self.node_drag_state.canvas_x0)
            dy = (canvas_y - self.node_drag_state.canvas_y0)
            pos = mob.GetPosition()
            pos.x = self.node_drag_state.sim_x0 + transform_distance_canvas_to_simulation(dx)
            pos.y = self.node_drag_state.sim_y0 + transform_distance_canvas_to_simulation(dy)
            #print "SetPosition(%G, %G)" % (pos.x, pos.y)
            mob.SetPosition(pos)
            node.set_position(*transform_point_simulation_to_canvas(pos.x, pos.y))
        finally:
            self.simulation.lock.release()            
        return True

    def end_node_drag(self, node):
        if self.node_drag_state is None:
            return
        node.canvas_item.disconnect(self.node_drag_state.motion_signal)
        self.node_drag_state = None

    def popup_node_menu(self, node, event):
        menu = gtk.Menu()
        self.emit("populate-node-menu", node, menu)
        menu.popup(None, None, None, event.button, event.time)

    def _update_ipython_selected_node(self):
        # If we are running under ipython -gthread, make this new
        # selected node available as a global 'selected_node'
        # variable.
        try:
            __IPYTHON__
        except NameError:
            pass
        else:
            if self.selected_node is None:
                ns3_node = None
            else:
                self.simulation.lock.acquire()
                try:
                    ns3_node = ns.network.NodeList.GetNode(self.selected_node.node_index)
                finally:
                    self.simulation.lock.release()
            __IPYTHON__.user_ns['selected_node'] = ns3_node


    def select_node(self, node):
        if isinstance(node, ns.network.Node):
            node = self.nodes[node.GetId()]
        elif isinstance(node, (int, long)):
            node = self.nodes[node]
        elif isinstance(node, Node):
            pass
        elif node is None:
            pass
        else:
            raise TypeError("expected None, int, viz.Node or ns.network.Node, not %r" % node)

        if node is self.selected_node:
            return

        if self.selected_node is not None:
            self.selected_node.selected = False
        self.selected_node = node
        if self.selected_node is not None:
            self.selected_node.selected = True

        if self._show_transmissions_mode == ShowTransmissionsMode.SELECTED:
            if self.selected_node is None:
                self.simulation.set_nodes_of_interest([])
            else:
                self.simulation.set_nodes_of_interest([self.selected_node.node_index])

        self._update_ipython_selected_node()


    def add_information_window(self, info_win):
        self.information_windows.append(info_win)
        self.simulation.lock.acquire()
        try:
            info_win.update()
        finally:
            self.simulation.lock.release()

    def remove_information_window(self, info_win):
        self.information_windows.remove(info_win)
        
    def _canvas_tooltip_cb(self, canvas, x, y, keyboard_mode, tooltip):
        #print "tooltip query: ", x, y
        hadj = self._scrolled_window.get_hadjustment()
        vadj = self._scrolled_window.get_vadjustment()
        x, y = self.canvas.convert_from_pixels(hadj.value + x, vadj.value + y)
        item = self.canvas.get_item_at(x, y, True)
        #print "items at (%f, %f): %r | keyboard_mode=%r" % (x, y, item, keyboard_mode)
        if not item:
            return False
        while item is not None:
            obj = item.get_data("pyviz-object")
            if obj is not None:
                obj.tooltip_query(tooltip)
                return True
            item = item.props.parent
        return False

    def _get_export_file_name(self):
        sel = gtk.FileChooserDialog("Save...", self.canvas.get_toplevel(),
                                    gtk.FILE_CHOOSER_ACTION_SAVE,
                                    (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                     gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        sel.set_default_response(gtk.RESPONSE_OK)
        sel.set_local_only(True)
        sel.set_do_overwrite_confirmation(True)
        sel.set_current_name("Unnamed.pdf")

        filter = gtk.FileFilter()
        filter.set_name("Embedded PostScript")
        filter.add_mime_type("image/x-eps")
        sel.add_filter(filter)

        filter = gtk.FileFilter()
        filter.set_name("Portable Document Graphics")
        filter.add_mime_type("application/pdf")
        sel.add_filter(filter)

        filter = gtk.FileFilter()
        filter.set_name("Scalable Vector Graphics")
        filter.add_mime_type("image/svg+xml")
        sel.add_filter(filter)

        resp = sel.run()
        if resp != gtk.RESPONSE_OK:
            sel.destroy()
            return None
        
        file_name = sel.get_filename()
        sel.destroy()
        return file_name

    def _take_screenshot(self, dummy_button):
        #print "Cheese!"
        file_name = self._get_export_file_name()
        if file_name is None:
            return

        # figure out the correct bounding box for what is visible on screen
        x1 = self._scrolled_window.get_hadjustment().value
        y1 = self._scrolled_window.get_vadjustment().value
        x2 = x1 + self._scrolled_window.get_hadjustment().page_size
        y2 = y1 + self._scrolled_window.get_vadjustment().page_size
        bounds = goocanvas.Bounds()
        bounds.x1, bounds.y1 = self.canvas.convert_from_pixels(x1, y1)
        bounds.x2, bounds.y2 = self.canvas.convert_from_pixels(x2, y2)
        dest_width = bounds.x2 - bounds.x1
        dest_height = bounds.y2 - bounds.y1
        #print bounds.x1, bounds.y1, " -> ", bounds.x2, bounds.y2

        dummy, extension = os.path.splitext(file_name)
        extension = extension.lower()
        if extension == '.eps':
            surface = cairo.PSSurface(file_name, dest_width, dest_height)
        elif extension == '.pdf':
            surface = cairo.PDFSurface(file_name, dest_width, dest_height)
        elif extension == '.svg':
            surface = cairo.SVGSurface(file_name, dest_width, dest_height)
        else:
            dialog = gtk.MessageDialog(parent  = self.canvas.get_toplevel(),
                		       flags   = gtk.DIALOG_DESTROY_WITH_PARENT,
                		       type    = gtk.MESSAGE_ERROR,
                		       buttons = gtk.BUTTONS_OK,
                		       message_format = "Unknown extension '%s' (valid extensions are '.eps', '.svg', and '.pdf')"
                                                          % (extension,))
            dialog.run()
            dialog.destroy()
            return

        # draw the canvas to a printing context
        cr = cairo.Context(surface)
        cr.translate(-bounds.x1, -bounds.y1)
        self.canvas.render(cr, bounds, self.zoom.value)
        cr.show_page()
        surface.finish()

    def set_follow_node(self, node):
        if isinstance(node, ns.network.Node):
            node = self.nodes[node.GetId()]
        self.follow_node = node

    def _start_shell(self, dummy_button):
        if self.shell_window is not None:
            self.shell_window.present()
            return
        
        self.shell_window = gtk.Window()
        self.shell_window.set_size_request(750,550)
        self.shell_window.set_resizable(True)
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
        ipython = ipython_view.IPythonView()
        ipython.modify_font(pango.FontDescription(SHELL_FONT))
        ipython.set_wrap_mode(gtk.WRAP_CHAR)
        ipython.show()
        scrolled_window.add(ipython)
        scrolled_window.show()
        self.shell_window.add(scrolled_window)
        self.shell_window.show()
        self.shell_window.connect('destroy', self._on_shell_window_destroy)

        self._update_ipython_selected_node()
        __IPYTHON__.user_ns['viz'] = self


    def _on_shell_window_destroy(self, window):
        self.shell_window = None


initialization_hooks = []

def add_initialization_hook(hook, *args):
    """
    Adds a callback to be called after
    the visualizer is initialized, like this::
       initialization_hook(visualizer, *args)
    """
    global initialization_hooks
    initialization_hooks.append((hook, args))


def set_bounds(x1, y1, x2, y2):
    assert x2>x1
    assert y2>y1
    def hook(viz):
        cx1, cy1 = transform_point_simulation_to_canvas(x1, y1)
        cx2, cy2 = transform_point_simulation_to_canvas(x2, y2)
        viz.canvas.set_bounds(cx1, cy1, cx2, cy2)
    add_initialization_hook(hook)


def start():
    assert Visualizer.INSTANCE is None
    if _import_error is not None:
        import sys
        print >> sys.stderr, "No visualization support (%s)." % (str(_import_error),)
        ns.core.Simulator.Run()
        return
    load_plugins()
    viz = Visualizer()
    for hook, args in initialization_hooks:
        gobject.idle_add(hook, viz, *args)
    ns.network.Packet.EnablePrinting()
    viz.start()

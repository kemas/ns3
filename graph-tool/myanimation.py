#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This simple example on how to do animations using graph-tool, where the layout
# changes dynamically. We start with some network, and randomly rewire its
# edges, and update the layout dynamically, where edges are rewired only if
# their euclidean distance is reduced. It is thus a very simplistic model for
# spatial segregation.

from graph_tool.all import *
from numpy.random import *
from numpy.linalg import norm
import sys, os, os.path

# We need some Gtk and gobject functions
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject

# initialize graph 
g = Graph()
g.add_vertex(10)

# Parameters for the layout update
step = 0.005       # move step
K = 0.5            # preferred edge length
#pos = radial_tree_layout(g, g.vertex(0))  # initial layout positions
pos = g.vertex_properties

# If True, the frames will be dumped to disk as images.
offscreen = sys.argv[1] == "offscreen" if len(sys.argv) > 1 else False
max_count = 5000
if offscreen and not os.path.exists("./frames"):
    os.mkdir("./frames")

# This creates a GTK+ window with the initial graph layout
if not offscreen:
    win = GraphWindow(g, pos, geometry=(500, 400))
else:
    win = Gtk.OffscreenWindow()
    win.set_default_size(500, 400)
    win.graph = GraphWidget(g, pos)
    win.add(win.graph)

# list of edges
#edges = list(g.edges())

count = 0

# This function will be called repeatedly by the GTK+ main loop, and we use it
# to update the vertex layout and perform the rewiring.
def update_state():
    global count

    # Perform one iteration of the layout step, starting from the previous positions
    radial_tree_layout(g, g.vertex(0))

    for i in range(1):
        # add one node to the graph in random position
        vnew = g.add_vertex()
        # connect the new node to an existing randomly chosen node
        idx = randint(g.num_vertices())
        vex = g.vertex(idx)
        g.add_edge(vnew, vex)

    # The movement of the vertices may cause them to leave the display area. The
    # following function rescales the layout to fit the window to avoid this.
#    print count
#    if count % 1000 == 0:
#        win.graph.fit_to_window(ink=True)
#    count += 1

    # The following will force the re-drawing of the graph, and issue a
    # re-drawing of the GTK window.
    win.graph.regenerate_surface(lazy=False)
    win.graph.queue_draw()

    # if doing an offscreen animation, dump frame to disk
    if offscreen:
        pixbuf = win.get_pixbuf()
        pixbuf.savev(r'./frames/dancing%06d.png' % count, 'png', [], [])
        if count > max_count:
            sys.exit(0)

    # We need to return True so that the main loop will call this function more
    # than once.
    return True

# Bind the function above as an 'idle' callback.
cid = GObject.idle_add(update_state)

# We will give the user the ability to stop the program by closing the window.
win.connect("delete_event", Gtk.main_quit)

# Actually show the window, and start the main loop.
win.show_all()
Gtk.main()

from graph_tool.all import *
from gi.repository import Gtk, GObject
import time
g = Graph(prune=True, directed=True)
vertextext = g.new_vertex_property("string")
vertexprop_dict = { "text" : vertextext }

v1 = g.add_vertex()
v2 = g.add_vertex()
g.add_edge(v1, v2)

vertextext[v1] = "Vertex 1"
vertextext[v2] = "Vertex 2"

def _add_vertex(graph):
    v = graph.add_vertex()
    #vertextext[v] = "New Vertex"

win = graph_tool.draw.GraphWindow(g, pos=sfdp_layout(g), geometry=(400, 300),
                      vprops=vertexprop_dict)

def update_state():
    global g
    win.graph.regenerate_surface(lazy=False)
    win.graph.queue_draw()

    # this will lead to a segmentation fault
    _add_vertex(g)
    time.sleep(1)
    print("next...")
    return True


cid = GObject.idle_add(update_state)
win.connect("delete_event", Gtk.main_quit)
win.show_all()
Gtk.main()

from graph_tool.all import *
from gi.repository import Gtk, GObject
import time
import random

g = Graph(prune=True, directed=True)
positions = g.new_vertex_property("vector<float>")
v1 = g.add_vertex()
positions[v1] = (0, 0)

def _add_vertex(graph):
    global positions, v1
    v = graph.add_vertex()
    print graph.num_vertices()
    random.seed(time.time())
    x = random.randint(0, 400)
    random.seed(time.time())
    y = random.randint(0, 300)
    # this wil cause NaN and non-invertible matrix errors
    #positions[v] = (0, 0)
    # this will cause vertices not to "distribute" pressing s
    positions[v] = (x, y)

    #graph.add_edge(v1, v)

for x in range(0, 10):
    _add_vertex(g)

win = graph_tool.draw.GraphWindow(g,
    pos=positions,
    geometry=(400, 300),
    vertex_pen_width=1,
    vertex_font_size=10,
    vertex_size=10,
    )

def update_state():
    global g
    for i in range(10):
        _add_vertex(g)
    win.graph.regenerate_surface(lazy=False)
    win.graph.queue_draw()
    time.sleep(0.01)
    return True

cid = GObject.idle_add(update_state)
win.connect("delete_event", Gtk.main_quit)
win.show_all()
Gtk.main()

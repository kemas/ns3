# exponential.py
# Generate an exponential network

import sys
from graph_tool.all import *
from gi.repository import Gtk, GObject
import time
import random

INIT = 10
WIDTH = 400
HEIGHT = 300
FREQ = 10
DELAY = 0.0

# initialize global parameters
g = None
pos = None
duration = 1000

def add_node(g, pos, x=None, y=None):
    v = g.add_vertex()

    if not x:
        x = random.randrange(WIDTH)

    if not y:
        y = random.randrange(HEIGHT)

    # set position
    pos[v] = (x, y)

    return v

def create_graph(init):
    # initialize a graph with init isolated vertices

    g = Graph()
    pos = g.new_vertex_property("vector<float>")

    for i in range(init):
        add_node(g, pos)

    return g, pos

def grow_random(g, pos):
    # add a vertex and connect randomly to an existing vertex
    
    # choose an existing vertex to be connected to
    vq = g.vertex(random.randrange(g.num_vertices()))
    # add a vertex
    vp = add_node(g, pos)
    # connect vp to vq
    return g.add_edge(vp, vq)

def create_window(g, pos, width, height):
    return graph_tool.draw.GraphWindow(g,
        pos=pos,
        geometry=(width, height),
        vertex_pen_width=1,
        vertex_font_size=10,
        vertex_size=10,
        )

def update_state():
    global duration

    if duration > 0:
        print "duration"
        for i in range(FREQ):
            print "grow"
            grow_random(g, pos)

        print "regenerate surface"
        win.graph.regenerate_surface(lazy=True, timeout=100)
        print "draw"
        win.graph.queue_draw()
        print "delay"
        time.sleep(DELAY)

        duration -= 1

    #if duration % 10 == 0:
    print duration

    return True

def main(argv):
    global g
    global pos
    global win

    g, pos = create_graph(INIT)
    win = create_window(g, pos, WIDTH, HEIGHT)
    cid = GObject.idle_add(update_state)
    win.connect("delete_event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    sys.exit(main(sys.argv))


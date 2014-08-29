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

# initialize global parameters
g = None
pos = None
duration = 100
freq = 1
tredraw = 0
delay = 0.0

# system argument handler functions

KEY_INIT = '-i'
KEY_WIDTH = '-w'
KEY_HEIGHT = '-h'
KEY_DURATION = '-t'
KEY_FREQ = '-f'
KEY_TREDRAW = '-r'
KEY_DELAY = '-l'

# dictionary contains option flags as keys and their corresonding default value
defopts = {KEY_INIT:INIT, KEY_WIDTH:WIDTH, KEY_HEIGHT:HEIGHT, KEY_DURATION:duration, KEY_FREQ:freq, KEY_TREDRAW:tredraw, KEY_DELAY:delay}

def add_to_dictarg(dictarg, key, arg):
    # add assertion here if necessary, e.g.:
    #if key == '-m':
    #    assert arg in ('wo', 'ko'), "Possible arguments for -m option are: "+", ".join(MARKERS)

    if dictarg.has_key(key):
        dictarg[key].append(arg)
    else:
        dictarg[key] = arg

def readargv(argv, defopts, pos=1, opt='', dictarg={}):
    if pos >= len(argv):
        return

    currarg = argv[pos]

    if pos == 1 or currarg[0] == '-':
        if currarg not in defopts.keys():
            printusage()
            return

        readargv(argv, defopts, pos + 1, currarg, dictarg)

    else:
        add_to_dictarg(dictarg, opt, currarg)
        readargv(argv, defopts, pos + 1, opt, dictarg)

    return dictarg

def getargval(dictarg, key, ifnone=None):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def printusage():
    pass
    #print "Usage: python plot.py -<function option> <file-1> [file-n] [-l label-1 label-n] [-m markset] [-s filename] [-x x-1 x-m -r r-1 r-p]"
    #print "Example: python plot.py -f data1.json data2.json -l \"data 1\" \"data 2\" -m var -s \"graph.png\""

# exponential network generator functions

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
    global freq
    global tredraw
    global delay

    if duration > 0:
        print "duration"
        for i in range(freq):
            print "grow"
            grow_random(g, pos)

        print "regenerate surface"
        win.graph.regenerate_surface(lazy=True, timeout=tredraw)
        print "draw"
        win.graph.queue_draw()
        print "delay"
        time.sleep(delay)

        duration -= 1
    else:
        return False

    #if duration % 10 == 0:
    print duration

    return True

def main(argv):
    global g
    global pos
    global win
    global duration
    global freq
    global tredraw
    global delay
#    global defopts

    # get values from arguments
    dictarg = readargv(argv, defopts) if len(argv) > 1 else {}
    if dictarg == None:
        return
    init = int(getargval(dictarg, KEY_INIT, defopts[KEY_INIT]))
    width = int(getargval(dictarg, KEY_WIDTH, defopts[KEY_WIDTH]))
    height = int(getargval(dictarg, KEY_HEIGHT, defopts[KEY_HEIGHT]))
    duration = int(getargval(dictarg, KEY_DURATION, defopts[KEY_DURATION]))
    freq = int(getargval(dictarg, KEY_FREQ, defopts[KEY_FREQ]))
    tredraw = int(getargval(dictarg, KEY_TREDRAW, defopts[KEY_TREDRAW]))
    delay = int(getargval(dictarg, KEY_DELAY, defopts[KEY_DELAY]))

    g, pos = create_graph(init)
    win = create_window(g, pos, width, height)
    cid = GObject.idle_add(update_state)
    win.connect("delete_event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    sys.exit(main(sys.argv))


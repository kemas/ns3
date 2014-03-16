# plot.py

import sys
import matplotlib.pyplot as plt
import json

markers = ['bo', 'rs', 'bv', 'rD', 'b+', 'rx', 'ro', 'bs', 'rv', 'bD', 'r+', 'bx']

def plotfailnodes(ds, labels, xybase=None
    , title='Random cascading failure in service network'
    , xylabels={'x':'Nodes removed', 'y':'Nodes fail'}):
    # plot fail nodes from data set
    # data set is a list of x and y data to plot

    itm = iter(markers)
    i = 0
    for xy in ds:
        try:
            mark = itm.next()
        except AttributeError:
            itm = iter(markers)
            mark = itm.next()

        if i < len(labels):
            plt.plot(xy[0], xy[1], mark, label=labels[i])
            i += 1
        else:
            plt.plot(xy[0], xy[1], mark, )

    if xybase:
        # xybase is defined
        # create baseline
        plt.plot(xybase[0], xybase[1], 'r-', label='x=y')

    plt.xlabel(xylabels['x'])
    plt.ylabel(xylabels['y'])
    plt.show()

def loaddata(ds, func, data, norm=False):
    x = []
    y = []
    label = ''

    if func == 'f':
        nodesremoved = data['nodesremoved']
        found = False; i = 0
        while not found and i < len(nodesremoved):
            if nodesremoved[i] > 0:
                found = True;
            else:
                i += 1

        if found:
            x = nodesremoved[i:]
            y = data['nodesfail'][i:]

    ds.append([x, y, label])

def main(argv):
    if len(sys.argv) < 3:
        print "Usage: python plot.py <function> <file-1> [file-n] [-l] [label-1 label-n]"
        print "Example: python plot.py f data1.json data2.json -l \"data 1\" \"data 2\""
        return

    func = sys.argv[1]
    ds = []
    i = 2; stop = False
    while not stop:
        filename = sys.argv[i]
        f = open(filename)
        try:
            data = json.load(f)
            loaddata(ds, func, data)
        finally:
            f.close()

        i += 1
        if i >= len(sys.argv) or sys.argv[i] == '-l':
            stop = True

    labels = []
    if i < len(sys.argv):
        labels = sys.argv[i:]

    if func == 'f':
        plotfailnodes(ds, labels)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

# plot.py

import sys
import matplotlib.pyplot as plt
import numpy as np
import json

GAMMA = u'\u03b3'
LOGBINBASE = 1.2
FUNC_FAIL = 'f'
FUNC_LOGINDEG = 'li'
FUNC_LOGOUTDEG = 'lo'
FUNC_HISTINDEG = 'hi'
FUNC_HISTOUTDEG = 'ho'

markers = ['bo-', 'rs-', 'bv-', 'rD-', 'b+-', 'rx-', 'ro-', 'bs-', 'rv-', 'bD-', 'r+-', 'bx-']

def drawhistogram(ds, xlabel, labels, nbins=50, normed=False, facecolor='green', alpha=0.5, histtype='bar', log=False):
    # the histogram of the degree distribution

    itm = iter(markers)
    i = 0
    for degrees, maxdegree in ds:
        plt.hist(degrees, bins=nbins, normed=normed, facecolor=facecolor, alpha=alpha, histtype=histtype, log=log)

    normedlabel = ''
    if normed:
        normedlabel = ' (normalized)'

    plt.title('Degree distribution')
    plt.xlabel(xlabel)
    plt.ylabel('Number of nodes'+ normedlabel)
    if len(labels) > 0:
        plt.legend()
    plt.show()

def logbins(amax, amin=0, base=LOGBINBASE):
    bins = [amin]
    num = amin + 1
    i = 1

    while num <= amax:
        bins.append(num)
        num += base**i
        i += 1

    bins.append(amax)
 
    return bins

def drawloglogdist(ds, xlabel, labels, density=False):
    # degree distribution in loglog scale

    itm = iter(markers)
    i = 0
    for degrees, maxdegree in ds:
        lbins = logbins(maxdegree, amin=0, base=LOGBINBASE)
        y, bins = np.histogram(degrees, bins=lbins, density=density)
        x = bins[:-1]

        xforlog = []; logx = []; logy = []
        for i in range(len(y)):
            if x[i] and y[i]:
                xforlog.append(x[i])
                logx.append(np.log10(x[i]))
                logy.append(np.log10(y[i]))

        try:
            mark = itm.next()
        except AttributeError:
            itm = iter(markers)
            mark = itm.next()

        gamma, logA = np.polyfit(logx, logy, 1)
        p = np.poly1d([gamma, logA])
        if i < len(labels):
            plt.plot(x, y, mark[:-1], label=labels[i])
            i += 1
        else:
            plt.plot(x, y, mark[:-1])
        plt.plot(xforlog, 10**p(logx), mark[0] + mark[2])

    plt.loglog()
    plt.title(u'Degree distribution (%s = %#.2f)' % (GAMMA, -1 * gamma))
    plt.xlabel(xlabel)
    plt.ylabel('Number of nodes')
    if len(labels) > 0:
        plt.legend()
    plt.show()

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

    plt.title(title)
    plt.xlabel(xylabels['x'])
    plt.ylabel(xylabels['y'])
    if len(labels) > 0:
        plt.legend()
    plt.show()

def loaddata(ds, func, data, step=50, norm=True):
    x = []
    y = []

    nbofnodes = 1
    if norm:
        # get the number of nodes
        nbofnodes = float(data['nodescreated'][-1])

    if func == FUNC_FAIL:
        nodesremoved = data['nodesremoved']
        found = False; i = 0
        while not found and i < len(nodesremoved):
            if nodesremoved[i] > 0:
                found = True;
            else:
                i += 1

        if found:
            x = [rmv / nbofnodes for rmv in nodesremoved[i::step]]
            y = [fail / nbofnodes for fail in data['nodesfail'][i::step]]

        ds.append([x, y])

    elif func in [FUNC_LOGINDEG, FUNC_HISTINDEG]:
        ds.append([data['indegree'], data['maxindegree']])

    elif func in [FUNC_LOGOUTDEG, FUNC_HISTOUTDEG]:
        ds.append([data['outdegree'], data['maxoutdegree']])

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
        labels = sys.argv[i+1:]

    if func in [FUNC_LOGINDEG, FUNC_HISTINDEG]:
        xlabel = 'Indegree'
    elif func in [FUNC_LOGOUTDEG, FUNC_HISTOUTDEG]:
        xlabel = 'Outdegree'

    if func == FUNC_FAIL:
        plotfailnodes(ds, labels)

    elif func in [FUNC_LOGINDEG, FUNC_LOGOUTDEG]:
        # loglog indegree distribution
        drawloglogdist(ds, xlabel, labels)

    elif func in [FUNC_HISTINDEG, FUNC_HISTOUTDEG]:
        # loglog outdegree distribution
        drawhistogram(ds, xlabel, labels)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

# plot.py

import sys
import matplotlib.pyplot as plt
import numpy as np
import json

GAMMA = u'\u03b3'
LOGBINBASE = 1.05
FUNC_FAIL = '-f'
FUNC_LOGINDEG = '-li'
FUNC_LOGOUTDEG = '-lo'
FUNC_HISTINDEG = '-hi'
FUNC_HISTOUTDEG = '-ho'
FUNCOPTS = (FUNC_FAIL, FUNC_LOGINDEG, FUNC_LOGOUTDEG, FUNC_HISTINDEG, FUNC_HISTOUTDEG)

MARKERS = {'var':['bo-', 'rs-', 'bv-', 'rD-', 'b+-', 'rx-', 'b*-', 'r*-', 'b|-', 'r|-', 'bp-', 'rp-', 'ro-', 'bs-', 'rv-', 'bD-', 'r+-', 'bx-', 'r*-', 'b*-', 'r|-', 'b|-', 'rp-', 'bp-']
        , 'sym':['bo-', 'ro-', 'bs-', 'rs-', 'bv-', 'rv-', 'bD-', 'rD-', 'b+-', 'r+-', 'bx-', 'rx-', 'b*-', 'r*-', 'b|-', 'r|-', 'bp-', 'rp-']}

def drawhistogram(ds, xlabel, labels, filename=None, nbins=50, normed=False, facecolor='green', alpha=0.5, histtype='bar', log=False):
    # the histogram of the degree distribution

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

    if filename:
        plt.savefig(filename)
    else:
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

def drawloglogdist(ds, xlabel, labels, markset='var', filename=None, density=False):
    # degree distribution in loglog scale
    
    lblgamma = u'%s = %%#.2f' % (GAMMA)
    itm = iter(MARKERS[markset])
    j = 0
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
            itm = iter(MARKERS[markset])
            mark = itm.next()

        gamma, logA = np.polyfit(logx, logy, 1)
        p = np.poly1d([gamma, logA])
        if j < len(labels):
            plt.plot(x, y, mark[:-1], label = '%s, %s' % (labels[j], lblgamma % (-1 * gamma)))
            j += 1
        else:
            plt.plot(x, y, mark[:-1], label = lblgamma % (-1 * gamma))
        plt.plot(xforlog, 10**p(logx), mark[0] + mark[2])

    plt.loglog()
    plt.title(u'Degree distribution')
    plt.xlabel(xlabel)
    plt.ylabel('Number of nodes')
    plt.legend()

    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def plotfailnodes(ds, labels, markset='var', filename=None
    , isBase=True
    , title='Random cascading failure in service network'
    , xylabels={'x':'Nodes removed', 'y':'Nodes fail'}):
    # plot fail nodes from data set
    # data set is a list of x and y data to plot

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.65, 0.8])

    itm = iter(MARKERS[markset])
    maxxy = 0
    i = 0
    for xy in ds:
        try:
            mark = itm.next()
        except AttributeError:
            itm = iter(MARKERS[markset])
            mark = itm.next()

        if i < len(labels):
            ax.plot(xy[0], xy[1], mark, label=labels[i])
            i += 1
        else:
            ax.plot(xy[0], xy[1], mark)

        currmaxxy = max(max(xy[0]), max(xy[1]))
        if maxxy < currmaxxy:
            maxxy = currmaxxy

    if isBase:
        # create baseline x=y
        ax.plot([0, maxxy], [0, maxxy], 'g-')

    ax.set_title(title)
    ax.set_xlabel(xylabels['x'])
    ax.set_ylabel(xylabels['y'])
    if len(labels) > 0:
        ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def loaddata(ds, func, data, step=300, norm=True):
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

def addtodictarg(dictarg, key, arg):
    # assert arguments for -m (markset)
    if key == '-m':
        assert arg in MARKERS, "Possible arguments for -m option are: "+", ".join(MARKERS)

    if dictarg.has_key(key):
        dictarg[key].append(arg)
    else:
        dictarg[key] = [arg]

def readargv(argv, pos=1, opt='', dictarg={}):
    if pos >= len(argv):
        return

    currarg = argv[pos]

    if pos == 1 or currarg[0] == '-':
        if currarg in FUNCOPTS:
            dictarg['func'] = currarg
            currarg = 'files'

        elif currarg not in ['-l', '-m', '-s']:
            printusage()
            return

        readargv(argv, pos + 1, currarg, dictarg)

    else:
        addtodictarg(dictarg, opt, currarg)
        readargv(argv, pos + 1, opt, dictarg)

    return dictarg

def getargval(dictarg, key, ifnone=[]):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def printusage():
    print "Usage: python plot.py -<function option> <file-1> [file-n] [-l label-1 label-n] [-m markset] [-s filename]"
    print "Example: python plot.py -f data1.json data2.json -l \"data 1\" \"data 2\" -m var -s \"graph.png\""

def main(argv):
    dictarg = readargv(argv)

    func = dictarg['func']
    ds = []
    for filename in dictarg['files']:
        f = open(filename)
        try:
            data = json.load(f)
            loaddata(ds, func, data)
        finally:
            f.close()

    if func in [FUNC_LOGINDEG, FUNC_HISTINDEG]:
        xlabel = 'Indegree'
    elif func in [FUNC_LOGOUTDEG, FUNC_HISTOUTDEG]:
        xlabel = 'Outdegree'

    if func == FUNC_FAIL:
        plotfailnodes(ds, getargval(dictarg, '-l'), getargval(dictarg, '-m', ['var'])[0], getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_LOGINDEG, FUNC_LOGOUTDEG]:
        # loglog indegree distribution
        drawloglogdist(ds, xlabel, getargval(dictarg, '-l'), getargval(dictarg, '-m', ['var'])[0], getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_HISTINDEG, FUNC_HISTOUTDEG]:
        # loglog outdegree distribution
        drawhistogram(ds, xlabel, getargval(dictarg, '-l'), getargval(dictarg, '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))

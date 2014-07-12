# plot.py

import sys
import matplotlib.pyplot as plt
import numpy as np
import json
import textwrap

GAMMA = u'\u03b3'
LOGBINBASE = 1.09
STEP = 300 #300
IFNONE = [] # to be returned when getargval does not find a key
FUNC_FAIL = '-f'
FUNC_FAILCASC = '-fc'
FUNC_EFF = '-e'
FUNC_LOGINDEG = '-li'
FUNC_LOGOUTDEG = '-lo'
FUNC_HISTINDEG = '-hi'
FUNC_HISTOUTDEG = '-ho'
FUNC_DISTINDEG = '-di'
FUNC_DISTOUTDEG = '-do'
FUNCOPTS = (FUNC_FAIL, FUNC_FAILCASC, FUNC_EFF, FUNC_LOGINDEG, FUNC_LOGOUTDEG, FUNC_HISTINDEG, FUNC_HISTOUTDEG, FUNC_DISTINDEG, FUNC_DISTOUTDEG)

MARKERS = {'var-':['wo-', 'ks-', 'wv-', 'kD-', 'w+-', 'kx-', 'w*-', 'k|-', 'wp-', 'k.-', 'w,-', 'k1-', 'w2-', 'k3-', 'w4-',\
                 'ko-', 'ws-', 'kv-', 'wD-', 'k+-', 'wx-', 'k*-', 'w|-', 'kp-', 'w.-', 'k,-', 'w1-', 'k2-', 'w3-', 'k4-']
        , 'sym-':['wo-', 'ko-', 'ws-', 'ks-', 'wv-', 'kv-', 'wD-', 'kD-', 'w+-', 'k+-', 'wx-', 'kx-', 'w*-', 'k*-', 'w|-', 'k|-',\
                 'wp-', 'kp-', 'w.-', 'k.-', 'w,-', 'k,-', 'w1-', 'k1-', 'w2-', 'k2-', 'w3-', 'k3-', 'w4-', 'k4-']
        , 'var':['wo', 'ks', 'wv', 'kD', 'w+', 'kx', 'w*', 'k|', 'wp', 'k.', 'w,', 'k1', 'w2', 'k3', 'w4',\
                 'ko', 'ws', 'kv', 'wD', 'k+', 'wx', 'k*', 'w|', 'kp', 'w.', 'k,', 'w1', 'k2', 'w3', 'k4']
        , 'sym':['wo', 'ko', 'ws', 'ks', 'wv', 'kv', 'wD', 'kD', 'w^', 'k^', 'wx', 'kx', 'w*', 'k*', 'w|', 'k|',\
                 'wp', 'kp', 'w.', 'k.', 'w,', 'k,', 'w1', 'k1', 'w2', 'k2', 'w3', 'k3', 'w4', 'k4']
        , 'black-':['ko-', 'ks-', 'kv-', 'kD-', 'k+-', 'kx-', 'k*-', 'k|-', 'kp-', 'k.-', 'k,-', 'k1-', 'k2-', 'k3-', 'k4-']
        , 'black':['ko', 'ks', 'kv', 'kD', 'k+', 'kx', 'k*', 'k|', 'kp', 'k.', 'k,', 'k1', 'k2', 'k3', 'k4']
        , 'white':['wo', 'ws', 'wv', 'wD', 'w+', 'wx', 'w*', 'w|', 'wp', 'w.', 'w,', 'w1', 'w2', 'w3', 'w4']}

def drawhistogram(ds, xlabel, labels, filename=None, nbins=50, normed=False, facecolor='green', alpha=0.5, histtype='step', log=False):
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

def drawloglogdist(ds, xlabel, ylabel, title, labels, markset='var', filename=None, density=True):
    # degree distribution in loglog scale

    lblgamma = u'%s = %%#.2f' % (GAMMA)
    itm = iter(MARKERS[markset])
    j = 0
    for degrees, maxdegree in ds:
        lbins = logbins(maxdegree, amin=0, base=LOGBINBASE)
        y, bins = np.histogram(degrees, bins=lbins, density=density)
        #y, bins = np.histogram(degrees, bins=100, density=density)
        #print sum(y)
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
        plt.plot(xforlog, 10**p(logx), mark[0] + ':')

    plt.loglog()
    plt.title('\n'.join(textwrap.wrap(title, 50)))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

#    # inset
#    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
#    from mpl_toolkits.axes_grid1.inset_locator import mark_inset
#
#    axins = zoomed_inset_axes(ax, 6, loc=1) # zoom = 6
#    axins.imshow(Z2, extent=extent, interpolation="nearest",
#                 origin="lower")
#
#    # sub region of the original image
#    x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9
#    axins.set_xlim(x1, x2)
#    axins.set_ylim(y1, y2)
#
#    plt.xticks(visible=False)
#    plt.yticks(visible=False)
#
    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def plotdata(ds, labels, title
    , xylabels # {'x':'...', 'y':'...'}
    , markset='var'
    , filename=None
    , isbase=True
    , logx=False
    , logy=False
    , isline=True
    , legloc=2):
    # plot degree distribution from data set
    # data set is a list of x and y data to plot

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.8])

    itm = iter(MARKERS[markset])
    maxxy = 0
    i = 0
    for xy in ds:
        try:
            mark = itm.next()
            if not isline:
                mark = mark[:-1]
        except AttributeError:
            itm = iter(MARKERS[markset])
            mark = itm.next()

        if i < len(labels):
            ax.plot(xy[0], xy[1], mark, label=labels[i])
            i += 1
        else:
            ax.plot(xy[0], xy[1], mark)

        if isbase:
            currmaxxy = max(max(xy[0]), max(xy[1]))
            if maxxy < currmaxxy:
                maxxy = currmaxxy

    if isbase:
        # create baseline x=y
        ax.plot([0, maxxy], [0, maxxy], 'g-')

    #ax.set_title(title)
    ax.set_title('\n'.join(textwrap.wrap(title, 50)))
    ax.set_xlabel(xylabels['x'])
    ax.set_ylabel(xylabels['y'])
    if len(labels) > 0:
        #ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        #ax.legend(bbox_to_anchor=(0, 1), ncol=2, loc=2, borderaxespad=0.)
        ax.legend(ncol=2, loc=legloc, borderaxespad=0.)

    if logx and logy:
        ax.loglog()
    elif logx:
        ax.semilogx()
    elif logy:
        ax.semilogy()

    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def plotdegdist(ds, labels, markset='var', filename=None
    , title='Degree distribution'
    , xylabels={'x':'Degree', 'y':'Number of Nodes'}
    , nbins=20
    , density=False
    , logx=False
    , logy=False
    , norm=True):
    # plot degree distribution from data set
    # data set is a list of x and y data to plot

    lsdeg = []
    for degrees in ds:
        y, bins = np.histogram(degrees, bins=nbins, density=density, normed=False)
        #print bins
        x = bins[:-1]

        if norm:
            nbofnodes = float(sum(y))

        lsy = []; lsx = []
        for i in range(len(y)):
            if y[i] > 0:
                if norm:
                    lsy.append(y[i] / nbofnodes)
                else:        
                    lsy.append(y[i])
                lsx.append(round(x[i]))

        lsdeg.append([lsx, lsy])
#        lsdeg.append([x, y])

    plotdata(lsdeg, labels, title, xylabels
        , markset, filename, isbase=False, logx=logx, logy=logy, isline=False)

    #print lsdeg

def plotfailnodes(ds, labels, markset='var', filename=None
    , isbase=True
    , title='Random cascading failure in service network'
    , xylabels={'x':'Nodes removed', 'y':'Nodes fail'}
    , legloc=2):
    # plot fail nodes from data set
    # data set is a list of x and y data to plot

    plotdata(ds, labels, title, xylabels
        , markset, filename, isbase, legloc=legloc)

def plotcasceff(ds, labels, randomfails, xylabels, xaxis
    , markset='var'
    , filename=None
    , isbase=False
    , title='Random cascading failure in service network'
    , legloc=2):
    # plot cascading effect where the data series are different number of nodes fail randomly
    # the y axis (cascading effect, number of active nodes) is the number of cascading fail nodes
    # the x axis is either the number of alternative, the number of dependency, the combination of both

    plots = []
    # series
    for r in randomfails:

        x = [] # holds the degree of interdependency 
        y = [] # holds the number of cascaded fail nodes
        # geting xy coordinates
        for i in range(len(ds)):
            val = ds[i]
            nodesremoved = val[0] # number of randomly fail nodes
            nodesfail = val[1] # number of nodes fail (both randomly chosen and cascaded fail nodes)
            reccount = len(nodesremoved)

            j = 0
            found = False
            while j < reccount and not found:
                if float(r) > nodesremoved[j]:
                    j += 1
                else:
                    # found
                    found = True

            if found:
                x.append(float(xaxis[i]))
                y.append(nodesfail[j] - nodesremoved[j])

        plots.append([x, y])

    plotdata(plots, labels, title, xylabels
        , markset, filename, isbase, legloc=legloc)

def loaddata(ds, func, data, step=STEP, norm=True):
    if func in [FUNC_FAIL, FUNC_FAILCASC, FUNC_EFF]:
        nbofnodes = 1
        if norm:
            # get the number of nodes
            nbofnodes = float(data['nodescreated'][-1])

        nodesremoved = data['nodesremoved']
        found = False; i = 0
        while not found and i < len(nodesremoved):
            if nodesremoved[i] > 0:
                found = True;
            else:
                i += 1

        x = []
        y = []
        if found:
            if func == FUNC_FAILCASC:
                # for y axis, only calculate the number of nodes that fail because of cascading failure
                # excluding those randomly chosen to be fail

                for j in range(i, len(nodesremoved), step):
                    xval = nodesremoved[j] / nbofnodes
                    yval = data['nodesfail'][j] / nbofnodes - xval
                    x.append(xval)
                    y.append(yval)

            else:
                # FUNC_FAIL, FUNC_EFF

                x = [rmv / nbofnodes for rmv in nodesremoved[i::step]]
                y = [fail / nbofnodes for fail in data['nodesfail'][i::step]]

        ds.append([x, y])

#        if func == FUNC_EFF:
#            # ds = [[nodesremoved, nodesfail, xval], ...]
#            ds[-1].append(data['xval'])

    elif func in [FUNC_DISTINDEG, FUNC_DISTOUTDEG]:
        if FUNC_DISTINDEG:
            degrees = data['indegree']
        else:
            degrees = data['outdegree']

        ds.append(degrees)

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

        elif currarg not in ['-l', '-m', '-s', '-x', '-r', '-xl', '-yl', '-t', '-logx', '-logy', '-loc']:
            printusage()
            return

        readargv(argv, pos + 1, currarg, dictarg)

    else:
        addtodictarg(dictarg, opt, currarg)
        readargv(argv, pos + 1, opt, dictarg)

    return dictarg

def getargval(dictarg, key, ifnone=IFNONE):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def printusage():
    print "Usage: python plot.py -<function option> <file-1> [file-n] [-l label-1 label-n] [-m markset] [-s filename] [-x x-1 x-m -r r-1 r-p]"
    print "Example: python plot.py -f data1.json data2.json -l \"data 1\" \"data 2\" -m var -s \"graph.png\""

def main(argv):
    dictarg = readargv(argv)

    func = dictarg['func']
    ds = []
    for i in range(len(dictarg['files'])):
        f = open(dictarg['files'][i])
        try:
            data = json.load(f)

            #if func == FUNC_EFF:
            #    data['xval'] = dictarg['xval'][i]

            loaddata(ds, func, data)
        finally:
            f.close()

    if func in [FUNC_LOGINDEG, FUNC_HISTINDEG]:
        xlabel = 'In-degree'
    elif func in [FUNC_LOGOUTDEG, FUNC_HISTOUTDEG]:
        xlabel = 'Out-degree'

    if func in [FUNC_FAIL, FUNC_FAILCASC]:
#        if func == FUNC_FAIL:
#            xylabels={'x':'Number of nodes fail randomly', 'y':'Total number of nodes fail (randomly + cascaded fail)'}
#        else:
#            # FUNC_FAILCASC
#            xylabels={'x':'Number of nodes fail randomly', 'y':'Number of cascaded fail nodes'}

        plotfailnodes(ds
            , getargval(dictarg, '-l')
            , getargval(dictarg, '-m', ['var'])[0]
            , getargval(dictarg, '-s', [None])[0]
            , isbase=func==FUNC_FAIL
            , xylabels={'x': getargval(dictarg, '-xl', [''])[0]
            , 'y': getargval(dictarg, '-yl', [''])[0]}
            , title=getargval(dictarg, '-t', [''])[0]
            , legloc=int(getargval(dictarg, '-loc')[0]))

    elif func == FUNC_EFF:
        plotcasceff(ds, getargval(dictarg, '-l'), getargval(dictarg, '-r'), {'x': getargval(dictarg, '-xl')[0], 'y': getargval(dictarg, '-yl')[0]}
                    , getargval(dictarg, '-x'), getargval(dictarg, '-m', ['var'])[0], getargval(dictarg, '-s', [None])[0], title=getargval(dictarg, '-t')[0], legloc=int(getargval(dictarg, '-loc')[0]))

    elif func in [FUNC_LOGINDEG, FUNC_LOGOUTDEG]:
        # loglog degree distribution
        drawloglogdist(ds, xlabel=getargval(dictarg, '-xl', [''])[0], ylabel=getargval(dictarg, '-yl', [''])[0], title=getargval(dictarg, '-t', [''])[0], labels=getargval(dictarg, '-l'), markset=getargval(dictarg, '-m', ['var'])[0], filename=getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_HISTINDEG, FUNC_HISTOUTDEG]:
        # histogram degree distribution
        drawhistogram(ds, xlabel, getargval(dictarg, '-l'), getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_DISTINDEG, FUNC_DISTOUTDEG]:
        # degree distribution plot

        if FUNC_DISTINDEG:
            title = 'Degree distribution of exponential network'
            xylabels = {'x':'k (degree)', 'y':'P(k)'}
        else:
            title = 'Outdegree distribution'
            xylabels = {'x':'Outdegree', 'y':'Number of nodes'}

        logx = False
        arglogx = getargval(dictarg, '-logx')
        if arglogx:
            logx = int(arglogx[0]) > 0

        logy = False
        arglogy = getargval(dictarg, '-logy')
        if arglogy:
            logy = int(arglogy[0]) > 0

        plotdegdist(ds, getargval(dictarg, '-l'), getargval(dictarg, '-m', ['var'])[0], getargval(dictarg, '-s', [None])[0]
            , title=title, xylabels=xylabels, nbins=50, logx=logx,  logy=logy)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


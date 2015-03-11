# plot.py

import sys
import matplotlib.pyplot as plt
import numpy as np
import json
import textwrap
import csv

GAMMA = u'\u03b3'
LOGBINBASE = 1.1
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
FUNC_PLOTFROMFILE = '-pl'
FUNC_PRINTDEPTH = '-pd'
FUNCOPTS = (FUNC_FAIL, FUNC_FAILCASC, FUNC_EFF, FUNC_LOGINDEG, FUNC_LOGOUTDEG, FUNC_HISTINDEG, FUNC_HISTOUTDEG, FUNC_DISTINDEG, FUNC_DISTOUTDEG, FUNC_PRINTDEPTH, FUNC_PLOTFROMFILE)
LINESTYLES = ('-', '--', '-.', ':')
FILENAME = 'depthstat.csv'
LOCONPLOT = 11 # legend is written at the end of each series
LOCOUTRIGHT = 22 # legend is located outside the graph on the right
LOCOUTBELOW = 29 # below the graph

MARKERS = {'var-':['wo-', 'ks-', 'wv-', 'kD-', 'w+-', 'kx-', 'w*-', 'k|-', 'wp-', 'k.-', 'w,-', 'k1-', 'w2-', 'k3-', 'w4-',\
                 'ko-', 'ws-', 'kv-', 'wD-', 'k+-', 'wx-', 'k*-', 'w|-', 'kp-', 'w.-', 'k,-', 'w1-', 'k2-', 'w3-', 'k4-']
        , 'var':['wo', 'ks', 'wv', 'kD', 'w+', 'kx', 'w*', 'k|', 'wp', 'k.', 'w,', 'k1', 'w2', 'k3', 'w4',\
                 'ko', 'ws', 'kv', 'wD', 'k+', 'wx', 'k*', 'w|', 'kp', 'w.', 'k,', 'w1', 'k2', 'w3', 'k4']
        , 'sym-':['wo-', 'ko-', 'ws-', 'ks-', 'w^-', 'k^-', 'wv-', 'kv-', 'wD-', 'kD-', 'w+-', 'k+-', 'wx-', 'kx-', 'w*-', 'k*-', 'w|-', 'k|-',\
                 'wp-', 'kp-', 'w.-', 'k.-', 'w,-', 'k,-', 'w1-', 'k1-', 'w2-', 'k2-', 'w3-', 'k3-', 'w4-', 'k4-']
        , 'sym':['wo', 'ko', 'ws', 'ks', 'w^', 'k^', 'wv', 'kv', 'wD', 'kD', 'w^', 'k^', 'wx', 'kx', 'w*', 'k*', 'w|', 'k|',\
                 'wp', 'kp', 'w.', 'k.', 'w,', 'k,', 'w1', 'k1', 'w2', 'k2', 'w3', 'k3', 'w4', 'k4']
        , 'trisym-':{'linestyle':'-', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['0.3', 'white', 'black']}
        , 'trisym':{'linestyle':'', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['0.3', 'white', 'black']}
        , 'tricol-':{'linestyle':'-', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['red', 'blue', 'orange']}
        , 'tricol':{'linestyle':'', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['red', 'blue', 'orange']}
        , 'trired-':{'linestyle':'-', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['red']}
        , 'trired':{'linestyle':'', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['red']}
        , 'triblue-':{'linestyle':'-', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['blue']}
        , 'triblue:':{'linestyle':':', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['blue']}
        , 'triblue':{'linestyle':'', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['blue']}
        , 'triorange-':{'linestyle':'-', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['orange']}
        , 'triorange:':{'linestyle':':', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['orange']}
        , 'triorange':{'linestyle':'', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['orange']}
        , 'tribrown':{'linestyle':'', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['sienna']}
        , 'trifive-':{'linestyle':'-', 'markers':['o', 's', '^', 'v', 'D', 'p', '+', 'x', '*', '|', '.', ',', '1', '2', '3', '4'],  'markerfacecolors':['red', 'blue', 'orange', 'green', 'cyan']}
        , 'black-':['ko-', 'ks-', 'k^-', 'kv-', 'kD-', 'k+-', 'kx-', 'k*-', 'k|-', 'kp-', 'k.-', 'k,-', 'k1-', 'k2-', 'k3-', 'k4-']
        , 'black':['ko', 'ks', 'k^', 'kv', 'kD', 'k+', 'kx', 'k*', 'k|', 'kp', 'k.', 'k,', 'k1', 'k2', 'k3', 'k4']
        , 'white-':['wo-', 'ws-', 'w^-', 'wv-', 'wD-', 'w+-', 'wx-', 'w*-', 'w|-', 'wp-', 'w.-', 'w,-', 'w1-', 'w2-', 'w3-', 'w4-']
        , 'white':['wo', 'ws', 'w^', 'wv', 'wD', 'w+', 'wx', 'w*', 'w|', 'wp', 'w.', 'w,', 'w1', 'w2', 'w3', 'w4']
        , 'red-':['ro-', 'rs-', 'r^-', 'rv-', 'rD-', 'r+-', 'rx-', 'r*-', 'r|-', 'rp-', 'r.-', 'r,-', 'r1-', 'r2-', 'r3-', 'r4-']
        , 'red':['ro', 'rs', 'r^', 'rv', 'rD', 'r+', 'rx', 'r*', 'r|', 'rp', 'r.', 'r,', 'r1', 'r2', 'r3', 'r4']
        , 'green':['go', 'gs', 'g^', 'gv', 'gD', 'g+', 'gx', 'g*', 'g|', 'gp', 'g.', 'g,', 'g1', 'g2', 'g3', 'g4']
        , 'blue':['bo', 'bs', 'b^', 'bv', 'bD', 'b+', 'bx', 'b*', 'b|', 'bp', 'b.', 'b,', 'b1', 'b2', 'b3', 'b4']
        , 'magenta':['mo', 'ms', 'm^', 'mv', 'mD', 'm+', 'mx', 'm*', 'm|', 'mp', 'm.', 'm,', 'm1', 'm2', 'm3', 'm4']
        , 'cyan':['co', 'cs', 'c^', 'cv', 'cD', 'c+', 'cx', 'c*', 'c|', 'cp', 'c.', 'c,', 'c1', 'c2', 'c3', 'c4']
        , 'plus':['k+']
        , 'diamond':['gd']
        , 'reddia':['rd']
        , 'reddia-':['rd-']
        , 'bluepenta':['bp']
        , 'bluepenta-':['bp-']
        , 'trihexaorg':{'linestyle':'', 'markers':['v'],  'markerfacecolors':['orange']}
        , 'trihexaorg-':{'linestyle':'-', 'markers':['v'],  'markerfacecolors':['orange']}
        , 'triplus':{'linestyle':'', 'markers':['+'],  'markerfacecolors':['sienna']}
        , 'star':['m*']
}

def preparetrimarker(markset):
    tri = MARKERS[markset]
    markers = iter(tri['markers'])
    markerfacecolors = iter(tri['markerfacecolors'])
    linestyle = ''
    if markset[-1] in LINESTYLES:
        linestyle = markset[-1]
    
    return markers, markerfacecolors, linestyle

def prepareunimarker(markset):
    return iter(MARKERS[markset])

def gettrimarker(markset, markers, markerfacecolors, counter):
    if counter % 3 == 0:
        try:
            marker = markers.next()
        except StopIteration:
            tri = MARKERS[markset]
            markers = iter(tri['markers'])
            marker = markers.next()
    else:
        marker = None

    counter += 1

    try:
        markerfacecolor = markerfacecolors.next()
    except StopIteration:
        tri = MARKERS[markset]
        markerfacecolors = iter(tri['markerfacecolors'])
        markerfacecolor = markerfacecolors.next()

    return markers, marker, markerfacecolors, markerfacecolor, counter

def getunimarker(markset, itm, isline):
    try:
        mark = itm.next()
        if not isline and markset[:-1] == '-':
            mark = mark[:-1]
    except StopIteration:
        itm = iter(MARKERS[markset])
        mark = itm.next()

    markerfacecolor = mark[0]
    marker = mark[1]
    linestyle = ''
    if len(mark) > 2:
        linestyle = mark[2]

    return itm, marker, markerfacecolor, linestyle

def drawhistogram(ds, xlabel, labels, nbins=50, normed=False, facecolor='green', alpha=0.5, histtype='step', log=False):
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

#    if filename:
#        plt.savefig(filename)
#    else:
#        plt.show()

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

def drawloglogdist(ds, xlabel, ylabel, title
    , labels
    , markset='var'
    , density=True
    , xlim=None, ylim=None
    , axisfsize=None
    , logbinbase=LOGBINBASE
    , showexp=True
    , isline=False
    , legloc=2
    , ax=None
    , ncol=1
    , numpoints=1):
    # degree distribution in loglog scale

    if not ax:
        # ax not defined, add axes
        #ax = plt.axes([0.1, 0.1, 0.6, 0.78])
        ax = plt.gca()

    lblgamma = u'%s = %%#.2f' % (GAMMA)

    if markset[:3] == 'tri':
        markers, markerfacecolors, linestyle = preparetrimarker(markset)
        counter = 0
    else:
        itm = prepareunimarker(markset)

    j = 0
    for degrees, maxdegree in ds:
        lbins = logbins(maxdegree, amin=0, base=logbinbase)
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

        if markset[:3] == 'tri':
            markers, newmarker, markerfacecolors, markerfacecolor, counter = gettrimarker(markset, markers, markerfacecolors, counter)
            if newmarker:
                marker = newmarker
        else:
            itm, marker, markerfacecolor, linestyle = getunimarker(markset, itm, isline)

        gamma, logA = np.polyfit(logx, logy, 1)
        p = np.poly1d([gamma, logA])
        if j < len(labels):
            if showexp:
                label = '%s, %s' % (labels[j], lblgamma % (-1 * gamma))
            else:
                label = labels[j]
            #plt.plot(x, y, mark[:-1], label = '%s, %s' % (labels[j], lblgamma % (-1 * gamma)))
            j += 1
        else:
            if showexp:
                label = lblgamma % (-1 * gamma)
            else:
                label = ''
            #plt.plot(x, y, mark[:-1], label = lblgamma % (-1 * gamma))

        #plt.plot(x, y, marker=marker, markerfacecolor=markerfacecolor, linestyle=linestyle, label=label)
        ax.plot(x, y, marker=marker, markerfacecolor=markerfacecolor, linestyle=linestyle, label=label, color=markerfacecolor)

        #plt.plot(xforlog, 10**p(logx), mark[0] + ':')
        #plt.plot(xforlog, 10**p(logx), markerfacecolor=markerfacecolor, linestyle=':')
        ax.plot(xforlog, 10**p(logx), markerfacecolor=markerfacecolor, linestyle=':')

    #setaxislim(xlim, ylim, plt=plt)
    setaxislim(xlim, ylim, ax=ax)

    #plt.loglog()
    #plt.title('\n'.join(textwrap.wrap(title, 50)))
    #plt.xlabel(xlabel, fontsize=axisfsize)
    #plt.ylabel(ylabel, fontsize=axisfsize)
    #plt.legend(numpoints=1, loc=4)

    ax.loglog()
    ax.set_title('\n'.join(textwrap.wrap(title, 50)))
    ax.set_xlabel(xlabel, fontsize=axisfsize)
    ax.set_ylabel(ylabel, fontsize=axisfsize)

    if len(labels) > 0: 
        if legloc < LOCONPLOT:
            # legend is located according to legloc position
            #ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            #ax.legend(bbox_to_anchor=(0, 1), ncol=2, loc=2, borderaxespad=0.)
            #ax.legend(ncol=2, loc=legloc, borderaxespad=0.)
            axpos = ax.get_position()
            ax.set_position([axpos.x0, axpos.y0, 0.76, axpos.height])
            ax.legend(ncol=ncol, loc=legloc, borderaxespad=0., prop={'size':14}, numpoints=numpoints)
            #ax.legend(ncol=1, loc=legloc, borderaxespad=0., prop={'size':14}, numpoints=1)

        elif legloc == LOCOUTRIGHT:
            # legend is located on the right of the graph
            ax.legend(bbox_to_anchor=(1.02, 1.), loc=2, borderaxespad=0., ncol=ncol, numpoints=numpoints)

        elif legloc == LOCOUTBELOW:
            # legend is located below the graph 
            # shrink the axis
            axpos = ax.get_position()
            ax.set_position([axpos.x0, axpos.y0 + axpos.height * 0.2, 0.78, axpos.height * 0.8])
            ax.legend(bbox_to_anchor=(0.5, -0.15), loc=9, borderaxespad=0., numpoints=numpoints, ncol=ncol, prop={'size':13})

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
#    if filename:
#        plt.savefig(filename)
#    else:
#        plt.show()

def plotdata(ds, labels, title
    , xylabels # {'x':'...', 'y':'...'}
    , markset='var'
    , isbase=True
    , logx=False
    , logy=False
    , xlim=None
    , ylim=None
    , isline=True
    , legloc=2
    , axisfsize=None
    , ax=None
    , polyfit=False
    , ncol=1
    , numpoints=1
    , legmode='normal'
    , bbox_to_anchor=None):
    # plot degree distribution from data set
    # data set is a list of x and y data to plot

    if not ax:
        # ax not defined, add axes
        #ax = plt.axes([0.1, 0.1, 0.6, 0.78])
        ax = plt.gca()

    if markset[:3] == 'tri':
        markers, markerfacecolors, linestyle = preparetrimarker(markset)
        counter = 0
    else:
        itm = prepareunimarker(markset)

    maxxy = 0
    i = 0
    for xy in ds:
        # markers related
        if markset[:3] == 'tri':
            markers, newmarker, markerfacecolors, markerfacecolor, counter = gettrimarker(markset, markers, markerfacecolors, counter)
            if newmarker:
                marker = newmarker
        else:
            itm, marker, markerfacecolor, linestyle = getunimarker(markset, itm, isline)

        if i < len(labels):
            #ax.plot(xy[0], xy[1], mark, label=labels[i])
            ax.plot(xy[0], xy[1], label=labels[i], color='black', linestyle=linestyle, marker=marker, markerfacecolor=markerfacecolor)

            if legloc == LOCONPLOT:
                # legend is written at the end of each series
                ax.annotate(labels[i], xy=(xy[0][-1],xy[1][-1]), xytext=(10, 0), textcoords='offset points')

            i += 1

        else:
            #ax.plot(xy[0], xy[1], mark)
            ax.plot(xy[0], xy[1], color='black', linestyle=linestyle, marker=marker, markerfacecolor=markerfacecolor)

        if isbase:
            currmaxxy = max(max(xy[0]), max(xy[1]))
            if maxxy < currmaxxy:
                maxxy = currmaxxy

        if polyfit:
            z = np.polyfit(xy[0], xy[1], 3)
            f = np.poly1d(z)
            xfit = np.linspace(xy[0][0], xy[0][-1], 100)
            yfit = f(xfit)
            ax.plot(xfit, yfit, markerfacecolor=markerfacecolor, linestyle=':')

    if isbase:
        # create baseline x=y
        ax.plot([0, maxxy], [0, maxxy], 'g-')

    # set xlim ylim
    setaxislim(xlim, ylim, ax=ax)

    #ax.set_title(title)
    ax.set_title('\n'.join(textwrap.wrap(title, 50)))
    #ax.set_xlabel('$k_{in}$')
    ax.set_xlabel(xylabels['x'], fontsize=axisfsize)
    #ax.set_ylabel('$P(k_{in})$')
    ax.set_ylabel(xylabels['y'], fontsize=axisfsize)
    if len(labels) > 0: 
        if legloc < LOCONPLOT:
            # legend is located according to legloc position
            #ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
            #ax.legend(bbox_to_anchor=(0, 1), ncol=2, loc=2, borderaxespad=0.)
            #ax.legend(ncol=2, loc=legloc, borderaxespad=0.)
            axpos = ax.get_position()
            ax.set_position([axpos.x0, axpos.y0, 0.76, axpos.height])
            ax.legend(ncol=ncol, loc=legloc, borderaxespad=0., prop={'size':14}, numpoints=numpoints, mode=legmode, bbox_to_anchor=bbox_to_anchor)
            #ax.legend(ncol=1, loc=legloc, borderaxespad=0., prop={'size':14}, numpoints=1)

        elif legloc == LOCOUTRIGHT:
            # legend is located on the right of the graph
            ax.legend(bbox_to_anchor=(1.02, 1.), loc=2, borderaxespad=0., ncol=ncol, numpoints=numpoints, mode=legmode)


        elif legloc == LOCOUTBELOW:
            # legend is located below the graph 
            # shrink the axis
            axpos = ax.get_position()
            ax.set_position([axpos.x0, axpos.y0 + axpos.height * 0.2, 0.78, axpos.height * 0.8])
            ax.legend(bbox_to_anchor=(0.5, -0.15), loc=9, borderaxespad=0., ncol=ncol, numpoints=numpoints, prop={'size':13}, mode=legmode)

    if logx and logy:
        ax.loglog()
    elif logx:
        ax.semilogx()
    elif logy:
        ax.semilogy()

    return ax

#    if filename:
#        plt.savefig(filename)
#    else:
#        plt.show()

def plotdegdist(ds, labels, markset='var' 
    , title='Degree distribution'
    , xylabels={'x':'Degree', 'y':'Number of Nodes'}
    , nbins=20
    , density=False
    , logx=False
    , logy=False
    , norm=True
    , xlim=None
    , ylim=None
    , legloc=2
    , axisfsize=None
    , ax=None
    , polyfit=False
    , ncol=1
    , numpoints=1):
    # plot degree distribution from data set
    # data set is a list of x and y data to plot

#    print nbins

    lsdeg = []
    for degrees in ds:
        y, bins = np.histogram(degrees, bins=nbins, density=density, normed=False)
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
        , markset, isbase=False, logx=logx, logy=logy, xlim=xlim, ylim=ylim, isline=False, legloc=legloc, axisfsize=axisfsize, ax=ax, polyfit=polyfit
        , ncol=ncol, numpoints=numpoints)

    #print lsdeg

def plotfailnodes(ds, labels, markset='var'
    , isbase=True
    , title='Random cascading failure in service network'
    , xylabels={'x':'Nodes removed', 'y':'Nodes fail'}
    , legloc=2
    , xlim=None
    , ylim=None
    , axisfsize=None
    , ax=None
    , ncol=1
    , numpoints=1
    , legmode='normal'
    , bbox_to_anchor=None):

    # plot fail nodes from data set
    # data set is a list of x and y data to plot

    return plotdata(ds, labels, title, xylabels
        , markset, isbase, legloc=legloc, xlim=xlim, ylim=ylim, axisfsize=axisfsize, ax=ax
        , ncol=ncol, numpoints=numpoints, legmode=legmode, bbox_to_anchor=bbox_to_anchor)

def plotcasceff(ds, labels, randomfails, xylabels, xaxis
    , markset='var'
    , isbase=False
    , title='Random cascading failure in service network'
    , legloc=2
    , xlim=None
    , ylim=None
    , plotfile=None
    , axisfsize=None
    , ncol=1
    , numpoints=1):
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

    if plotfile:
        # save plot file
        f = open(plotfile, 'w')
        try:
            json.dump(plots, f)
        finally:
            f.close()

    plotdata(plots, labels, title, xylabels
        , markset, isbase, legloc=legloc, xlim=xlim, ylim=ylim, axisfsize=axisfsize
        , ncol=ncol, numpoints=numpoints)

def printdepth(ds, filename):
    if not filename:
        filename = FILENAME

    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile)

        i = 1
        for series in ds:
            print series[0]
            print '%s: %4d' % ('maxdepth'.ljust(13), series[1])
            print '%s: %7.2f' % ('avgdepth'.ljust(13), series[2])
            print '%s: %7.2f' % ('maxmeandepth'.ljust(13), series[3])
            print '%s: %7.2f' % ('avgmeandepth'.ljust(13), series[4])
            print
            
            stats = [stat for stat in series]
            writer.writerow(stats)

            i += 1

def setaxislim(xlim, ylim, plt=None, ax=None):
    if xlim:
        if plt:
            plt.xlim(xmax=float(xlim[-1]))
        else:
            # ax
            ax.set_xlim(right=float(xlim[-1]))
        if len(xlim) > 1:
            if plt:
                plt.xlim(xmin=float(xlim[0]))
            else:
                # ax
                ax.set_xlim(left=float(xlim[0]))
    if ylim:
        if plt:
            plt.ylim(ymax=float(ylim[-1]))
        else:
            # ax
            ax.set_ylim(top=float(ylim[-1]))
        if len(ylim) > 1:
            if plt:
                plt.ylim(ymin=float(ylim[0]))
            else:
                # ax
                ax.set_ylim(bottom=float(ylim[0]))

def loaddata(ds, func, data, filename, step=STEP, norm=True):
    if func in [FUNC_FAIL, FUNC_FAILCASC, FUNC_EFF]:
        nbofnodes = 1
#        nbofcomps = 1
        if norm:
            # number of all nodes
            nbofnodes = float(data['nodescreated'][-1])
#            # number of composite nodes, i.e. those having outdegree
#            nbofcomps = 0.0
#            for deg in data['outdegree']:
#                if deg > 0:
#                    nbofcomps += 1 
#        ###
#        print 'nbofcomps: '+ str(nbofcomps)
        nodesremoved = data['nodesremoved']
        found = False; i = 0
        while not found and i < len(nodesremoved):
            if nodesremoved[i] > 0:
                found = True;
            else:
                i += 1

#        print 'i: %d' % i
#        print 'nbofnodes: %d' % nbofnodes
        x = []
        y = []
        if found:
            if func == FUNC_FAILCASC:
                # for y axis, only calculate the number of nodes that fail because of cascading failure
                # excluding those randomly chosen to be fail

                #for j in range(i, len(nodesremoved), step):
                for j in range(len(nodesremoved)-1, i-1, -step):
                    xval = nodesremoved[j] / nbofnodes
                    yval = data['nodesfail'][j] / nbofnodes - xval
#                    yval = (data['nodesfail'][j] - nodesremoved[j]) / nbofcomps
                    x.append(xval)
                    y.append(yval)
#                    ###
#                    print 'nodesremoved[i] %d' % nodesremoved[j]
#                    print "data['nodesfail'][j] %d" % data['nodesfail'][j]
#                    print "xval %.2f" % xval
#                    print "yval %.2f" % yval
#                    print "------"
#                print x
#                print y

            else:
                # FUNC_FAIL, FUNC_EFF

                #x = [rmv / nbofnodes for rmv in nodesremoved[i::step]]
                #y = [fail / nbofnodes for fail in data['nodesfail'][i::step]]
                if i == 0:
                    x = [rmv / nbofnodes for rmv in nodesremoved[::-step]]
                    y = [fail / nbofnodes for fail in data['nodesfail'][::-step]]
                else:
                    stop = i - 1
                    x = [rmv / nbofnodes for rmv in nodesremoved[:stop:-step]]
                    y = [fail / nbofnodes for fail in data['nodesfail'][:stop:-step]]

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

    elif func in FUNC_PRINTDEPTH:
        ds.append([filename, data['maxdepth'], data['avgdepth'], data['maxmeandepth'], data['avgmeandepth']])

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

        elif currarg not in ['-l', '-m', '-s', '-x', '-r', '-xl', '-yl', '-t', '-logx', '-logy', '-loc', '-b', '-xlim', '-ylim', '-v', '-axisfsize', '-j', '-lb', '-g', '-ncol', '-numpoints', '-lm', '-lbb']:
            print "*** %s" % currarg
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

def processplot(plt, filename=None):
    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def main(argv):
    dictarg = readargv(argv)

    step = STEP
    argstep = getargval(dictarg, '-j')
    if argstep:
        step = int(argstep[0])

    func = dictarg['func']
    ds = []
    for i in range(len(dictarg['files'])):
        f = open(dictarg['files'][i])
        try:
            data = json.load(f)

            #if func == FUNC_EFF:
            #    data['xval'] = dictarg['xval'][i]

            loaddata(ds, func, data, dictarg['files'][i], step)
        finally:
            f.close()

    logx = False
    arglogx = getargval(dictarg, '-logx')
    if arglogx:
        logx = int(arglogx[0]) > 0

    logy = False
    arglogy = getargval(dictarg, '-logy')
    if arglogy:
        logy = int(arglogy[0]) > 0

    lb = LOGBINBASE
    arglb = getargval(dictarg, '-lb')
    if arglb:
        lb = float(arglb[0])

    xlim = getargval(dictarg, '-xlim')
    ylim = getargval(dictarg, '-ylim')

    plotfile = getargval(dictarg, '-v', [None])[0]

    if func in [FUNC_LOGINDEG, FUNC_HISTINDEG]:
        xlabel = 'In-degree'
    elif func in [FUNC_LOGOUTDEG, FUNC_HISTOUTDEG]:
        xlabel = 'Out-degree'

    axisfsize = getargval(dictarg, '-axisfsize', ['medium'])[0]
    try:
        axisfsize = int(axisfsize)
    except:
        pass

    ncol = int(getargval(dictarg, '-ncol', [1])[0])
    numpoints = int(getargval(dictarg, '-numpoints', [1])[0])

    legmode = getargval(dictarg, '-lm', ['normal'])[0]
    bbox_to_anchor = getargval(dictarg, '-lbb', None)

    if func in [FUNC_FAIL, FUNC_FAILCASC]:
#        if func == FUNC_FAIL:
#            xylabels={'x':'Number of nodes fail randomly', 'y':'Total number of nodes fail (randomly + cascaded fail)'}
#        else:
#            # FUNC_FAILCASC
#            xylabels={'x':'Number of nodes fail randomly', 'y':'Number of cascaded fail nodes'}

        plotfailnodes(ds
            , getargval(dictarg, '-l')
            , getargval(dictarg, '-m', ['var'])[0]
            , isbase=func==FUNC_FAIL
            , xylabels={'x': getargval(dictarg, '-xl', [''])[0], 'y': getargval(dictarg, '-yl', [''])[0]}
            , title=getargval(dictarg, '-t', [''])[0]
            , legloc=int(getargval(dictarg, '-loc', [2])[0])
            , xlim=xlim
            , ylim=ylim
            , axisfsize=axisfsize
            , ncol=ncol
            , numpoints=numpoints
            , legmode=legmode
            , bbox_to_anchor=bbox_to_anchor)

        processplot(plt, getargval(dictarg, '-s', [None])[0])

    elif func == FUNC_EFF:
        plotcasceff(ds
            , getargval(dictarg, '-l')
            , getargval(dictarg, '-r')
            , {'x': getargval(dictarg, '-xl')[0], 'y': getargval(dictarg, '-yl')[0]}
            , getargval(dictarg, '-x')
            , getargval(dictarg, '-m', ['var'])[0]
            , title=getargval(dictarg, '-t')[0]
            , legloc=int(getargval(dictarg, '-loc')[0])
            , plotfile=plotfile)

        processplot(plt, getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_LOGINDEG, FUNC_LOGOUTDEG]:
        # loglog degree distribution
        drawloglogdist(ds
            , xlabel=getargval(dictarg, '-xl', [''])[0]
            , ylabel=getargval(dictarg, '-yl', [''])[0]
            , title=getargval(dictarg, '-t', [''])[0]
            , labels=getargval(dictarg, '-l')
            , markset=getargval(dictarg, '-m', ['var'])[0]
            , xlim=xlim
            , ylim=ylim
            , axisfsize=axisfsize
            , logbinbase=lb
            , showexp=int(getargval(dictarg, '-g', [1])[0]))

        processplot(plt, getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_HISTINDEG, FUNC_HISTOUTDEG]:
        # histogram degree distribution
        drawhistogram(ds, xlabel, getargval(dictarg, '-l'))
        processplot(plt, getargval(dictarg, '-s', [None])[0])

    elif func in [FUNC_DISTINDEG, FUNC_DISTOUTDEG]:
        # degree distribution plot

        if func == FUNC_DISTINDEG:
            title = getargval(dictarg, '-t', ['Degree distribution of exponential network'])[0]
            xylabels = {'x':getargval(dictarg, '-xl', ['k (degree)'])[0], 'y':getargval(dictarg, '-yl', ['P(k)'])[0]}
        else:
            title = getargval(dictarg, '-t', ['Outdegree distribution'])[0]
            xylabels = {'x':getargval(dictarg, '-xl', ['Outdegree'])[0], 'y':getargval(dictarg, '-yl', ['Number of nodes'])[0]}

        plotdegdist(ds
            , getargval(dictarg, '-l')
            , getargval(dictarg, '-m', ['var'])[0]
            , title=title
            , xylabels=xylabels
            , nbins=int(getargval(dictarg, '-b', ['50'])[0])
            , logx=logx, logy=logy
            , xlim=xlim
            , ylim=ylim
            , axisfsize=axisfsize)

        processplot(plt, getargval(dictarg, '-s', [None])[0])

    elif func == FUNC_PLOTFROMFILE:
        f = open(dictarg['files'][0])
        try:
            ds = json.load(f)
        finally:
            f.close()

        plotdata(ds
            , getargval(dictarg, '-l')
            , getargval(dictarg, '-t', ['The effect of degree of dependency on cascading failure in service networks'])[0]
            , {'x': getargval(dictarg, '-xl', ['Degree of dependency $\langle dep \\rangle$'])[0], 'y': getargval(dictarg, '-yl', ['Number of cascaded fail nodes $n_c$ (in fraction)'])[0]}
            , getargval(dictarg, '-m', ['var'])[0]
            , isbase=False
            , logx=logx
            , logy=logy
            , xlim=xlim
            , ylim=ylim
            , legloc=int(getargval(dictarg, '-loc', ['1'])[0])
            , ncol=int(getargval(dictarg, '-ncol', ['1'])[0])
            , numpoints=int(getargval(dictarg, '-numpoints', ['1'])[0])
            , axisfsize=axisfsize)

        processplot(plt, getargval(dictarg, '-s', [None])[0])

    elif func == FUNC_PRINTDEPTH:
        printdepth(ds, getargval(dictarg, '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


import sys
import json
import plot as p

def getargval(dictarg, key, ifnone=p.IFNONE):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def getaxisfsize(dictarg):
    axisfsize = getargval(dictarg, '-axisfsize', ['medium'])[0]
    try:
        axisfsize = int(axisfsize)
    except:
        pass

    return axisfsize

def getlogparam(dictarg):
    logx = False
    arglogx = getargval(dictarg, '-logx')
    if arglogx:
        logx = int(arglogx[0]) > 0

    logy = False
    arglogy = getargval(dictarg, '-logy')
    if arglogy:
        logy = int(arglogy[0]) > 0

    return logx, logy

def loadarg(lsarg):
    ds = []
    for i in range(len(lsarg)):
        func = lsarg[i]['func'][0]

        step = p.STEP
        argstep = getargval(lsarg[i], '-j')
        if argstep:
            step = int(argstep[0])

        for finjson in lsarg[i]['files']:
            f = open(finjson)
            try:
                data = json.load(f)

                p.loaddata(ds, func, data, finjson, step)
            finally:
                f.close()

        xlim = getargval(lsarg[i], '-xlim')
        ylim = getargval(lsarg[i], '-ylim')

        plotfile = getargval(lsarg[i], '-v', [None])[0]

        axisfsize = getargval(lsarg[i], '-axisfsize', ['medium'])[0]
        try:
            axisfsize = int(axisfsize)
        except:
            pass

    return ds

def main(argv):
    indegarg = {'func':['-id'], 'files':['simdata/svcsimn_d2a1_1.json'], '-m':['plus'], '-t':['In-degree of random failed services and total degree of the network during network failure'], '-xl':['Timestep'], '-yl':['In-degree of random failed services'], '-l':['In-degree'], '-loc':[2], '-axisfsize':['large'], '-j':[1], '-ylim':[50]}
    totdegarg = {'func':['-td'], 'files':['simdata/svcsimn_d2a1_1.json'], '-m':['red'], '-yl':['Total degree (number of links) in the network'], '-l':['Total degree'], '-axisfsize':['large'], '-loc':[1], '-ylim':[4500]}

    ax = p.plt.axes([0.13, 0.15, 0.6, 0.75])
    logx, logy = getlogparam(indegarg)

    p.plotdata(loadarg([indegarg])
        , getargval(indegarg, '-l')
        , getargval(indegarg, '-t')[0]
        , {'x': getargval(indegarg, '-xl', ['Time'])[0], 'y': getargval(indegarg, '-yl', ['Degree'])[0]}
        , getargval(indegarg, '-m', ['var'])[0]
        , isbase=False
        , logx=logx
        , logy=logy
        , xlim=getargval(indegarg, '-xlim')
        , ylim=getargval(indegarg, '-ylim')
        , legloc=int(getargval(indegarg, '-loc', ['1'])[0])
        , ncol=int(getargval(indegarg, '-ncol', ['1'])[0])
        , numpoints=int(getargval(indegarg, '-numpoints', ['1'])[0])
        , axisfsize=getaxisfsize(indegarg)
        , ax=ax)

    ax.set_ylabel(ax.get_ylabel(), color='black')
    for tl in ax.get_yticklabels():
        tl.set_color('black')

    ax2 = p.plt.twinx(ax)
    logx, logy = getlogparam(totdegarg)

    p.plotdata(loadarg([totdegarg ])
        , getargval(totdegarg, '-l')
        , ''
        , {'x': getargval(totdegarg, '-xl', ['Time'])[0], 'y': getargval(totdegarg, '-yl', ['Degree'])[0]}
        , getargval(totdegarg, '-m', ['var'])[0]
        , isbase=False
        , logx=logx
        , logy=logy
        , xlim=getargval(totdegarg, '-xlim')
        , ylim=getargval(totdegarg, '-ylim')
        , legloc=int(getargval(totdegarg, '-loc', ['1'])[0])
        , ncol=int(getargval(totdegarg, '-ncol', ['1'])[0])
        , numpoints=int(getargval(totdegarg, '-numpoints', ['1'])[0])
        , axisfsize=getaxisfsize(totdegarg)
        , ax=ax2)


    ax2.set_ylabel(ax2.get_ylabel(), color='red')
    for tl in ax2.get_yticklabels():
        tl.set_color('red')

    p.processplot(p.plt, getargval(totdegarg, '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


import sys
import json
import plot as p

def getargval(dictarg, key, ifnone=p.IFNONE):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def main(argv):
    lsarg = []
    lsarg.append({'func':['-fc'], 'files':['simdata/pwsvcsim_avg1_16.json'], '-m':['diamond'], '-j':[500], '-l':['ProgrammableWeb'], '-axisfsize':['large']})
    lsarg.append({'func':['-fc'], 'files':['simdata/lgsvcsim_avg1_16.json'], '-m':['star'], '-j':[10], '-t':['Cascading failure on real networks'], '-xl':['Random failed services $n_r$ (in fraction)'], '-yl':['Cascade failed services $n_c$ (in fraction)'], '-l':['The Language Grid'], '-loc':[2], '-axisfsize':['large']})

    for i in range(len(lsarg)):
        ds = []
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

        logx = False
        arglogx = getargval(lsarg[i], '-logx')
        if arglogx:
            logx = int(arglogx[0]) > 0

        logy = False
        arglogy = getargval(lsarg[i], '-logy')
        if arglogy:
            logy = int(arglogy[0]) > 0

        lb = p.LOGBINBASE
        arglb = getargval(lsarg[i], '-lb')
        if arglb:
            lb = float(arglb[0])

        xlim = getargval(lsarg[i], '-xlim')
        ylim = getargval(lsarg[i], '-ylim')

        plotfile = getargval(lsarg[i], '-v', [None])[0]

        axisfsize = getargval(lsarg[i], '-axisfsize', ['medium'])[0]
        try:
            axisfsize = int(axisfsize)
        except:
            pass

        ax = p.plt.gca()

        if func in [p.FUNC_FAIL, p.FUNC_FAILCASC]:
            p.plotfailnodes(ds
                , getargval(lsarg[i], '-l')
                , getargval(lsarg[i], '-m', ['var'])[0]
                , isbase=func==p.FUNC_FAIL
                , xylabels={'x': getargval(lsarg[i], '-xl', [''])[0], 'y': getargval(lsarg[i], '-yl', [''])[0]}
                , title=getargval(lsarg[i], '-t', [''])[0]
                , legloc=int(getargval(lsarg[i], '-loc', [2])[0])
                , xlim=xlim
                , ylim=ylim
                , axisfsize=axisfsize
                , ax=ax)

            # process legend independently
            #legend = p.plt.legend([ax.get_lines()[0]], loc=int(getargval(lsarg[i], '-loc', [2])[0]))
            # add the legend to te axes
            #ax.add_artist(legend)

    p.processplot(p.plt, getargval(lsarg[i], '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


#python scratch/plot.py -di simdata/lg_comp.json -m black -logx 1 -logy 1 -t 'In-degree distribution of the Language Grid service network' -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$'
#python scratch/plot.py -li simdata/pwsvcsim_1.json -m black -logx 1 -logy 1 -t 'In-degree distribution of ProgrammableWeb APIs' -xl 'In-degree $k_{in}$' -yl 'Probability distribution $P(k_{in})$' -lb 1.21

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
    lsarg.append({'func':['-li'], 'files':['simdata/pwsvcsim_1.json'], '-m':['plus'], '-l':['ProgrammableWeb'], '-axisfsize':['large'], '-lb':[1.21]})
    lsarg.append({'func':['-di'], 'files':['simdata/lg_comp.json'], '-m':['star'], '-t':['In-degree distribution of the service network'], '-xl':['Random failed services $n_r$ (in fraction)'], '-yl':['Cascade failed services $n_c$ (in fraction)'], '-l':['The Language Grid'], '-loc':[1], '-axisfsize':['large']})

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

        if func == p.FUNC_LOGINDEG:
            p.drawloglogdist(ds
                , xlabel=getargval(lsarg[i], '-xl', [''])[0]
                , ylabel=getargval(lsarg[i], '-yl', [''])[0]
                , title=getargval(lsarg[i], '-t', [''])[0]
                , labels=getargval(lsarg[i], '-l')
                , markset=getargval(lsarg[i], '-m', ['var'])[0]
                , xlim=xlim
                , ylim=ylim
                , axisfsize=axisfsize
                , logbinbase=lb
                , showexp=int(getargval(lsarg[i], '-g', [1])[0]))

        elif func == p.FUNC_DISTINDEG:
            title = getargval(lsarg[i], '-t', ['Degree distribution of exponential network'])[0]
            xylabels = {'x':getargval(lsarg[i], '-xl', ['k (degree)'])[0], 'y':getargval(lsarg[i], '-yl', ['P(k)'])[0]}

            p.plotdegdist(ds
                , getargval(lsarg[i], '-l')
                , getargval(lsarg[i], '-m', ['var'])[0]
                , title=getargval(lsarg[i], '-t', [''])[0]
                , xylabels={'x': getargval(lsarg[i], '-xl', [''])[0], 'y': getargval(lsarg[i], '-yl', [''])[0]}
                , nbins=int(getargval(lsarg[i], '-b', ['50'])[0])
                , logx=logx, logy=logy
                , xlim=xlim
                , ylim=ylim
                , axisfsize=axisfsize
                , ax=p.plt.twinx(p.plt.gca()))
                #, ax=p.plt.gca())

    p.processplot(p.plt, getargval(lsarg[i], '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


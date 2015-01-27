#python scratch/plot.py -pl simdata/plotfunceff_tri_a1_a9.json -m trifive- -t 'The effect of $\langle alt \rangle$ on cascading failure in service networks' -xl 'Degree of alternative $\langle alt \rangle$' -yl 'Cascade failed services $n_c$ (in fraction)' -l scale-free exponential random -axisfsize large -ncol 3

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

    lsarg.append({'func':['-pl'], 'files':['simdata/plotfunceff_tri-sf_a1_a9.json'], '-m':['reddia-'], '-l':['scale-free']}) 
    lsarg.append({'func':['-pl'], 'files':['simdata/plotfunceff_tri-exp_a1_a9.json'], '-m':['bluepenta-'], '-l':['exponential']})
    lsarg.append({'func':['-pl'], 'files':['simdata/plotfunceff_tri-rand_a1_a9.json'], '-m':['trihexaorg-'], '-l':['random'], '-t':['The effect of $\langle alt \\rangle$ on cascading failure in service networks'], '-xl':['Degree of dependency $\langle alt \\rangle$'], '-yl':['Cascade failed services $n_c$ (in fraction)'], '-axisfsize':['large'], '-ncol':[3]})

    for i in range(len(lsarg)):
        ds = []
        func = lsarg[i]['func'][0]

        step = p.STEP
        argstep = getargval(lsarg[i], '-j')
        if argstep:
            step = int(argstep[0])

        with open(lsarg[i]['files'][0]) as f:
            ds = json.load(f)

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

        ncol = int(getargval(lsarg[i], '-ncol', [1])[0])
        numpoints = int(getargval(lsarg[i], '-numpoints', [1])[0])

        p.plotdata(ds
            , getargval(lsarg[i], '-l')
            , getargval(lsarg[i], '-t', [''])[0]
            , {'x': getargval(lsarg[i], '-xl', [''])[0], 'y': getargval(lsarg[i], '-yl', [''])[0]}
            , getargval(lsarg[i], '-m', ['var'])[0]
            , isbase=False
            , logx=logx
            , logy=logy
            , xlim=xlim
            , ylim=ylim
            , legloc=int(getargval(lsarg[i], '-loc', ['1'])[0])
            , ncol=int(getargval(lsarg[i], '-ncol', ['1'])[0])
            , numpoints=int(getargval(lsarg[i], '-numpoints', ['1'])[0])
            , axisfsize=axisfsize
            , ax=p.plt.gca())

    p.processplot(p.plt, getargval(lsarg[i], '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))



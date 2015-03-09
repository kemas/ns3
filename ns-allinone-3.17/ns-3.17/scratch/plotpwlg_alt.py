#python scratch/plot.py -fc \
#    simdata/pwsvcsim_avg1_16.json \
#    simdata/pwsvcsim_a2_avg1_16.json \
#    simdata/pwsvcsim_a3_avg1_16.json \
#-xl 'Random failed services $r$ (in fraction)' \
#-yl 'Cascade failed services $n_c$ (in fraction)' \
#-t 'Cascading failure with different $\langle{alt}\rangle$ on real networks' \
#-m green -j 500
#
#python scratch/plot.py -fc \
#    simdata/lgsvcsim_avg1_16.json \
#    simdata/lgsvcsim_a2_avg1_16.json \
#    simdata/lgsvcsim_a3_avg1_16.json \
#-m magenta -j 10

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
    lsarg.append({'func':['-fc'], 'files':['simdata/pwsvcsim_avg1_16.json', 'simdata/pwsvcsim_a2_avg1_16.json', 'simdata/pwsvcsim_a3_avg1_16.json'], '-m':['green'], '-j':[500]})
    lsarg.append({'func':['-fc'], 'files':['simdata/lgsvcsim_avg1_16.json', 'simdata/lgsvcsim_a2_avg1_16.json', 'simdata/lgsvcsim_a3_avg1_16.json'], '-m':['cyan'], '-j':[10], '-t':['Cascading failure with different $\langle{alt}\\rangle$ on real networks'], '-xl':['Random failed services $n_r$ (in fraction)'], '-yl':['Cascade failed services $n_c$ (in fraction)']})

    fig = p.plt.figure()

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

        if func in [p.FUNC_LOGINDEG, p.FUNC_HISTINDEG]:
            xlabel = 'In-degree'
        elif func in [p.FUNC_LOGOUTDEG, p.FUNC_HISTOUTDEG]:
            xlabel = 'Out-degree'

        axisfsize = getargval(lsarg[i], '-axisfsize', ['medium'])[0]
        try:
            axisfsize = int(axisfsize)
        except:
            pass

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
                , fig=fig)

    p.processplot(p.plt, getargval(lsarg[i], '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


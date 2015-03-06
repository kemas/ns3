import sys
import json
import plot as p

def getargval(dictarg, key, ifnone=p.IFNONE):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def main(argv):
    oax = p.plt.gca()
    oax2 = p.plt.twinx(oax)

    lsarg = []
    lsarg.append({'func':['-fc'], 'files':['simdata/svcsimn_10k_10k_d2_a2_i10_avg1_8.json', 'simdata/expsvcsimn_10k_10k_d2_a2_i10_avg1_8.json', 'simdata/randsvcsimn_10k_10k_d2_a2_i10_avg1_8.json', 'simdata/svcsimn_10k_10k_d2_a3_i10_avg1_8.json', 'simdata/expsvcsimn_10k_10k_d2_a3_i10_avg1_8.json', 'simdata/randsvcsimn_10k_10k_d2_a3_i10_avg1_8.json', 'simdata/svcsimn_10k_10k_d2_a4_i10_avg1_8.json', 'simdata/expsvcsimn_10k_10k_d2_a4_i10_avg1_8.json', 'simdata/randsvcsimn_10k_10k_d2_a4_i10_avg1_8.json'], '-m':['tricol'], '-j':[500], '-l':['sf, $\langle{alt}\\rangle = 0$', 'exp, $\langle{alt}\\rangle = 0$', 'rand, $\langle{alt}\\rangle = 0$', 'sf, $\langle{alt}\\rangle \\approx 0.5$', 'exp, $\langle{alt}\\rangle \\approx 0.5$', 'rand, $\langle{alt}\\rangle \\approx 0.5$', 'sf, $\langle{alt}\\rangle \\approx 1$', 'exp, $\langle{alt}\\rangle \\approx 1$', 'rand, $\langle{alt}\\rangle \\approx 1$'], '-axisfsize':['large'], '-ncol':[3], '-ax':[oax], '-ylim':[-0.02, 0.25], '-t':['Cascading failure with different $\langle{alt}\\rangle$ in service networks'], '-xl':['Random failed services $n_r$ (in fraction)'], '-yl':['Cascade failed services $n_c$ (in fraction)']})
    lsarg.append({'func':['-fc'], 'files':['simdata/pwsvcsim_avg1_16.json'], '-m':['diamond'], '-j':[500], '-l':['ProgrammableWeb'], '-axisfsize':['large'], '-ax':[oax2]})
    lsarg.append({'func':['-fc'], 'files':['simdata/lgsvcsim_avg1_16.json'], '-m':['star'], '-j':[10], '-l':['The Language Grid'], '-axisfsize':['large'], '-ncol':[3], '-ax':[oax2], '-ylim':[-0.02, 0.25], '-loc':[4]})

    for i in range(len(lsarg)):
        ds = []
        func = lsarg[i]['func'][0]

        ax = getargval(lsarg[i], '-ax')[0]

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

        ncol = int(getargval(lsarg[i], '-ncol', [1])[0])

        legmode = getargval(lsarg[i], '-lm', ['normal'])[0]
        bbox_to_anchor = getargval(lsarg[i], '-lbb', None)

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
                , ax=ax
                , ncol=ncol
                , legmode=legmode
                , bbox_to_anchor=bbox_to_anchor)

    oax2.get_yaxis().set_visible(False)
    #oax.get_yaxis().set_ticks()

    p.processplot(p.plt, getargval(lsarg[i], '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


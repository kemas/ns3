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


    #lsarg.append({'func':['-di'], 'files':['simdata/rsvcsim_10k_10k_d3_a5_i10_1d.json'], '-m':['triblue'], '-logx':[1], '-logy':[1], '-xlim':[1, 500], '-ylim':[1e-6, 1], '-t':['Exponential'], '-xl':['In-degree $k_{in}$'], '-yl':['Probability distribution $P(k_{in})$'], '-axisfsize':['large'], '-b':['100']})
    lsarg.append({'func':['-di'], 'files':['simdata/expsvcsimn_10k_10k_d2_a7_i10_avg1_8.json'], '-m':['triblue'], '-b':['100']})
    #lsarg.append({'func':['-di'], 'files':['simdata/randsvcsim_10k_10k_d3_a5_i10_1d.json'], '-m':['triorange'], '-logx':[1], '-logy':[1], '-xlim':[1, 500], '-ylim':[1e-6, 1], '-t':['Random'], '-xl':['In-degree $k_{in}$'], '-yl':['Probability distribution $P(k_{in})$'], '-axisfsize':['large'], '-b':['100']})
    lsarg.append({'func':['-di'], 'files':['simdata/randsvcsimn_10k_10k_d2_a11_i10_avg1_8.json'], '-m':['triorange'], '-b':['100']})
    #lsarg.append({'func':['-li'], 'files':['simdata/svcsim_10k_10k_d3_a3_i10_5.json'], '-m':['trired'], '-logx':[1], '-logy':[1], '-xlim':[1, 500], '-ylim':[1e-6, 1], '-t':['Scale-free, exponential, and random network degree distribution'], '-xl':['In-degree $k_{in}$'], '-yl':['Probability distribution $P(k_{in})$'], '-axisfsize':['large'], '-lb':['1.21'], '-g':[0]})
    lsarg.append({'func':['-li'], 'files':['simdata/svcsimn_10k_10k_d2_a7_i10_avg1_8.json'], '-m':['trired'], '-logx':[1], '-logy':[1], '-xlim':[1, 500], '-ylim':[1e-6, 1], '-t':['Scale-free, exponential, and random network degree distribution'], '-xl':['In-degree $k_{in}$'], '-yl':['Probability distribution $P(k_{in})$'], '-axisfsize':['large'], '-lb':['1.21'], '-g':[0]}) # gamma 2.22

    fig = p.plt.figure()

    for i in range(len(lsarg)):
        ds = []
        func = lsarg[i]['func'][0]

        step = p.STEP
        argstep = getargval(lsarg[i], '-j')
        if argstep:
            step = int(argstep[0])

        f = open(lsarg[i]['files'][0])
        try:
            data = json.load(f)

            p.loaddata(ds, func, data, lsarg[i]['files'][0], step)
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

        if func in [p.FUNC_LOGINDEG, p.FUNC_LOGOUTDEG]:
            # loglog degree distribution
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

        elif func in [p.FUNC_DISTINDEG, p.FUNC_DISTOUTDEG]:
            # degree distribution plot

            if p.FUNC_DISTINDEG:
                title = getargval(lsarg[i], '-t', ['Degree distribution of exponential network'])[0]
                xylabels = {'x':getargval(lsarg[i], '-xl', ['k (degree)'])[0], 'y':getargval(lsarg[i], '-yl', ['P(k)'])[0]}
            else:
                title = getargval(lsarg[i], '-t', ['Outdegree distribution'])[0]
                xylabels = {'x':getargval(lsarg[i], '-xl', ['Outdegree'])[0], 'y':getargval(lsarg[i], '-yl', ['Number of nodes'])[0]}

            p.plotdegdist(ds
                , getargval(lsarg[i], '-l')
                , getargval(lsarg[i], '-m', ['var'])[0]
                , title=title
                , xylabels=xylabels
                , nbins=int(getargval(lsarg[i], '-b', ['50'])[0])
                , logx=logx, logy=logy
                , xlim=xlim
                , ylim=ylim
                , axisfsize=axisfsize
                , fig=fig)

    p.processplot(p.plt, getargval(lsarg[i], '-s', [None])[0])

if __name__ == '__main__':
    sys.exit(main(sys.argv))


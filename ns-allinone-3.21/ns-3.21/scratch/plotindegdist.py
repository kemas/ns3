#python scratch/plot.py -li simdata/svcsimn_d2a1_6.json simdata/svcsimn_d3a1_2.json simdata/svcsimn_d4a1_2.json -l '$\langle{dep}\rangle = 1$' '$\langle{dep}\rangle \approx 1.5$' '$\langle{dep}\rangle \approx 2$' -m var -t 'In-degree distribution of some generated scale-free service networks' -xl 'In-degree $k_{in}$' -yl '$P(k_{in})$'
#python scratch/plot.py -di simdata/expsvcsimn_d2a1_5.json simdata/expsvcsimn_d3a1_2.json simdata/expsvcsimn_d4a1_3.json -l '$\langle{dep}\rangle = 1, \langle{alt}\rangle = 0$' '$\langle{dep}\rangle \approx 1.5, \langle{alt}\rangle = 0$' '$\langle{dep}\rangle \approx 2, \langle{alt}\rangle = 0$' -m var -t 'In-degree distribution of some generated exponential service networks' -xl 'In-degree $k_{in}$' -yl '$P(k_{in})$' -logy 1
#python scratch/plot.py -di simdata/randsvcsimn_d2a1_5.json simdata/randsvcsimn_d3a1_2.json simdata/randsvcsimn_d4a1_3.json -l '$\langle{dep}\rangle = 1, \langle{alt}\rangle = 0$' '$\langle{dep}\rangle \approx 1.5, \langle{alt}\rangle = 0$' '$\langle{dep}\rangle \approx 2, \langle{alt}\rangle = 0$' -m var -t 'In-degree distribution of some generated random service networks' -xl 'In-degree $k_{in}$' -yl '$P(k_{in})$'

import sys
import plot as p
import plotlib as pl

def main(argv):
    argsf = {'func':['-li'], 'files':['simdata/svcsimn_d2a1_6.json', 'simdata/svcsimn_d3a1_2.json', 'simdata/svcsimn_d4a1_2.json'], '-m':['red'], '-yl':['$P(k_{in})$'], '-axisfsize':['large'], '-lb':[1.21], '-gl':[0], '-l':['1', '2', '3'], '-loc':[1]}
    argexp = {'func':['-di'], 'files':['simdata/expsvcsimn_d2a1_5.json', 'simdata/expsvcsimn_d3a1_2.json', 'simdata/expsvcsimn_d4a1_3.json'], '-m':['blue'], '-xl':['In-degree $k_{in}$'], '-axisfsize':['large'], '-logy':[1]}
    argrand = {'func':['-di'], 'files':['simdata/randsvcsimn_d2a1_5.json', 'simdata/randsvcsimn_d3a1_2.json', 'simdata/randsvcsimn_d4a1_3.json'], '-m':['yellow'], '-axisfsize':['large']}
    #'-t':['In-degree distribution of service networks'], 

    p.plt.subplot(131)
    #ax = p.plt.axes([0.13, 0.15, 0.6, 0.75])

    p.drawloglogdist(pl.loadarg([argsf])
        , xlabel=pl.getargval(argsf, '-xl', [''])[0]
        , ylabel=pl.getargval(argsf, '-yl', [''])[0]
        , title=pl.getargval(argsf, '-t', [''])[0]
        , labels=pl.getargval(argsf, '-l')
        , markset=pl.getargval(argsf, '-m', ['var'])[0]
        , xlim=pl.getargval(argsf, '-xlim')
        , ylim=pl.getargval(argsf, '-ylim')
        , axisfsize=pl.getaxisfsize(argsf)
        , logbinbase=pl.getargval(argsf, '-lb', [1.21])[0]
        , showexp=int(pl.getargval(argsf, '-g', [1])[0])
        , legloc=int(pl.getargval(argsf, '-loc', [1])[0])
        , isexpline=int(pl.getargval(argsf, '-gl', [1])[0]))

    p.plt.subplot(132)
    logx, logy = pl.getlogparam(argexp)

    p.plotdegdist(pl.loadarg([argexp])
        , pl.getargval(argexp, '-l')
        , pl.getargval(argexp, '-m', ['var'])[0]
        , title=pl.getargval(argexp, '-t', [''])[0]
        , xylabels={'x': pl.getargval(argexp, '-xl', [''])[0], 'y': pl.getargval(argexp, '-yl', [''])[0]}
        , nbins=int(pl.getargval(argexp, '-b', ['50'])[0])
        , logx=logx, logy=logy
        , xlim=pl.getargval(argexp, '-xlim')
        , ylim=pl.getargval(argexp, '-ylim')
        , legloc=int(pl.getargval(argexp, '-loc', [2])[0])
        , axisfsize=pl.getaxisfsize(argexp))
#
#    p.plt.subplot(133)
#    logx, logy = pl.getlogparam(argrand)
#
#    p.plotdegdist(pl.loadarg([argrand])
#        , pl.getargval(argrand, '-l')
#        , pl.getargval(argrand, '-m', ['var'])[0]
#        , title=pl.getargval(argrand, '-t', [''])[0]
#        , xylabels={'x': pl.getargval(argrand, '-xl', [''])[0], 'y': pl.getargval(argrand, '-yl', [''])[0]}
#        , nbins=int(pl.getargval(argrand, '-b', ['50'])[0])
#        , logx=logx, logy=logy
#        , xlim=pl.getargval(argrand, '-xlim')
#        , ylim=pl.getargval(argrand, '-ylim')
#        , legloc=int(pl.getargval(argrand, '-loc', [2])[0])
#        , axisfsize=pl.getaxisfsize(argrand))

    p.plt.gcf().suptitle('In-degree distribution of scale-free (red), exponential (blue), and random (yellow) service networks', fontsize=14)
    p.processplot(p.plt)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


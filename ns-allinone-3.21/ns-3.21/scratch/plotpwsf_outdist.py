import sys
import json
import plot as p
import plotlib as pl 

def main(argv):
    sfarg = {'func':['-do'], 'files':['simdata/svcsimn_d4a1_1.json'], '-m':['red'], '-t':['Out-degree distribution of scale-free and ProgrammableWeb service networks'], '-xl':['Out-degree $k_{out}$'], '-yl':['Probability distribution $P(k_{out})$\nScale-free'], '-l':['Scale-free'], '-loc':[2], '-axisfsize':['large'], '-logy':[1], '-ylim':[0.1, 1.3]}
    pwarg = {'func':['-do'], 'files':['simdata/pwsvc_1.json'], '-m':['diamond'], '-yl':['ProgrammableWeb'], '-l':['ProgrammableWeb'], '-axisfsize':['large'], '-loc':[1], '-logy':[1], '-ylim':[1e-05, 4]}

    ax = p.plt.axes([0.13, 0.12, 0.6, 0.78])
    logx, logy = pl.getlogparam(sfarg)

    p.plotdegdist(pl.loadarg([sfarg])
        , pl.getargval(sfarg, '-l')
        , pl.getargval(sfarg, '-m', ['var'])[0]
        , title=pl.getargval(sfarg, '-t', [''])[0]
        , xylabels={'x': pl.getargval(sfarg, '-xl', [''])[0], 'y': pl.getargval(sfarg, '-yl', [''])[0]}
        , nbins=int(pl.getargval(sfarg, '-b', ['50'])[0])
        , logx=logx, logy=logy
        , xlim=pl.getargval(sfarg, '-xlim')
        , ylim=pl.getargval(sfarg, '-ylim')
        , legloc=int(pl.getargval(sfarg, '-loc', [2])[0])
        , axisfsize=pl.getaxisfsize(sfarg)
        , ax=ax)

    ax.set_ylabel(ax.get_ylabel(), color='red')
    for tl in ax.get_yticklabels():
        tl.set_color('red')

    ax2 = p.plt.twinx(ax)
    logx, logy = pl.getlogparam(pwarg)

    p.plotdegdist(pl.loadarg([pwarg])
        , pl.getargval(pwarg, '-l')
        , pl.getargval(pwarg, '-m', ['var'])[0]
        , title=pl.getargval(pwarg, '-t', [''])[0]
        , xylabels={'x': pl.getargval(pwarg, '-xl', [''])[0], 'y': pl.getargval(pwarg, '-yl', [''])[0]}
        , nbins=int(pl.getargval(pwarg, '-b', ['50'])[0])
        , logx=logx, logy=logy
        , xlim=pl.getargval(pwarg, '-xlim')
        , ylim=pl.getargval(pwarg, '-ylim')
        , legloc=int(pl.getargval(pwarg, '-loc', [2])[0])
        , axisfsize=pl.getaxisfsize(pwarg)
        , ax=ax2)

    ax2.set_ylabel(ax2.get_ylabel(), color='#003200')
    for tl in ax2.get_yticklabels():
        tl.set_color('#003200')

    p.processplot(p.plt)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


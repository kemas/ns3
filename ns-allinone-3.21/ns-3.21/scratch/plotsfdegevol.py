import sys
import plot as p
import plotlib as pl

def main(argv):
    indegarg = {'func':['-id'], 'files':['simdata/svcsimn_d2a1_1.json'], '-m':['plus'], '-t':['In-degree of random failed services and total degree of the network during network failure'], '-xl':['Timestep'], '-yl':['In-degree of random failed services'], '-l':['In-degree'], '-loc':[2], '-axisfsize':['large'], '-j':[1], '-ylim':[50]}
    totdegarg = {'func':['-td'], 'files':['simdata/svcsimn_d2a1_1.json'], '-m':['red'], '-yl':['Total degree (number of links) in the network'], '-l':['Total degree'], '-axisfsize':['large'], '-loc':[1], '-ylim':[4500]}

    ax = p.plt.axes([0.13, 0.15, 0.6, 0.75])
    logx, logy = pl.getlogparam(indegarg)

    p.plotdata(pl.loadarg([indegarg])
        , pl.getargval(indegarg, '-l')
        , pl.getargval(indegarg, '-t')[0]
        , {'x': pl.getargval(indegarg, '-xl', ['Time'])[0], 'y': pl.getargval(indegarg, '-yl', ['Degree'])[0]}
        , pl.getargval(indegarg, '-m', ['var'])[0]
        , isbase=False
        , logx=logx
        , logy=logy
        , xlim=pl.getargval(indegarg, '-xlim')
        , ylim=pl.getargval(indegarg, '-ylim')
        , legloc=int(pl.getargval(indegarg, '-loc', ['1'])[0])
        , ncol=int(pl.getargval(indegarg, '-ncol', ['1'])[0])
        , numpoints=int(pl.getargval(indegarg, '-numpoints', ['1'])[0])
        , axisfsize=pl.getaxisfsize(indegarg)
        , ax=ax)

    ax.set_ylabel(ax.get_ylabel(), color='black')
    for tl in ax.get_yticklabels():
        tl.set_color('black')

    ax2 = p.plt.twinx(ax)
    logx, logy = pl.getlogparam(totdegarg)

    p.plotdata(pl.loadarg([totdegarg ])
        , pl.getargval(totdegarg, '-l')
        , ''
        , {'x': pl.getargval(totdegarg, '-xl', ['Time'])[0], 'y': pl.getargval(totdegarg, '-yl', ['Degree'])[0]}
        , pl.getargval(totdegarg, '-m', ['var'])[0]
        , isbase=False
        , logx=logx
        , logy=logy
        , xlim=pl.getargval(totdegarg, '-xlim')
        , ylim=pl.getargval(totdegarg, '-ylim')
        , legloc=int(pl.getargval(totdegarg, '-loc', ['1'])[0])
        , ncol=int(pl.getargval(totdegarg, '-ncol', ['1'])[0])
        , numpoints=int(pl.getargval(totdegarg, '-numpoints', ['1'])[0])
        , axisfsize=pl.getaxisfsize(totdegarg)
        , ax=ax2)

    ax2.set_ylabel(ax2.get_ylabel(), color='red')
    for tl in ax2.get_yticklabels():
        tl.set_color('red')

    p.processplot(p.plt)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


#python scratch/plot.py -id simdata/svcsimn_d4a1_4.json -m plus -t 'In-degree of each random failed service during cascading failure simulation' -xl Timestep -yl 'In-degree' -axisfsize large -j 1
#python scratch/plot.py -ad simdata/svcsimn_d4a1_4.json -m plus -t 'Average in-degree of the available services during cascading failure simulation' -xl Timestep -yl 'Average in-degree' -axisfsize large -j 150    

import sys
import plot as p
import plotlib as pl

def main(argv):
    argid = {'func':['-id'], 'files':['simdata/svcsimn_d4a1_4.json'], '-m':['plus'], '-yl':['In-degree'], '-axisfsize':['large'], '-j':[1]}
    argavgid = {'func':['-ad'], 'files':['simdata/svcsimn_d4a1_4.json'], '-m':['plus'], '-xl':['Timestep'], '-yl':['Average in-degree'], '-axisfsize':['large'], '-j':[150]}

    #ax = p.plt.axes([0.13, 0.15, 0.6, 0.75])
    p.plt.subplot(211)

    p.plotdata(pl.loadarg([argid])
        , xylabels={'x': pl.getargval(argid, '-xl', [''])[0], 'y': pl.getargval(argid, '-yl', [''])[0]}
        , markset=pl.getargval(argid, '-m', ['var'])[0]
        , isbase=False
        , xlim=pl.getargval(argid, '-xlim')
        , ylim=pl.getargval(argid, '-ylim')
        , legloc=int(pl.getargval(argid, '-loc', ['1'])[0])
        , ncol=int(pl.getargval(argid, '-ncol', ['1'])[0])
        , numpoints=int(pl.getargval(argid, '-numpoints', ['1'])[0])
        , axisfsize=pl.getaxisfsize(argid))

    p.plt.subplot(212)

    p.plotdata(pl.loadarg([argavgid])
        , xylabels={'x': pl.getargval(argavgid, '-xl', [''])[0], 'y': pl.getargval(argavgid, '-yl', [''])[0]}
        , markset=pl.getargval(argavgid, '-m', ['var'])[0]
        , isbase=False
        , xlim=pl.getargval(argavgid, '-xlim')
        , ylim=pl.getargval(argavgid, '-ylim')
        , legloc=int(pl.getargval(argavgid, '-loc', ['1'])[0])
        , ncol=int(pl.getargval(argavgid, '-ncol', ['1'])[0])
        , numpoints=int(pl.getargval(argavgid, '-numpoints', ['1'])[0])
        , axisfsize=pl.getaxisfsize(argavgid))

    p.plt.gcf().suptitle('In-degree of each random failed service (top) and the average in-degree\n of the available services (bottom) during cascading failure simulation', fontsize=14)
    p.processplot(p.plt)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


import matplotlib.pyplot as plt

def plotdata(x, y
    , mark='bo'
    , label=''
    , title=''
    , xylabels={'x':'','y':''}
    , xlim=None
    , ylim=None
    , legloc=2
    , logx=False
    , logy=False
    , filename=None):

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.6, 0.8])

    ax.plot(x, y, mark, label=label)
    #ax.plot(xy[0], xy[1], label=labels[i], color='black', linestyle=linestyle, marker=marker, markerfacecolor=markerfacecolor)

    ax.set_title(title)
    ax.set_xlabel(xylabels['x'])
    ax.set_ylabel(xylabels['y'])
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    #ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #ax.legend(bbox_to_anchor=(0, 1), ncol=2, loc=2, borderaxespad=0.)
    ax.legend(ncol=2, loc=legloc, borderaxespad=0.)

    if logx and logy:
        ax.loglog()
    elif logx:
        ax.semilogx()
    elif logy:
        ax.semilogy()

    if filename:
        plt.savefig(filename)
    else:
        plt.show()

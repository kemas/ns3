import numpy as np
import matplotlib.pyplot as plt
import json

GAMMA = u'\u03b3'
LOGBINBASE = 1.2

def savetofile(obj, filename):
    f = open(filename or 'basim.json', 'w')
    try:
        json.dump(obj, f)
    finally:
        f.close()

def drawhistogram(vertices, nbins=20, filename=None, normed=False, facecolor='green', alpha=0.5, histtype='bar', log=False):
    # the histogram of the degree distribution

    degrees = [vertices.getvertex(i).getdegree() for i in range(vertices.getlength())]
    n, bins, patches = plt.hist(degrees, bins=nbins, normed=normed, facecolor=facecolor, alpha=alpha, histtype=histtype, log=log)
    plt.title('Degree distribution')
    plt.xlabel('Degree')
    plt.ylabel('Number of nodes')
    plt.show()

    # save to file
    savetofile({'indegree': degrees, 'maxindegree': max(degrees)}, filename)

def logbins(amax, amin=0, base=LOGBINBASE):
    bins = [amin]
    num = amin + 1
    i = 1

    while num <= amax:
        bins.append(num)
        num += base**i
        i += 1

    bins.append(amax)
 
    return bins

def drawloglogdist(vertices, lbinsbase=LOGBINBASE, density=False, filename=None):
    # the degree distribution in loglog scale

    lbins = logbins(vertices.maxdegree, amin=0, base=lbinsbase)

    degrees = [vertices.getvertex(i).getdegree() for i in range(vertices.getlength())]
    #y, bins = np.histogram(degrees, bins=nbins, density=density)
    y, bins = np.histogram(degrees, bins=lbins, density=density)
    x = bins[:-1]

    xforlog = []; logx = []; logy = []
    for i in range(len(y)):
        if x[i] and y[i]:
            xforlog.append(x[i])
            logx.append(np.log10(x[i]))
            logy.append(np.log10(y[i]))
           
    gamma, logA = np.polyfit(logx, logy, 1)
    p = np.poly1d([gamma, logA])
    plt.plot(x, y, 'bo', xforlog, 10**p(logx), 'r-')
    plt.loglog()
    plt.title(u'Degree distribution (%s = %#.2f)' % (GAMMA, -1 * gamma))
    plt.show()

    # save to file
    savetofile({'indegree': degrees}, filename)


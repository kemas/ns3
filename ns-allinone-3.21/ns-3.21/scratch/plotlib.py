import json
import plot as p

def getargval(dictarg, key, ifnone=p.IFNONE):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def getaxisfsize(dictarg):
    axisfsize = getargval(dictarg, '-axisfsize', ['medium'])[0]
    try:
        axisfsize = int(axisfsize)
    except:
        pass

    return axisfsize

def getlogparam(dictarg):
    logx = False
    arglogx = getargval(dictarg, '-logx')
    if arglogx:
        logx = int(arglogx[0]) > 0

    logy = False
    arglogy = getargval(dictarg, '-logy')
    if arglogy:
        logy = int(arglogy[0]) > 0

    return logx, logy

def loadarg(lsarg):
    ds = []
    for i in range(len(lsarg)):
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

        xlim = getargval(lsarg[i], '-xlim')
        ylim = getargval(lsarg[i], '-ylim')

        plotfile = getargval(lsarg[i], '-v', [None])[0]

        axisfsize = getargval(lsarg[i], '-axisfsize', ['medium'])[0]
        try:
            axisfsize = int(axisfsize)
        except:
            pass

    return ds


import sys
import json
import types

OPT_AVGFILE = '-a'
OPT_FILES = '-f'
OPT_FIELDS = '-c'
OPTS = (OPT_AVGFILE, OPT_FILES, OPT_FIELDS)
EXCLS = ['snapshot']

def rounddiv(n, d):
    if types.FloatType == type(n):
        n = int(n) 
    return (((n << 1) // d) + 1) >> 1

def average(avgfile, **kwargs):
    # **kwargs: *files, *fields
    # calculate the average of data in each field for all files
    # save it to a new file avgfile

    fileset = []
    for filename in kwargs['files']:
        f = open(filename)
        try:
            fileset.append(json.load(f))
        finally:
            f.close()
    lenfset = len(fileset)

    if kwargs['fields'][0] == '*':
        # all fields based on the first file
        fields = fileset[0].keys()
        # remove excluded fields
        for excl in EXCLS:
            if excl in fields:
                fields.pop(fields.index(excl))
    else:
        fields = kwargs['fields'] 

    # average the data
    avgds = {}
    for col in fields:
        firstds = fileset[0][col]

        if type(firstds) == types.ListType:
            collen = max(len(i[col]) for i in fileset)

            # add the first dataset of fileset to avgds dictionary
            #avgds[col] = firstds[:collen]
            lenfds = len(firstds)
            avgds[col] = firstds + [firstds[-1] for i in range(collen - lenfds)]
            #recavgds = [1 for i in range(lenfds)] + [0 for i in range(collen - lenfds)]
            #recavgds = [1 for i in range(collen)]

            for ds in fileset[1:]:
                currlen = len(ds[col])
                for i in range(currlen):
                    avgds[col][i] += ds[col][i]
                    #recavgds[i] += 1

                for i in range(collen - currlen):
                    avgds[col][-i - 1] += ds[col][-1]
                #avgds[col][i] += [ds[col][-1] for i in range(collen - currlen)]

            # calculate the average (divide by the number of records at each value)
            for i in range(collen):
                #avgds[col][i] = rounddiv(avgds[col][i], recavgds[i])
                avgds[col][i] = rounddiv(avgds[col][i], lenfset)

        else:
            # add the first dataset of fileset to avgds dictionary
            avgds[col] = firstds

            # types.IntegerType
            for ds in fileset[1:]:
                avgds[col] += ds[col]

            # calculate the average (divide by the length of fileset)
            avgds[col] = rounddiv(avgds[col], lenfset)

    # save avgds to avgfile
    fnew = open(avgfile, 'w')
    try:
        json.dump(avgds, fnew)
    finally:
        fnew.close()

def printusage():
    print "Usage: python simdata.py -a <avgfile> -f <file-1>[ <file-n>] -c <field-1>[ <file-m>]"
    print "Example: python simdata.py -a avgfile.json -f data1.json data2.json -c field1 field2"
    sys.exit()

def readargv(argv, pos=1, opt='', dictarg={}):
    if pos >= len(argv):
        return

    currarg = argv[pos]
    if pos == 1 or currarg[0] == '-':
        if currarg not in OPTS:
            printusage()

        readargv(argv, pos + 1, currarg, dictarg)

    else:
        if dictarg.has_key(opt):
            dictarg[opt].append(currarg)
        else:
            dictarg[opt] = [currarg]
        readargv(argv, pos + 1, opt, dictarg)

    return dictarg

def getargval(dictarg, key, ifnone=[]):
    try:
        return dictarg[key]
    except:
        printusage()

def main(argv):
    dictarg = readargv(argv)
    average(getargval(dictarg, '-a')[0], files=getargval(dictarg, '-f'), fields=getargval(dictarg, '-c'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))

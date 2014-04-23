import sys
import json
import types

OPT_AVGFILE = '-a'
OPT_FILES = '-f'
OPT_FIELDS = '-c'
OPTS = (OPT_AVGFILE, OPT_FILES, OPT_FIELDS)

def rounddiv(n, d):
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

    # average the data
    avgds = {}
    for col in kwargs['fields']:
        # add the first dataset of fileset to avgds dictionary
        avgds[col] = fileset[0][col]

        if type(avgds[col]) == types.ListType:
            collen = min(len(i[col]) for i in fileset)

            for ds in fileset[1:]:
                for i in range(collen):
                    avgds[col][i] += ds[col][i]

            # calculate the average (divide by the length of fileset)
            for i in range(collen):
                avgds[col][i] = rounddiv(avgds[col][i], len(fileset))

        else:
            # types.IntegerType
            for ds in fileset[1:]:
                avgds[col] += ds[col]

            # calculate the average (divide by the length of fileset)
            avgds[col] = rounddiv(avgds[col], len(fileset))

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

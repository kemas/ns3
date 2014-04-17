import sys
import json

OPT_AVGFILE = '-a'
OPT_FILES = '-f'
OPT_FIELDS = '-c'
OPTS = (OPT_AVGFILE, OPT_FILES, OPT_FIELDS)

def average(avgfile, **kwargs):
    # **kwargs: *files, *fields
    # calculate the average of data in each field from each file
    # save it to a new file

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

        # add the remaining data from fileset
        if len(fileset) > 1:
            collen = len(avgds[col])

            for ds in fileset[1:]:
                for i in range(collen):
                    avgds[col][i] += ds[col][i]

            # calculate the average (divide by the length of fileset)
            for i in range(collen):
                avgds[col][i] = round(avgds[col][i] / float(len(fileset)), 2)

    # save avgds to avgfile
    fnew = open(avgfile, 'w')
    try:
        json.dump(avgds, fnew)
    finally:
        fnew.close()

def printusage():
    print "Usage: python simdata.py -a <avgfile> -f <file-1>[ <file-n>] -c <field-1>[ <file-m>]"
    print "Example: python simdata.py -a avgfile.json -f data1.json data2.json -c field1 field2"

def readargv(argv, pos=1, opt='', dictarg={}):
    if pos >= len(argv):
        return

    currarg = argv[pos]
    if pos == 1 or currarg[0] == '-':
        if currarg not in OPTS:
            printusage()
            return

        readargv(argv, pos + 1, currarg, dictarg)

    else:
        if dictarg.has_key(opt):
            dictarg[opt].append(currarg)
        else:
            dictarg[opt] = [currarg]
        readargv(argv, pos + 1, opt, dictarg)

    return dictarg

def getargval(dictarg, key, ifnone=[]):
    if dictarg.has_key(key):
        return dictarg[key]
    else:
        return ifnone

def main(argv):
    dictarg = readargv(argv)
    average(getargval(dictarg, '-a')[0], getargval(dictarg, '-f'), getargval(dictarg, '-c'))

if __name__ == '__main__':
    sys.exit(main(sys.argv))

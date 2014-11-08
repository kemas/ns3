import sys
import json
import unicodecsv

IDX_IND = 0
IDX_OUTD = 1
IDX_MASHUPNAME = 2
IDX_MASHUPTYPE = 3
IDX_CHILDREN = 4

class MashupsJSON:
    def __init__(self, obj):
        self._ID_ATTRIBUTES = 1
        self._ID_TARGETS = 2
        self._ID_ENDPOINTS = 3
        self._ID_MASHUPURLS = 4

        self._obj = obj
        self._items = obj[1:]

    def get_items(self):
        return self._items

    def get_item(self, idx):
        return self._items[idx]

    def del_item(self, idx):
        return self._items.pop(idx)

    def get_vid(self, item):
        return item[self._ID_ATTRIBUTES]['vid']

    def get_title(self, item):
        return item[self._ID_ATTRIBUTES]['title']

    def is_mashup(self, item):
        return item[self._ID_ATTRIBUTES]['type'] == 'mashup'

    def get_lscompvid(self, item):
        # only when type == 'mashup' (!= 'api')

        ls = []
        for t in item[self._ID_TARGETS][1:]:
            ls.append(t[1])
        return ls

    def get_lsendpoint(self, item):
        ls = []
        for t in item[self._ID_ENDPOINTS][1:]:
            try:
                ls.append(t[1])
            except IndexError:
                # IndexError means the item has no endpoint info
                pass
        return ls

    def get_lsmashupurls(self, item):
        ls = []
        for t in item[self._ID_MASHUPURLS][1:]:
            try:
                ls.append(t[1])
            except IndexError:
                # IndexError means the item has no mashupurls info
                pass
        return ls

    def removeredapis(self):
        # "remove" redundant apis
        # actually sets the _items with unique list
        vids = []
        uniqitems = []

        for item in self._items:
            vid = self.get_vid(item)

            if vid not in vids:
                vids.append(vid)
                uniqitems.append(item)

        # set items
        self._items = uniqitems

        return vids

def load(filename):
    with open(filename) as f:
        obj = json.load(f)

    return obj

def calcdepth(dictdepth, vid, apis):
    # returns the depth of vid or 
    # calculate recursively through its children

    if dictdepth.has_key(vid):
        return dictdepth[vid]

    # else, depth for vid has not been calculated

    children = apis[vid][IDX_CHILDREN]
    viddepth = 0; vidmeandepth = 0

    if len(children):
        # vid has child
        maxdepth = 0; totmeandepth = 0.0
        for compvid in children:
            # calculate reccursively
            d, m =  calcdepth(dictdepth, compvid, apis)

            if d > maxdepth:
                maxdepth = d

            totmeandepth += m 

        viddepth = maxdepth
        vidmeandepth = totmeandepth / len(children)

    # add to depth
    dictdepth[vid] = [viddepth + 1, vidmeandepth + 1]

    return dictdepth[vid]

def converttodictapis(obj):
    # remove redundant in mashups obj and convert into apis format
    apis = {} # api and mashups {vid:[indegree, outdegree, name, mashuptype, [compvid, ...]], ...}

    mashups = MashupsJSON(obj)
    # clean from redundant apis
#    print 'len before cleaning %d' % len(mashups.get_items())
    reds = mashups.removeredapis()
#    print 'unique apis %d' % len(reds)
#    print 'len after cleaning %d' % len(mashups.get_items())

    items = mashups.get_items()

    for item in items:
        vid = mashups.get_vid(item)

        if not apis.has_key(vid):
            # vid not found, add to the dictionary
            apis[vid] = [0, 0, mashups.get_title(item), mashups.is_mashup(item), []]

        elif not apis[vid][IDX_MASHUPNAME]:
            # vid is in the dictionary but name/title is not defined
            apis[vid][IDX_MASHUPNAME] = mashups.get_title(item)
            # also the type
            apis[vid][IDX_MASHUPTYPE] = mashups.is_mashup(item)

        if mashups.is_mashup(item):
            # mashup components 
            lscomps = mashups.get_lscompvid(item)
            # increment the outdegree
            apis[vid][IDX_OUTD] += len(lscomps)

            for compvid in lscomps:
                if not apis.has_key(compvid):
                    # compvid not found, add to the dictionary
                    apis[compvid] = [0, 0, None, None, []]

                # increment the indegree
                apis[compvid][IDX_IND] += 1

                # add vid's child
                apis[vid][IDX_CHILDREN].append(compvid)

    return apis

def converttoplotfmt(apis):
    # convert apis format into plotting format

    maxdeg = 0; maxdegid = None
    mashupid = apis.keys()
    indegree = []
    outdegree = []
    mashupname = []
    mashuptype = []
    dictdepth = {} # vid: [depth, meandepth]
    maxdepth = 0; avgdepth = 0.0
    avgmeandepth = 0.0

    for key in mashupid:
        ind = apis[key][IDX_IND]

        if ind > maxdeg:
            maxdeg = ind
            maxdegid = key

        indegree.append(ind)
        outdegree.append(apis[key][IDX_OUTD])
        mashupname.append(apis[key][IDX_MASHUPNAME])
        mashuptype.append(apis[key][IDX_MASHUPTYPE])

        # calculate depth recursively to parents and children
        # or do nothing (only to return the values) if depth for current api (key) has been defined
        calcdepth(dictdepth, key, apis)

    depth = [d[0] for d in dictdepth.values()]
    meandepth = [d[1] for d in dictdepth.values()]

    # return the degrees as json readable format for pyplot, and max degree id
    return {'indegree': indegree
        , 'outdegree': outdegree
        , 'mashupid': mashupid
        , 'mashupname': mashupname
        , 'mashuptype': mashuptype # 1 = mashup, 0 = api
        , 'maxindegree': maxdeg
        , 'maxindegreeid': maxdegid
        , 'depth': depth
        , 'maxdepth': max(depth)
        , 'avgdepth': sum(depth) / float(len(depth))
        , 'meandepth': meandepth
        , 'avgmeandepth': sum(meandepth) / float(len(meandepth))}

def savetofile(ds, filename):
    with open(filename, 'w') as f:
        json.dump(ds, f)

#def gethubs(thold, indegrees):
#    ls = []; lsidx = []
#
#    i = 0
#    for deg in indegrees:
#        if deg >= thold:
#            ls.append(deg)
#            lsidx.append(i)
#        
#        i += 1
#
#    return ls, lsidx

def dstocsv(ds, filename):
    with open(filename, 'w') as f:
        csvwr = unicodecsv.UnicodeWriter(f)
        for i in range(len(ds['mashupid'])):
            row = [ds['mashupid'][i], ds['mashupname'][i] or '', str(ds['indegree'][i])]
            #print row
            csvwr.writerow(row)

def checkredundant(fsource, fred):
    # retrieve multiple entry apis in fsource and write it to fred

    with open(fsource) as fs:
        osource = json.load(fs)

    ored = []
    vids = []

    for api in osource[1:]:
        vid = api[1]['vid']

        if vid in vids:
            ored.append(api)
        else:
            vids.append(vid)

    if ored > 1:
        # ored != []
        with open(fred, 'w') as fr:
            json.dump(ored, fr)

def main(argv):
    option = argv[1]
    fin = argv[2]
    fout = argv[3]

    obj = load(fin)

    if option == '-p':
        # write json for plotting
        ds = converttoplotfmt(obj)
        savetofile(ds, fout)

    elif option == '-c':
        # write csv of apis and mashups 
        ds = converttoplotfmt(obj)
        fout = argv[3]
        dstocsv(ds, fout)

    elif option == '-a':
        # write json of following format for further processing
        # {id:[indegree, outdegree, name, mashuptype, [child, ...]], ...}
        ds = converttodictapis(obj)
        savetofile(ds, fout)

if __name__ == '__main__':
    sys.exit(main(sys.argv))


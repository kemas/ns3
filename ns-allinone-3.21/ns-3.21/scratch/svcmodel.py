# svcmodel.py
#--------------------------------------------------------
# This program models the generation of a service network.
# A service network is a directed graph where the nodes represent services and the directed links represent dependency between services
# A service p depends on service q if p requires q to perform its function
# Two kinds of dependency are defined: full and partial
# Service p is partially depends on service q if the functionality of q can be substituted by another service, e.g. service r
# In such case, service q and r are listed in altlinks of p

#import pdb

import sys
import random
import svc_nodes
import pwjsonloader as pwj
import ns.network
import ns.point_to_point

ALPHA   = 1 # default number of alpha >= 0, initial attractiveness for young nodes
COMP    = 0.4 # the probability/proportion of the number of composite services
M_INIT  = 3 # default initial number of nodes
M_ADD   = 1 # default number of nodes to be added in every timestep
M_DEP   = 3 # default upper limit number of links to be created from each added node
M_ALT   = 3 # default upper limit number of alternate links to be created of each link
MODEL_SF    = 'sf'
MODEL_EXP   = 'exp'
MODEL_RAND  = 'rand'

def addnode(vertices):
    vertex = svc_nodes.Vertex(ns.network.Node())
    return vertices.addvertex(vertex)

def randomfail(vertices):
    # choose a node randomly and make it fails

    nact = vertices.getnbofactive()
    if not nact:
        # no vertices in the network
        return

    totmandlinks = vertices.gettotmandlinks()
    totaltlinks = vertices.gettotaltlinks()

    index = random.randrange(nact)
    idx = vertices.getindexbyact(index)
    ###
    #print 'index: '+ str(idx)
    #print 'indegree: '+ str(vertices.getvertex(idx).getindegree())
    #print '========'
    vertices.dofail(idx)

    vertices.analyzer.fail(
        vertices.getnbofremoved()
        , vertices.getnboffail()
        , vertices.analyzer.getmandfail() + totmandlinks - vertices.gettotmandlinks()
        , vertices.analyzer.getaltfail() + totaltlinks - vertices.gettotaltlinks()
        , vertices.getvertex(idx).getindegree()
        , vertices.getvertex(idx).getoutdegree())

def connect(vertices, indexp, indexq, indexexst=None):
    # connect node p to node q
    # if indexexst is provided, node q is an alternative of node at indexexst

#    pointToPoint = ns.point_to_point.PointToPointHelper()
#    pointToPoint.Install(vertices.getvertex(indexp).getnode(), vertices.getvertex(indexq).getnode())
#    vertices.connect(indexp, indexq)

    channel = ns.point_to_point.PointToPointChannel()
    for i in [indexp, indexq]:
        node = vertices.getvertex(i).getnode()
        netdev = ns.point_to_point.PointToPointNetDevice()
        netdev.SetAddress(ns.network.Mac48Address.Allocate())
        netdev.Attach(channel)
        node.AddDevice(netdev)

    vertices.connect(indexp, indexq, channel, indexexst)

def initnetwork(vertices, m_init):
    # create m_init nodes and add it to the network 

    for i in range(m_init):
        addnode(vertices)

def chooserandom(vertices, nbofnodes=1):
    # choose nbofnodes nodes randomly
    return random.sample(range(vertices.getnbofvertices()), nbofnodes)

def choosepref(vertices, alpha=0, nbofnodes=1):
    # choose nbofnodes nodes based on BA preferential attachment with alpha as initial attractiveness
    # a node with higher indegree is more likely to be chosen than nodes with lower indegree

    ### mungkin masih bisa dioptimalkan dengan pencarian secara random
    ### atau cari algoritma pencarian yang lebih cepat
    #pdb.set_trace()
    nver = vertices.getnbofvertices()
    # totdegalpha = (SIGMAj(kj + alpha))
    totdegalpha = vertices.gettotdegree() + nver * alpha
    lsidx = range(nver)
    prevr = totdegalpha + 1 # large enough value
    nodes = []

    for i in range(nbofnodes):
        #pdb.set_trace()
        # generate a random number between 1 to totdegalpha
        r = random.randint(1, totdegalpha)
        if r < prevr:
            # search from the beginning of lsidx
            j = 0
            sumdegree = 0

        stop = False
        while j < len(lsidx) and not stop:
            idx = lsidx[j]
            degalpha = vertices.getvertex(idx).getindegree() + alpha
            sumdegree += degalpha

            if sumdegree >= r:
                # stop the loop
                stop = True
                # add the index to the solution list
                nodes.append(idx)
                # remove the index from lsidx to prevent it to be chosen again
                lsidx.pop(j)
                # "remove" its degree
                totdegalpha -= degalpha
                sumdegree -= degalpha
                # record the current random number for later comparison
                prevr = r
            else:
                j += 1

    return nodes

def addcompsvc(vertices, m_dep, m_alt, alpha, model, indexp=None):
    # add one node (except in MODEL_RAND mode) and connect it to m_dep_i links
    # for each link, add m_alt_j alternate links
    # model = 'sf', 'exp', 'rand'
    # prec:
    # - number of existing nodes >= 2

    nver = vertices.getnbofvertices()
    nverless = nver - 1

    # generate m_dep_i, the number of links to be created
    # atomic services are created outside this function, randrange starts from 1
    m_dep_i = random.randrange(1, m_dep)

    if m_dep_i > nver:
        m_dep_i = nver

    if model == MODEL_SF:
        # choose existing nodes to be connected using preferential attachment
        lsnodeidx = choosepref(vertices, alpha, m_dep_i)
    else:
        # model == MODEL_EXP or MODEL_RAND
        # choose existing nodes randomly
        lsnodeidx = chooserandom(vertices, m_dep_i)

    if model != MODEL_RAND:
        # add one node
        indexp = addnode(vertices)

    # create m_dep_i links
    for indexq in lsnodeidx:

        # create link to the node if they are not connected
        if not vertices.isconnected(indexp, indexq):
            connect(vertices, indexp, indexq)

            # generate m_alt_j, the number of alternate links of p->q
            m_alt_j = random.randrange(m_alt)
            if m_alt_j > nverless:
                m_alt_j = nverless

            # create m_alt_j links
            if model == MODEL_SF:
                # choose alternatives using preferential attachment
                lsaltidx = choosepref(vertices, alpha, m_alt_j)
            else:
                # model == MODEL_EXP or MODEL_RAND
                # choose alternatives randomly
                lsaltidx = chooserandom(vertices, m_alt_j)

            for indexr in lsaltidx:
                # create link p->r if r is not p and they are not connected
                if indexp != indexr and not vertices.isconnected(indexp, indexr):
                    # create link p->r as an alternative of p->q
                    connect(vertices, indexp, indexr, indexq)

#                # choose alternatives randomly
#                for k in range(m_alt_j):
#
#                    # choose an existing node randomly
#                    #indexr = random.randrange(nverless)
#                    indexr = random.randrange(nver)
#                    # create link p->r if r is not p and they are not connected
#                    if indexp != indexr and not vertices.isconnected(indexp, indexr):
#                        # create link p->r as an alternative of p->q
#                        connect(vertices, indexp, indexr, indexq)

def grow(vertices, comp, m_add, m_dep, m_alt, alpha, model=MODEL_SF):
    # add m_add nodes to the network if model is not MODEL_RAND
    # if model is MODEL_RAND, connect existing nodes randomly to each other. in this case m_add is not used 

    if model == MODEL_RAND:
        # for each isolated vertex
        # create links (dependency and alternate links) to existing nodes randomly
        # random network has been initialized with large number N nodes, where N is the size of the network

        for indexp in range(vertices.getnbofvertices()):
            if random.random() < comp:
                # connect indexp node to an existing node randomly
                addcompsvc(vertices, m_dep, m_alt, alpha, model, indexp)

    else:
        # exponential or scale-free
        # add m_add nodes and connect them to existing nodes

        for i in range(m_add):
            if random.random() < comp:
                # add a composite service node
                addcompsvc(vertices, m_dep, m_alt, alpha, model)
            else:
                # add an atomic service node
                addnode(vertices)

    vertices.analyzer.grow(
        vertices.getnbofvertices()
        , vertices.gettotmandlinks()
        , vertices.gettotaltlinks())

    ###!!!
    #print '** countconnect **'
    #print vertices.countconnect

    # verbose
    #vertices.printinfo()

def addpwvertex(vertices, dictvid, vid, pwapis, m_dep, m_alt, alpha, model):
    # add a pw api to vertices as a new vertex if not exist in dictvid
    # process recursively to its component/children

    if dictvid.has_key(vid):
        # vid has been added into the network; get the index
        indexp = dictvid[vid]

    else:
        # vid not in dictvid; add to the network
        indexp = addnode(vertices)
        # add to the directory of added vids
        dictvid[vid] = indexp

    lscompvid = pwapis[str(vid)][pwj.IDX_CHILDREN] # list of list of vid
    lsoutlink = [] # list of list of index

    # process the children/component if any
    # convert list of list of vid (lscompvid) into list of list of index (lsoutlink)
    for altgrp in lscompvid:
        lsalt = []

        for compvid in altgrp:
            # recursively add compvid node to vertices and create connection
            lsalt.append(addpwvertex(vertices, dictvid, compvid, pwapis, m_dep, m_alt, alpha, model))

        if lsalt:
            # len(lsalt) > 0
            lsoutlink.append(lsalt)

    nver = vertices.getnbofvertices()
    nverless = nver - 1

    # choose more vertices according to m_dep_i (defined below)
    if m_dep > 1:
        m_dep_i = random.randrange(1, m_dep)

        if m_dep_i > nver:
            m_dep_i = nver

        if model == MODEL_SF:
            # choose existing nodes to be connected using preferential attachment
            lsdepadd = choosepref(vertices, alpha, m_dep_i)
        else:
            # model == MODEL_EXP or MODEL_RAND
            # choose existing nodes randomly
            lsdepadd = chooserandom(vertices, m_dep_i)

        # add indexes in lsdepadd to lsoutlink as strong dependency links
        for indexdepadd in lsdepadd:
            if [indexdepadd] not in lsoutlink:
                lsoutlink.append([indexdepadd])

    # for each lsalt in lsoutlink,
    # choose existing nodes to be connected as alternative
#    print "m_alt "+ str(m_alt)
    if m_alt > 0:
        for lsalt in lsoutlink:
            # generate m_alt_j, the number of alternate links
            m_alt_j = random.randrange(m_alt)
            if m_alt_j > nverless:
                m_alt_j = nverless

            # create m_alt_j links
            if model == MODEL_SF:
                # choose alternatives using preferential attachment
                lsaltidx = choosepref(vertices, alpha, m_alt_j)
            else:
                # model == MODEL_EXP or MODEL_RAND
                # choose alternatives randomly
                lsaltidx = chooserandom(vertices, m_alt_j)

#            print "len lsaltidx "+ str(len(lsaltidx))
            # add indexes in lsaltidx to lsoutlink as alternate links
            for indexalt in lsaltidx:
                if indexalt not in lsalt:
                    lsalt.append(indexalt)

    # create connection based on lsoutlink
    for lsalt in lsoutlink:
        # connect indexp to indexdep, the first elmt of lsalt
        indexdep = lsalt[0]
        if indexp != indexdep and not vertices.isconnected(indexp, indexdep):
            connect(vertices, indexp, indexdep)

#        print lsalt
#        if len(lsalt) > 1:
#            print lsalt
        # connect indexp to the other elmts as alternate of indexdep
        for indexalt in lsalt[1:]:
            # connect indexp to compvid node as alternative of indexdep
            if indexp != indexalt and not vertices.isconnected(indexp, indexalt):
                connect(vertices, indexp, indexalt, indexdep)

    return indexp

def snapshottopwapis(snapshot):
    # convert snapshot to pwapis format
    # snapshot {vid:[isactive, outlinks, inlinks, altls, altref], ...}
    # pwapis {vid:[indegree, outdegree, name, mashuptype, [[compvid, ...], ...]], ...}

    pwapis = {}
    for vid in snapshot.keys():

        vsnap = snapshot[vid]

        indegree = len(vsnap[2]); outdegree = len(vsnap[1])
        name = str(vid)
        mashuptype = outdegree > 0
        lscomp = vsnap[3]

        pwapis[vid] = [indegree, outdegree, name, mashuptype, lscomp]

    return pwapis

def buildfromjson(vertices, filename, m_dep, m_alt, alpha, model, fmt=0):
    # build network from programmable web apis

    # pwapis {vid:[indegree, outdegree, name, mashuptype, [[compvid, ...], ...]], ...}
    pwapis = pwj.load(filename)

    if fmt:
        # fmt != 0, "snapshot" format
        pwapis = snapshottopwapis(pwapis["snapshot"][0])

    dictvid = {}
    for vid in pwapis.keys():
        addpwvertex(vertices, dictvid, vid, pwapis, m_dep, m_alt, alpha, model)

    vertices.analyzer.grow(
        vertices.getnbofvertices()
        , vertices.gettotmandlinks()
        , vertices.gettotaltlinks())

def print_params(vertices, m_init, comp, m_add, m_dep, m_alt, alpha, timegrow, timefail, freq):
    # print statistic
    leftwidth = 10
    print '========================='
    print 'Parameters'
    print '%s : %6d' % ('alpha'.ljust(leftwidth), alpha)
    print '%s : %8.1f' % ('comp'.ljust(leftwidth), comp)
    print '%s : %6d' % ('m_init'.ljust(leftwidth), m_init)
    print '%s : %6d' % ('m_add'.ljust(leftwidth), m_add)
    print '%s : %6d' % ('m_dep'.ljust(leftwidth), m_dep)
    print '%s : %6d' % ('m_alt'.ljust(leftwidth), m_alt)
    print '%s : %6d' % ('timegrow'.ljust(leftwidth), timegrow)
    print '%s : %6d' % ('timefail'.ljust(leftwidth), timefail)
    print '%s : %6d' % ('freq'.ljust(leftwidth), freq)

def print_stats(vertices):
    leftwidth = 35
    print '========================='
    print '%s : %5d' % ('Nodes created'.ljust(leftwidth), vertices.getnbofvertices())
    print '%s : %5d' % ('Total indegree (outdegree)'.ljust(leftwidth), vertices.gettotdegree())
    print '%s : %5d (#%d)' % ('Max indegree'.ljust(leftwidth), vertices.getmaxindegree(), vertices.getmaxindegreeidx())
    #vertices.getvertex(vertices.getmaxindegreeidx()).printinfo()
    print '%s : %5d (#%d)' % ('Max outdegree'.ljust(leftwidth), vertices.getmaxoutdegree(), vertices.getmaxoutdegreeidx())
    #vertices.getvertex(vertices.getmaxoutdegreeidx()).printinfo()
    print '%s : %5d' % ('Number of strong ("AND") dependency'.ljust(leftwidth), vertices.gettotmandlinks())
    print '%s : %5d (#%d)' % ('Max number'.ljust(leftwidth), vertices.getmaxmandlinks(), vertices.getmaxmandlinksidx())
    print '%s : %8.2f' % ('Average'.ljust(leftwidth), float(vertices.gettotmandlinks()) / vertices.getnbofvertices())
    #vertices.getvertex(vertices.getmaxmandlinksidx()).printinfo()
    print '%s : %5d' % ('Number of weak ("OR") dependency'.ljust(leftwidth), vertices.gettotaltlinks())
    print '%s : %5d (#%d)' % ('Max number'.ljust(leftwidth), vertices.getmaxaltlinks() or svc_nodes.NODEGREE, vertices.getmaxaltlinksidx() or svc_nodes.NODEGREE)
    print '%s : %8.2f' % ('Average'.ljust(leftwidth), float(vertices.gettotaltlinks()) / vertices.getnbofvertices())
    #vertices.getvertex(vertices.getmaxaltlinksidx()).printinfo()
    print '%s : %5d (#%d)' % ('Max depth'.ljust(leftwidth), vertices.getmaxdepth(), vertices.getmaxdepthidx())
    print '%s : %8.2f (#%d)' % ('Max mean depth'.ljust(leftwidth), vertices.getmaxmeandepth(), vertices.getmaxmeandepthidx())
    #print '%s : %8.2f' % ('Average'.ljust(leftwidth), vertices.getavgdepth())

def print_aftermath(vertices):
    leftwidth = 35
    print '========================='
    print '%s : %5d' % ('Nodes created'.ljust(leftwidth), vertices.getnbofvertices())
    print '%s : %5d' % ('Fail nodes'.ljust(leftwidth), vertices.getnboffail())
#    print 'nodescreated'
#    print vertices.analyzer.nodescreated
#    print 'nodesremoved'
#    print vertices.analyzer.nodesremoved
#    print 'nodesfailed'
#    print vertices.analyzer.nodesfail
#    print 'linkscreated'
#    print vertices.analyzer.linkscreated
#    print 'linksfailed'
#    print vertices.analyzer.linksfail
#    print 'altcreated'
#    print vertices.analyzer.altcreated
#    print 'altfail'
#    print vertices.analyzer.altfail
#    print 'mandcreated'
#    print vertices.analyzer.mandcreated
#    print 'mandfail'
#    print vertices.analyzer.mandfail
#    vertices.analyzer.plotfailure()

def __test(argv):
    vertices = svc_nodes.Vertices()
    initnetwork(vertices, 10)
    print "### Print Info vertices ###"
    vertices.printinfo()
    print "### Choose node ###"
    print choosepref(vertices, 10, 3)
    print "### grow(vertices, 1, 2, 2, 10) ###"
    for i in range(10):
        grow(vertices, 1, 2, 2, 10)
    print "### Print Info vertices ###"
    vertices.printinfo()

if __name__ == '__main__':
    sys.exit(__test(sys.argv))


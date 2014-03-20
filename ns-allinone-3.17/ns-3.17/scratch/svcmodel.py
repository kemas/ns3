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
import ns.network
import ns.point_to_point

ALPHA   = 1 # default number of alpha >= 0, initial attractiveness for young nodes
M_INIT  = 3 # default initial number of nodes
M_ADD   = 1 # default number of nodes to be added in every timestep
M_DEP   = 3 # default upper limit number of links to be created from each added node
M_ALT   = 3 # default upper limit number of alternate links to be created of each link

def addnode(vertices):
    vertex = svc_nodes.Vertex(ns.network.Node())
    return vertices.addvertex(vertex)

def randomfail(vertices):
    # choose a node randomly and make it fails
    totmandlinks = vertices.gettotmandlinks()
    totaltlinks = vertices.gettotaltlinks()

    nact = vertices.getnbofactive()
    if not nact:
        # no vertices in the network
        return

    index = random.randrange(nact)
    vertices.dofail(vertices.getindexbyact(index))

    vertices.analyzer.fail(
        vertices.getnbofremoved()
        , vertices.getnboffail()
        , vertices.analyzer.getmandfail() + totmandlinks - vertices.gettotmandlinks()
        , vertices.analyzer.getaltfail() + totaltlinks - vertices.gettotaltlinks())

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

def choosenodes(vertices, alpha=0, nbofnodes=1):
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

def addnewnode(vertices, m_dep, m_alt, alpha, ispref=True):
    # add one node and connect it to m_dep_i links
    # for each link, add m_alt_j alternate links
    # prec:
    # - number of existing nodes >= 2

    nver = vertices.getnbofvertices()
    nverless = nver - 1

    # generate m_dep_i, the number of links to be created
    m_dep_i = random.randrange(m_dep)
    if m_dep_i > nver:
        m_dep_i = nver

    if ispref:
        # choose existing nodes to be connected to using preferential attachment
        lsnodeidx = choosenodes(vertices, alpha, m_dep_i)
    else:
        # choose existing nodes randomly
        lsnodeidx = chooserandom(vertices, m_dep_i)

    # add one node
    indexp = addnode(vertices)

    sumalt = 0
    # create m_dep_i links
    for indexq in lsnodeidx:

        # create link to the node if they are not connected
        if not vertices.isconnected(indexp, indexq):
            connect(vertices, indexp, indexq)

            # generate m_alt_j, the number of alternate links of p->q
            m_alt_j = random.randrange(m_alt)
            if m_alt_j > nverless:
                m_alt_j = nverless
            sumalt += m_alt_j

            # create m_alt_j links
            for k in range(m_alt_j):

                # choose an existing node randomly
                indexr = random.randrange(nverless)
                # create link p->r if r is not p and they are not connected
                if indexp != indexr and not vertices.isconnected(indexp, indexr):
                    # create link p->r as an alternative of p->q
                    connect(vertices, indexp, indexr, indexq)

def grow(vertices, m_add, m_dep, m_alt, alpha, ispref=True):
    # add m_add nodes to the network

    for i in range(m_add):
        addnewnode(vertices, m_dep, m_alt, alpha, ispref)

    vertices.analyzer.grow(
        vertices.getnbofvertices()
        , vertices.gettotmandlinks()
        , vertices.gettotaltlinks())

def print_params(vertices, m_init, m_add, m_dep, m_alt, alpha, timegrow, timefail, freq):
    # print statistic
    leftwidth = 10
    print '========================='
    print 'Parameters'
    print '%s : %6d' % ('alpha'.ljust(leftwidth), alpha)
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
    print choosenodes(vertices, 10, 3)
    print "### grow(vertices, 1, 2, 2, 10) ###"
    for i in range(10):
        grow(vertices, 1, 2, 2, 10)
    print "### Print Info vertices ###"
    vertices.printinfo()

if __name__ == '__main__':
    sys.exit(__test(sys.argv))


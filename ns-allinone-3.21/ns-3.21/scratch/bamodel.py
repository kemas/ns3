#import pdb

import sys
import random
import sf_nodes
import ns.network
import ns.point_to_point

M0 = 2 # default initial number of nodes
M_ADD = 1 # default number of nodes to be added in every timestep

def addnode(vertices):
    vertex = sf_nodes.Vertex(ns.network.Node())
    return vertices.addvertex(vertex)

def linknodes(vertices, indexp, indexq):
    # link two nodes

#    pointToPoint = ns.point_to_point.PointToPointHelper()
#    pointToPoint.Install(vertices.getvertex(indexp).getnode(), vertices.getvertex(indexq).getnode())
#    vertices.linknodes(indexp, indexq)

    channel = ns.point_to_point.PointToPointChannel()
    for i in [indexp, indexq]:
        node = vertices.getvertex(i).getnode()
        netdev = ns.point_to_point.PointToPointNetDevice()
        netdev.SetAddress(ns.network.Mac48Address.Allocate())
        netdev.Attach(channel)
        node.AddDevice(netdev)

    vertices.linknodes(indexp, indexq, channel)

def initnodes(vertices, m0):
    # m0 nodes is added to the network
    # each node creates one link to an arbitrary another node

    # create m0 nodes and add it to the network
    for i in range(m0):
        addnode(vertices)

#    import pdb
#    pdb.set_trace()
    # create links between the nodes
    verlen = vertices.getlength()
    for indexp in range(verlen):
        # choose random vertex which is not itself
        indexq = random.randrange(verlen)
        while indexq == indexp:
            indexq = random.randrange(verlen)

        # check if these two have been connected to each other
        if not vertices.is_connected(indexp, indexq):
            # they are not connected, make connection
            linknodes(vertices, indexp, indexq)

def choosenode(vertices, pref=True):
    # choose a node according to BA model if pref==True, 
    # else choose a node randomly

    if pref:
        # choose a node using preferential attachment (BA model)

        # generate a random number between 1 to totdegree
        totdegree = vertices.gettotdegree()
        #pdb.set_trace()
        r = random.randint(1, totdegree)

        i = 0
        verlen = vertices.getlength()
        sumdegree = 0
        while i < verlen and sumdegree < r:
            sumdegree += vertices.getvertex(i).getdegree()
            if sumdegree < r:
                i += 1

    else:
        # choose a node randomly from existing nodes
        # excluding the newly added node (nbofvertices - 1)
        i = random.randrange(vertices.getlength() - 1)

    return i

def grow(vertices, m_add, pref=True):
    # add a node and connect to m_add existing nodes

    verlen = vertices.getlength()
    if m_add > verlen:
        m_add = verlen

    indexp = addnode(vertices)

    for i in range(m_add):
        # choose existing node to connect
        indexq = choosenode(vertices, pref)
        while indexp == indexq:
            indexq = choosenode(vertices, pref)

        # connect these two if they are not connected
        if not vertices.is_connected(indexp, indexq):
            linknodes(vertices, indexp, indexq)

#    index_p = addnode(vertices)
#    verlen = veri
#    for i in range(m_add):
#        index_exist = choosenode(vertices)
#        while index_new == index_exist:
#            index_exist = choosenode(vertices)
#
#        # check if these two have been connected to each other
#        if not vertices.is_connected(index_new, index_exist):
#            # they are not connected, make connection
#            linknodes(vertices, index_new, index_exist)

def __test(argv):
    vertices = sf_nodes.Vertices()
    initnodes(vertices, 10)
    print "### Print Info vertices ###"
    vertices.printinfo()
    print "### Choose node ###"
    print choosenode(vertices)
    print "### grow(vertices, 200) ###"
    grow(vertices, 200)
    print "### Print Info vertices ###"
    vertices.printinfo()

if __name__ == '__main__':
    sys.exit(__test(sys.argv))


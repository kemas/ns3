import pdb
import sys
import random
import sf_nodes
import ns.network
import ns.point_to_point

ALPHA = 1 # default number of alpha >= 0, initial attractiveness for young sites
M0 = 2 # default initial number of nodes, m >= 2 to prevent infinite looping
M_ADD = 1 # default number of links to be connected to one newly created node in every timestep
L_ADD = 1 #5 # default number of new links added in every timestep
L_REWIRE = 1 #5 # default number of links to be rewired in every timestep
# m_add, l_add, l_rewire, alpha >= 0, and m_add + link_add > 0 

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

def disconnectnodes(vertices, indexp, indexq):
    # disconnect two connected nodes
    # nodes are assumed to be connected
    # because currently ns-3 does not support channel disconnection
    # and does not completely support channel destruction
    # here, disconnection is performed by disposing (destroying) netdevices connected to that channel

    vertexp = vertices.getvertex(indexp)
    idxlinktoq = vertexp.getlinkid(indexq)
    channel = vertexp.getchannel(idxlinktoq)

    for i in range(channel.GetNDevices()):
        #print "Dispose device node %d" % channel.GetDevice(i).GetNode().GetId()
        channel.GetDevice(i).Dispose()
    #channel.Dispose()

    vertices.disconnectnodes(indexp, indexq)

def initnodes(vertices, m0):
    # m0 nodes is added to the network
    # no links added between them

    # create m0 nodes and add it to the network
    #pdb.set_trace()
    for i in range(m0):
        addnode(vertices)

def choosenode(vertices, alpha):
    # based on the PI(ki, alpha) probability function of the A model
    # a vertex is chosen based on its degree (ki) and initial attractiveness (alpha)
    # original formula: PI(ki, alpha) = (ki + alpha) / (SIGMAj(kj + alpha))

    # generate a random number between 1 to totdegree
    # totdegree = (SIGMAj(kj + alpha))
    verlen = vertices.getlength()
    totdegree = vertices.gettotdegree() + verlen * alpha
    #pdb.set_trace()
    r = random.randint(1, totdegree)

    i = 0
    sumdegree = 0
    while i < verlen and sumdegree < r:
        sumdegree += vertices.getvertex(i).getdegree() + alpha
        if sumdegree < r:
            i += 1

    return i

def addnewlinks(vertices, alpha, l_add):
    # add l_add new links between existing vertices
    # choose randomly l_add number of vertices
    # for each chosen vertex, connect to other vertex based on the probability function

    # choose l_add number of random vertices
    verlen = vertices.getlength()
    #pdb.set_trace()
    if l_add > verlen:
        l_add = verlen
    lsindex = random.sample(range(verlen), l_add)

    for indexp in lsindex:
        # choose another vertex to be connected to
        indexq = choosenode(vertices, alpha)
        while indexp == indexq:
            indexq = choosenode(vertices, alpha)
        # connect these two if they are not connected
        if not vertices.is_connected(indexp, indexq):
            #print "** linknodes: %d %d" % (vertices.getvertex(indexp).getnode().GetId(), vertices.getvertex(indexq).getnode().GetId())
            linknodes(vertices, indexp, indexq)

def addnewnode(vertices, alpha, m_add):
    # add one node and connect it to m_add new links

    verlen = vertices.getlength()
    if m_add > verlen:
        m_add = verlen

    indexp = addnode(vertices)

    for i in range(m_add):
        indexq = choosenode(vertices, alpha)
        while indexp == indexq:
            indexq = choosenode(vertices, alpha)
        # connect these two if they are not connected
        if not vertices.is_connected(indexp, indexq):
            linknodes(vertices, indexp, indexq)

def rewirelinks(vertices, alpha, l_rewire):
    # rewire l_rewire links
    # for l_rewire times, select a random node p
    # select a link lpq, rewire lpq to a new node p'

    # choose l_rewire number of random vertices
    verlen = vertices.getlength()
    if l_rewire > verlen:
        l_rewire = verlen
    lsindex = random.sample(range(verlen), l_rewire)

    for indexp in lsindex:
        vertexp = vertices.getvertex(indexp)
        # choose a random neighbor of vertexp if exist
        nboflinks = vertexp.getnboflinks()
        if nboflinks > 0:
            indexq = vertexp.getneighboridx(random.randrange(nboflinks))
            # choose a vertexp' to rewire the link from vertexp to vertexp'
            indexpnew = choosenode(vertices, alpha)
            while indexpnew == indexp:
                indexpnew = choosenode(vertices, alpha)
            if not vertices.is_connected(indexpnew, indexq):
                #print "rewire %d-%d to %d-%d" % (indexp, indexq, indexpnew, indexq)
                # disconnect vertexp and vertexq
                disconnectnodes(vertices, indexp, indexq)
                # connect vertexp' and vertexq
                linknodes(vertices, indexpnew, indexq)

def grow(vertices, alpha, l_add, m_add, l_rewire):
    addnewlinks(vertices, alpha, l_add)
    addnewnode(vertices, alpha, m_add)
    rewirelinks(vertices, alpha, l_rewire)

#def __test(argv):
#    vertices = sf_nodes.Vertices()
#    initnodes(vertices, 10)
#    print "### Print Info vertices ###"
#    vertices.printinfo()
#    print "### Choose node ###"
#    print choosenode(vertices)
#    print "### grow(vertices, 200) ###"
#    grow(vertices, 200)
#    print "### Print Info vertices ###"
#    vertices.printinfo()

if __name__ == '__main__':
    sys.exit(__test(sys.argv))


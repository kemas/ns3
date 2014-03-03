import pdb
import sys
import random
import sf_nodes
import amodel
import ns.network
import ns.point_to_point

M0 = 2 # default initial number of nodes, m >= 2 to prevent infinite looping
M_ADD = 1 # default number of links to be connected to one newly created node in every timestep
L_ADD = 1 #5 # default number of new links added in every timestep
L_DEL = 1 #5 # default number of links to be rewired in every timestep
# m_add, l_add, l_del >= 0, and m_add + link_add > 0 

def initnodes(vertices, m0):
    amodel.initnodes(vertices, m0)

def choosenode(vertices):
    # based on the PI(ki) probability function
    # a vertex is chosen based on its degree (ki)
    # original formula: PI(ki) = (ki) / (SIGMAj(kj))

    # generate a random number between 1 to totdegree
    # totdegree = (SIGMAj(kj))
    verlen = vertices.getlength()
    totdegree = vertices.gettotdegree()
    #pdb.set_trace()

    if totdegree > 0:
        r = random.randint(1, totdegree)

        i = 0
        sumdegree = 0
        while i < verlen and sumdegree < r:
            sumdegree += vertices.getvertex(i).getdegree()
            if sumdegree < r:
                i += 1
    else:
        # totdegree == 0, new network or links were deleted
        # choose vertex randomly
        i = random.randrange(verlen)

    return i

def addnewnode(vertices, m_add):
    # add one node and connect it to m_add new links

    verlen = vertices.getlength()
    if m_add > verlen:
        m_add = verlen

    indexp = amodel.addnode(vertices)

    for i in range(m_add):
        indexq = choosenode(vertices)
        while indexp == indexq:
            indexq = choosenode(vertices)
        # connect these two if they are not connected
        if not vertices.is_connected(indexp, indexq):
            amodel.linknodes(vertices, indexp, indexq)

def addnewlinks(vertices, l_add):
    # add l_add new links between existing vertices
    # choose randomly l_add number of vertices
    # for each chosen vertex, connect to other vertex based on the probability function

    # choose l_add number of random vertices
    verlen = vertices.getlength()
    if l_add > verlen:
        l_add = verlen

    lsindex = random.sample(range(verlen), l_add)

    for indexp in lsindex:
        # choose another vertex to be connected to
        indexq = choosenode(vertices)
        while indexp == indexq:
            indexq = choosenode(vertices)
        # connect these two if they are not connected
        if not vertices.is_connected(indexp, indexq):
            amodel.linknodes(vertices, indexp, indexq)

def antichoosenode(vertices, ignorezerodeg=True):
    # based on the PI*(ki) anti-preferential probability function
    # if ignorzerodeg is True, zero degree nodes are not included in the calculation

    verlen = vertices.getlength()
    if ignorezerodeg:
        nbofvertices = 0
        for i in range(verlen):
            if vertices.getvertex(i).getdegree() > 0:
                nbofvertices += 1
    else:
        nbofvertices = verlen

    totdegree = vertices.gettotdegree()
    #pdb.set_trace()
    totsum = totdegree * (nbofvertices - 1) 

    if totsum > 0:
        r = random.randint(1, totsum)
        i = 0
        sumdegree = 0

        if ignorezerodeg:
            while i < verlen and sumdegree < r:
                if vertices.getvertex(i).getdegree() > 0:
                    sumdegree += totdegree - vertices.getvertex(i).getdegree()
                    if sumdegree < r:
                        i += 1
                else:
                    i += 1

        else:
            while i < verlen and sumdegree < r:
                sumdegree += totdegree - vertices.getvertex(i).getdegree()
                if sumdegree < r:
                    i += 1

    else:
        # totdegree == 0, new network or links were deleted
        # choose vertex randomly
        i = random.randrange(verlen)

    return i

def dellinks(vertices, l_del):
    # delete l_del links
    # for l_del times, select a node p based on anti-preferential probability function

    verlen = vertices.getlength()
    if l_del > verlen:
        l_del = verlen

    for i in range(l_del):
        indexp = antichoosenode(vertices)
        vertex = vertices.getvertex(indexp)
        # disconnect with one of the neighbors
        indexq = vertex.getneighboridx(random.randrange(vertex.getnboflinks()))
        amodel.disconnectnodes(vertices, indexp, indexq)

#        while vertex.getnboflinks() > 0:
#            #pdb.set_trace()
#            
#            vertices.disconnectnodes(index, vertex.getneighboridx(0))

def grow(vertices, m_add, l_add, l_del):
    addnewnode(vertices, m_add)
    addnewlinks(vertices, l_add)
    dellinks(vertices, l_del)

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


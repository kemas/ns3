import random
import pdb

def initvertices(nver, degrange):
    vertices = []
    for i in range(nver):
        vertices.append(random.randrange(degrange))

    return vertices

def gettotdegree(vertices):
    totdegree = 0
    for deg in vertices:
        totdegree += deg
    return totdegree

def choosenode(vertices, alpha, nbofnodes=1):
    # choose nbofnodes nodes based on BA preferential attachment with alpha as initial attractiveness
    # a node with higher indegree is more likely to be chosen than nodes with lower indegree

    nver = len(vertices)
    # generate a random number between 1 to totdegalpha
    # totdegalpha = (SIGMAj(kj + alpha))
    totdegalpha = gettotdegree(vertices) + nver * alpha
    print "> totdegalpha:"
    print totdegalpha
    #pdb.set_trace()
    #r = random.randint(1, totdegalpha)
    rands = random.sample(range(1, totdegalpha + 1), nbofnodes)
    rands.sort()
    print "> rands:"
    print rands

    i = 0
    sumdegree = 0
    nodes = []
    previ = None

    pdb.set_trace()
    for r in rands:
        if sumdegree >= r:
            nodes.append(previ)
        else:
            while i < nver and sumdegree < r:
                sumdegree += vertices[i] + alpha
                if sumdegree >= r:
                    nodes.append(i)
                previ = i
                i += 1

    return nodes


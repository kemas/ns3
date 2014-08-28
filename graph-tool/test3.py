import pdb
import sys
import random

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

def choosenode(vertices, alpha=0, nbofnodes=1):
    # choose nbofnodes nodes based on BA preferential attachment with alpha as initial attractiveness
    # a node with higher indegree is more likely to be chosen than nodes with lower indegree

    pdb.set_trace()
    nver = len(vertices)
    totdegalpha = gettotdegree(vertices) + nver * alpha
    lsidx = range(nver)
    prevr = totdegalpha + 1 # large enough value
    nodes = []

    for i in range(nbofnodes):
        pdb.set_trace()
        # generate a random number between 1 to totdegalpha
        r = random.randint(1, totdegalpha)
        print "r: "+ str(r)
        if r < prevr:
            # search from the beginning of lsidx
            j = 0
            sumdegree = 0

        stop = False
        while j < len(lsidx) and not stop:
            idx = lsidx[j]
            degalpha = vertices[idx] + alpha
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

def __test(argv):
    vertices = initvertices(10, 20)
    print vertices
    totdegree = gettotdegree(vertices)
    print totdegree
    nodes = choosenode(vertices, 0, 20)
    print nodes

if __name__ == '__main__':
    sys.exit(__test(sys.argv))


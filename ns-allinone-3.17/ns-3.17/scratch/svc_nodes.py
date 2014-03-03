# svc_nodes.py
# Data structure for service network.
# The network is a directed network where vertex represent services and links represent dependency between services.
# There are two kinds of dependency: full and partial dependency

#import pdb
import sys

NODEGREE = -999

class AltLinks:
    # Class of list of list of vertex indices
    # Two vertices can substitute each other if the indices are listed in the same list of indices

    def __init__(self):
        self._ls = [] # list of list of links
        self._ref = {} # reference dictionary {idxvertex: [index, index], ...}

    def getidxaltlink(self, idxvertex):
        # get the index of idxvertex in _ls

        if self._ref.has_key(idxvertex):
            return self._ref[idxvertex]
        else:
            return None

    def addalt(self, idxvertex, idxalt):
        # add an alternative of idxvertex
        # idxvertex maybe exist
        # idxalt does not exist

        #pdb.set_trace()
        idxls = self.getidxaltlink(idxvertex)
        if idxls:
            # idxls != None, idxvertex exists
            # only add idxalt to the same list as idxvertex
            i = idxls[0]
            self._ls[i].append(idxalt)
            # add the indices of idxalt to the reference dictionary _ref
            self._ref[idxalt] = [i, len(self._ls[i]) - 1]
        else:
            # idxvertex does not exist
            # add both idvertex and idxalt
            self._ls.append([idxvertex, idxalt])
            i = len(self._ls) - 1
            # add to the reference dictionary _ref
            self._ref[idxvertex] = [i, 0]
            self._ref[idxalt] = [i, 1]

    def delaltbyidxls(self, i, j):
        # remove index at [i][j]
        # after deletion, if the same list only has one index, also delete this remaining index

        # remove from the list of index
        idxvertex = self._ls[i].pop(j)
        # remove from the reference dictionary
        self._ref.pop(idxvertex)
        # check the remaining indices in the same list _ls[i]
        if len(self._ls[i]) == 1:
            # list _ls[i] has only one index, remove the list
            lsidx = self._ls.pop(i)
            # remove the lone idxvertex from the reference dictionary
            self._ref.pop(lsidx[0])

    def delaltbyidxvertex(self, idxvertex):
        # remove idxvertex
        # after deletion, if the same list only has one index, also delete this remaining index
        # idxvertex exists

        # idxvertex is assumed to exist, no checking is needed
        i, j = getidxaltlink(idxvertex)
        self.delaltbyidxls(i, j)

class Vertex:
    # class of Vertex in a directed network

    def __init__(self, node, indegree=0, outdegree=0):
        self._data = [node, indegree, outdegree]
        self._outlinks = [] # outgoing links
        self._inlinks = [] # incoming links
        self._channels = []
        self._altlinks = AltLinks() # list of list of vertex indices connected by outgoing links
        self._isactive = True

    def isactive(self):
        return self._isactive

    def deactivate(self):
        # set active status to False
        self._isactive = False

    def fail(self):
        # deactivate this vertex
        # propagate failure to other fully dependent nodes

        # deactivate
        self.deactivate()
        # set color
        # node...

        # propagate failure
        for idxneighbor in self._inlinks:
            ###wrong, idxneighbor != neighbor
            if not neighbor.ispartiallydepend(index) and neighbor.isactive():
                # neighbor is fully depend and active
                # propagate the deactivation
                neighbor.fail()

    def getnode(self):
        return self._data[0]

    def getindegree(self):
        return self._data[1]

    def getoutdegree(self):
        return self._data[2]

    def _incrindegree(self, addby = 1):
        self._data[1] += addby

    def _decrindegree(self, substrby = 1):
        self._data[1] -= substrby

    def _incroutdegree(self, addby = 1):
        self._data[2] += addby

    def _decroutdegree(self, substrby = 1):
        self._data[2] -= substrby

    def getchannel(self, index):
        return self._channels[index]

    def itroutlinks(self):
        return self._outlinks.__iter__()

    def itrinlinks(self):
        return self._inlinks.__iter__()

    def getnbofoutlinks(self):
        return len(self._outlinks)

    def getnbofinlinks(self):
        return len(self._inlinks)

    def getneighborbyoutlink(self, index):
        # get the index of a neighbor connected from this vertex
        return self._outlinks[index]

    def getneighborbyinlink(self, index):
        # get the index of a neighbor connected to this vertex
        return self._inlinks[index]

    def getoutlinkbyver(self, idxvertex):
        # get the index of _outlinks that contains idxvertex
        # return None when idxvertex is not found

        found = False
        i = 0
        while not found and i < self.getnbofoutlinks():
            if self.getneighborbyoutlink(i) == idxvertex:
                found = True
            else:
                i += 1

        if found:
            return i
        else:
            return None

    def getinlinkbyver(self, idxvertex):
        # get the index of _inlinks that contains idxvertex
        # return None when idxvertex is not found

        found = False
        i = 0
        while not found and i < self.getnbofinlinks():
            if self.getneighborbyinlink(i) == idxvertex:
                found = True
            else:
                i += 1

        if found:
            return i
        else:
            return None

    def isconnectedto(self, index):
        return self._outlinks.count(index)

    def ispartiallydepend(self, index):
        # return true if this vertex is partially depend on the vertex at index
        return self.isconnectedto(index) and self._altlinks.getidxaltlink(index)

    def connectto(self, index, channel, indexexst=None):
        # connect this vertex to the vertex at index
        # if indexexst is given, the vertex at index is an alternate of the vertex at indexexst
        # currently no link from this vertex to the vertex at index
        # connectivity checking is not performed within this function

        # add the outlink (the index of the vertex)
        self._outlinks.append(index)
        # add the ns3 channel
        self._channels.append(channel)
        # increment the out degree
        self._incroutdegree()

        if indexexst:
            # add the information of alternate links to altlinks
            self._altlinks.addalt(indexexst, index)

    def connectfrom(self, index):
        # connect another vertex to this vertex

        # add the inlink (the index of the vertex)
        self._inlinks.append(index)
        # increment the indegree of this vertex because of the incoming edge from the vertex at index
        self._incrindegree()

    def disconnectto(self, index):
        # disconnect link from this vertex to the vertex at index
        # this vertex will be deactivated if no alternative in altlinks 
        # it is assumed no multiple links connected between the same pairs of vertices
        # i.e., self._outlinks has unique member

        # checking the connectivity between this vertex and the vertex at index
        if self.isconnectedto(index):
            # a link to vertex at the index exists, remove it
            idxlink = self.getoutlinkbyver(index) 
            self._outlinks.pop(idxlink)
            self._channels.pop(idxlink)
            # decrement the out degree
            self._decroutdegree()

            # remove the vertex from altlinks if any
            idxls = self._altlinks.getidxaltlink(index)
            if idxls != None:
                self._altlinks.delaltbyidxls(idxls[0], idxls[1])
            else:
                # no alternative, deactivate this vertex
                self.deactivate()

    def disconnectfrom(self, index):
        # disconnect another vertex from this vertex (connected by inlink)

        # get the link id of the vertex
        idxlink = self.getinlinkbyver(index) 
        # remove the vertex from inlinks
        self._inlinks.pop(idxlink)
        # decrement the indegree
        self._decrindegree()

    def printinfo(self):
        print "data    : "+ str(self._data)
        print "status  : "+ str(self.isactive())
        print "inlinks : "+ str(self._inlinks)
        print "outlinks: "+ str(self._outlinks)

    def printaltlinks(self):
        print self._altlinks._ls

class Vertices:
    def __init__(self):
        self._vertices = []
        self._totdegree = 0 # the sum of the number of indegree for all vertices
                            # this also the same as the sum of the number of outdegree
        self._maxindegree = NODEGREE
        self._maxindegreeidx = None
        self._maxoutdegree = NODEGREE
        self._maxoutdegreeidx = None

    def getmaxindegree(self):
        return self._maxindegree

#    def getmaxoutdegree(self):
#        return self._maxoutdegree

    def _updmaxindegree(self, idx=None):
        if idx != None:
            # only compares current maxindegree with the degree of the vertex at idx
            vertex = self.getvertex(idx)
            if vertex.getindegree() > self._maxindegree:
                self._maxindegree = vertex.getindegree()
                self._maxindegreeidx = idx

        else:
            # idx == None, find new max value
            maxindegree = NODEGREE
            maxindegreeidx = None
            for idx in range(self.getnbofvertices()):
                vertex = self.getvertex(idx)
                if vertex.getindegree() > maxindegree:
                    maxindegree = vertex.getindegree()
                    maxindegreeidx = idx

            self._maxindegree = maxindegree
            self._maxindegreeidx = maxindegreeidx

    def _updmaxoutdegree(self, idx=None):
        if idx != None:
            # only compares current maxoutdegree with the degree of the vertex at idx
            vertex = self.getvertex(idx)
            if vertex.getoutdegree() > self._maxoutdegree:
                self._maxoutdegree = vertex.getoutdegree()
                self._maxoutdegreeidx = idx

        else:
            # idx == None, find new max value
            maxoutdegree = NODEGREE
            maxoutdegreeidx = None
            for idx in range(self.getnbofvertices()):
                vertex = self.getvertex(idx)
                if vertex.getoutdegree() > maxoutdegree:
                    maxoutdegree = vertex.getoutdegree()
                    maxoutdegreeidx = idx

            self._maxoutdegree = maxoutdegree
            self._maxoutdegreeidx = maxoutdegreeidx

    def getnbofvertices(self):
        return len(self._vertices)

    def gettotdegree(self):
        return self._totdegree

    def getvertex(self, index):
        return self._vertices[index]

    def addvertex(self, vertex):
        idxnew = self.getnbofvertices()
        self._vertices.append(vertex)
        self._totdegree += vertex.getindegree()
        self._updmaxindegree(idxnew)
        self._updmaxoutdegree(idxnew)

        return self.getnbofvertices() - 1

    def connect(self, indexp, indexq, channel, indexexst=None):
        # connect vertex p to vertex q

        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        if not vertexp.isconnectedto(indexq):
            vertexp.connectto(indexq, channel, indexexst)
            vertexq.connectfrom(indexp)
            self._totdegree += 1
            # compare current maxindegree with the degree of indexq
            self._updmaxindegree(indexq)
            # compare current maxoutdegree with the degree of indexp
            self._updmaxoutdegree(indexp)

    def disconnect(self, indexp, indexq):
        # diconnect the link from vertex p to vertex q

        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        if vertexp.isconnectedto(indexq):
            vertexp.disconnectto(indexq)
            vertexq.disconnectfrom(indexp)
            self._totdegree -= 1
            self._updmaxindegree()
            self._updmaxoutdegree()

    def isconnected(self, indexp, indexq):
        # check if vertex p is connected to vertex q
        return self.getvertex(indexp).isconnectedto(indexq)

    def printinfo(self):
        print "** data **"
        for vertex in self._vertices:
            vertex.printinfo()
        print "** totdegree **"
        print self._totdegree

def __main(argv):
    print "** create vertex p (node, degree): ('p', 0)"
    p = Vertex('p')
    print "** getnode():"
    print p.getnode()
    print "** getindegree():"
    print p.getindegree()
    p.printinfo()
    print "** create vertex q **"
    q = Vertex('q')
    q.printinfo()
    print "** create network **"
    network = Vertices()
    print "** addvertex(p):"
    indexp = network.addvertex(p)
    network.printinfo()
    print "** addvertex(q):"
    indexq = network.addvertex(q)
    network.printinfo()
    print "** connect p to q:"
    network.connect(indexp, indexq, 'p->q')
    network.printinfo()
    print "** create vertex r **"
    r = Vertex('r')
    r.printinfo()
    print "** addvertex(r):"
    indexr = network.addvertex(r)
    network.printinfo()
    print "** connect p to r as an alternative of q:"
    network.connect(indexp, indexr, 'p->r', indexq)
    network.printinfo()
    p.printaltlinks()
    print "** disconnect p to q:"
    network.disconnect(indexp, indexq)
    network.printinfo()
    p.printaltlinks()

if __name__ == "__main__":
    sys.exit(__main(sys.argv))

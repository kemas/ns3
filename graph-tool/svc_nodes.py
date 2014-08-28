# svc_nodes.py
# Data structure for service network.
# The network is a directed network where nodes represent services and links represent dependency between services.
# There are two kinds of dependency: full and partial dependency

import sys

NODEGREE = -999

class AltLinks:
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
            self._ref[idxalt] = [j, 1]

    def delalt(self, idxvertex):
        # delete an idxvertex
        # after deletion, if the same list only has one index, also delete this remaining index
        # idxvertex exists

        # idxvertex is assumed to exist, no checking is needed
        i, j = getidxaltlink(idxvertex)
        # remove from the list of index
        self._ls[i].pop(j)
        # remove from the reference dictionary
        self._ref.pop(idxvertex)
        # check the remaining indices in the same list _ls[i]
        if len(self._ls[i]) == 1:
            # list _ls[i] has only one index, remove the list
            lsidx = self._ls.pop[i]
            # remove the lone idxvertex from the reference dictionary
            self._ref.pop(lsidx[0])

class Vertex:
    # class of Vertex in a directed network

    def __init__(self, node, indegree=0, outdegree=0):
        self._data = [node, indegree, outdegree]
        self._links = []
        self._channels = []
        self._altlinks = AltLinks()
        self._isactive = True

    def isactive(self):
        return self._isactive

    def _deactivate(self):
        self._isactive = False

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

    def getnboflinks(self):
        return len(self._links)

    def getneighboridx(self, index):
        # get the index of neighbors connected to this vertex
        return self._links[index]

    def getlinkidbyidxv(self, idxvertex):
        # get the index of _links that contains idxvertex
        # return None when idxvertex is not found

        found = False
        i = 0
        while not found and i < self.getnboflinks():
            if self.getneighboridx(i) == idxvertex:
                found = True
            else:
                i += 1

        if found:
            return i
        else:
            return None

    def is_connectedto(self, index):
        return self._links.count(index)

    def connectto(self, index, channel, indexexst=None):
        # connect this vertex to the vertex at index
        # if indexexst is given, the vertex at index is an alternate of the vertex at indexexst
        # currently no link from this vertex to the vertex at index
        # connectivity checking is not performed within this function

        # add the link (the index of the vertex)
        self._links.append(index)
        # add the ns3 channel
        self._channels.append(channel)
        # increment the out degree
        self._incroutdegree()

        if indexexst:
            # add the information of alternate links to altlinks
            self._altlinks.addalt(indexexst, index)

    def connectfrom(self):
        # increment the indegree of this vertex because of the incoming edge from the vertex at index
        self._incrindegree()

    def disconnectto(self, index):
        # disconnect link from this vertex to the vertex at index
        # this vertex will be deactivated if no alternative in altlinks 
        # it is assumed no multiple links connected between the same pairs of nodes
        # i.e., self._links has unique member

        # checking the connectivity between this vertex and the vertex at index
        if self.is_connectedto(index):
            # a link to vertex at the index exists, remove it
            idxlink = self.getlinkidbyidxv(index) 
            self._links.pop(idxlink)
            self._channels.pop(idxlink)
            # decrement the out degree
            self._decroutdegree()

            # remove the vertex from altlinks if any
            idxls = self._altlinks.getidxaltlink(index)
            if idxls != None:
                self.getaltlink(idxls[0]).pop(idxls[1])
            else:
                # no alternative, deactivate this vertex
                self._deactivate()

    def disconnectfrom(self):
        # decrement the indegree
        self._decrindegree()

    def printinfo(self):
        print self._data

class Vertices:
    def __init__(self):
        self._data = []
        self._totindegree = 0
        self._totoutdegree = 0
        self._maxindegree = NODEGREE
        self._maxindegreeidx = None
        self._maxoutdegree = NODEGREE
        self._maxoutdegreeidx = None

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
            for idx in range(self.getlength()):
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
            for idx in range(self.getlength()):
                vertex = self.getvertex(idx)
                if vertex.getoutdegree() > maxoutdegree:
                    maxoutdegree = vertex.getoutdegree()
                    maxoutdegreeidx = idx

            self._maxoutdegree = maxoutdegree
            self._maxoutdegreeidx = maxoutdegreeidx

    def getlength(self):
        return len(self._data)

    def gettotindegree(self):
        return self._totindegree

    def gettotoutdegree(self):
        return self._totoutdegree

    def getvertex(self, index):
        return self._data[index]

    def addvertex(self, vertex):
        idxnew = self.getlength()
        self._data.append(vertex)
        self._totindegree += vertex.getindegree()
        self._totoutdegree += vertex.getoutdegree()
        self._updmaxindegree(idxnew)
        self._updmaxoutdegree(idxnew)

        return self.getlength()-1

#    def delvertex(self, index):
#        # delete existing vertex at index
#        # does not deal with connected links and vertices' totdegree
#        self._data.pop(index)

#    def incrvertexdegree(self, index, addby = 1):
#        self.getvertex(index)._incrdegree(addby)
#        self._totdegree += addby
#
#    def decrvertexdegree(self, index, substrby = 1):
#        self.getvertex(index)._decrdegree(substrby)
#        self._totdegree -= substrby

    def linknodes(self, indexp, indexq, channel, indexexst=None):
        # connect vertex p to vertex q

        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        if not vertexp.is_connectedto(indexq):
            vertexp.connectto(indexq, channel, indexexst)
            vertexq.connectfrom()
            self._totindegree += 1
            self._totoutdegree += 1
            # compare current maxindegree with the degree of indexq
            self._updmaxindegree(indexq)
            # compare current maxoutdegree with the degree of indexp
            self._updmaxoutdegree(indexp)

    def disconnectnodes(self, indexp, indexq):
        # diconnect the link from vertex p to vertex q

        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        if vertexp.is_connectedto(indexq):
            vertexp.disconnectto(indexq)
            vertexq.disconnectfrom()
            self._totindegree -= 1
            self._totoutdegree -= 1
            self._updmaxindegree()
            self._updmaxoutdegree()

    def is_connected(self, indexp, indexq):
        # check if vertex p is connected to vertex q
        return self.getvertex(indexp).is_connectedto(indexq)

    def printinfo(self):
        print "**._data **"
        for vertex in self._data:
            vertex.printinfo()
#        print "** totdegree **"
#        print self._totdegree

def __main(argv):
    print "** create vertex p (node, degree): ('p', 0)"
    p = Vertex('p', 0)
    print "** getnode():"
    print p.getnode()
    print "** getindegree():"
    print p.getindegree()
    print "** _incrindegree():"
    p._incrindegree()
    print p.getindegree()
    print "** _incrindegree(2):"
    p._incrindegree(2)
    print p.getindegree()
    print "** _decrindegree():"
    p._decrindegree()
    print p.getindegree()
    print "** decrindgree(2):"
    p._decrindegree(2)
    print p.getindegree()
    print "** printinfo():"
    p.printinfo()
    
    print "** create vertex q **"
    q = Vertex('q', 0)
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
    network.linknodes(indexp, indexq, 'p->q')
    network.printinfo()
    print "** disconnect p to q:"
    network.disconnectnodes(indexp, indexq)
    network.printinfo()

if __name__ == "__main__":
    sys.exit(__main(sys.argv))

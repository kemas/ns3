import sys

NODEGREE = -999

class Vertex:
    def __init__(self, node, degree = 0):
        self._data = [node, degree]
        self._links = []
        self._channels = []

    def getnode(self):
        return self._data[0]

    def getdegree(self):
        return self._data[1]

    def _incrdegree(self, addby = 1):
        self._data[1] += addby

    def _decrdegree(self, substrby = 1):
        self._data[1] -= substrby

    def getchannel(self, index):
        return self._channels[index]

    def connecto(self, index, channel):
        self._links.append(index)
        self._channels.append(channel)
        self._incrdegree()

    def disconnectfrom(self, index):
        # disconnect link from a vertex
        # it is assumed no multiple links connected between the same pairs of nodes
        # therefore, self._links has unique member

        if self.is_connectedto(index):
            # link to vertex-index is exist, remove
            linkidx = self.getlinkid(index) 
            self._links.pop(linkidx)
            self._channels.pop(linkidx)
            # decrement degree
            self._decrdegree()

    def getnboflinks(self):
        return len(self._links)

    def getneighboridx(self, index):
        return self._links[index]

    def getlinkid(self, index):
        # get the index of _links that contains index (the index of vertex)
        # index is assumed to be existing in _links
        return self._links.index(index)

    def is_connectedto(self, index):
        return self._links.count(index)

    def printinfo(self):
        print self._data

class Vertices:
    def __init__(self):
        self._data = []
        self.totdegree = 0
        self.maxdegree = NODEGREE
        self.maxdegreeidx = None

    def _updmaxdegree(self, idx=None):
        if idx != None:
            vertex = self.getvertex(idx)
            if vertex.getdegree() > self.maxdegree:
                self.maxdegree = vertex.getdegree()
                self.maxdegeeidx = idx
        else:
            # idx == None, find new max value
            maxdegree = NODEGREE
            maxdegreeidx = None
            for idx in range(self.getlength()):
                vertex = self.getvertex(idx)
                if vertex.getdegree() > maxdegree:
                    maxdegree = vertex.getdegree()
                    maxdegreeidx = idx

            self.maxdegree = maxdegree
            self.maxdegreeidx = maxdegreeidx

    def getlength(self):
        return len(self._data)

    def gettotdegree(self):
        return self.totdegree

    def getvertex(self, index):
        return self._data[index]

    def addvertex(self, vertex):
        idxnew = self.getlength()
        self._data.append(vertex)
        self.totdegree += vertex.getdegree()
        self._updmaxdegree(idxnew)

        return self.getlength()-1
    
#    def delvertex(self, index):
#        # delete existing vertex at index
#        # does not deal with connected links and vertices' totdegree
#        self._data.pop(index)

#    def incrvertexdegree(self, index, addby = 1):
#        self.getvertex(index)._incrdegree(addby)
#        self.totdegree += addby
#
#    def decrvertexdegree(self, index, substrby = 1):
#        self.getvertex(index)._decrdegree(substrby)
#        self.totdegree -= substrby

    def linknodes(self, indexp, indexq, channel):
        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        # links are assumed to be undirected
        # link existence is only checked from one side
        if not vertexp.is_connectedto(indexq):
            vertexp.connecto(indexq, channel)
            vertexq.connecto(indexp, channel)
            self.totdegree += 2 # add 2 degrees in total (1 from each side)
            self._updmaxdegree(indexp)
            self._updmaxdegree(indexq)

    def disconnectnodes(self, indexp, indexq):
        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        # links are assumed to be undirected
        # link existence is only checked from one side
        if vertexp.is_connectedto(indexq):
            vertexp.disconnectfrom(indexq)
            vertexq.disconnectfrom(indexp)
            self.totdegree -= 2 # decrement 2 degrees in total (1 from each side)
            self._updmaxdegree()
        
    def is_connected(self, indexp, indexq):
        # links are assumed to be undirected
        # link existence is only checked from one side

        return self.getvertex(indexp).is_connectedto(indexq)

    def printinfo(self):
        print "**._data **"
        for vertex in self._data:
            vertex.printinfo()
        print "** totdegree **"
        print self.totdegree

def __main(argv):
    print "** vertex (node, degree): ('node1', 0)"
    vertex = Vertex('node1', 0)
    print "** getnode():"
    print vertex.getnode()
    print "** getdegree():"
    print vertex.getdegree()
#    print "** _incrdegree():"
#    vertex._incrdegree()
#    print vertex.getdegree()
#    print "** _incrdegree(2):"
#    vertex._incrdegree(2)
#    print vertex.getdegree()
#    print "** _decrdegree():"
#    vertex._decrdegree()
#    print vertex.getdegree()
#    print "** decrdgree(2):"
#    vertex._decrdegree(2)
#    print vertex.getdegree()
    print "** printinfo():"
    
    print "** create vertices **"
    vertices = Vertices()
    print "** addvertex(vertex):"
    vertices.addvertex(vertex)
    vertices.printinfo()
    print "** addvertex(vertex):"
    vertices.addvertex(Vertex('node2', 0))
    vertices.printinfo()
#    print "** incrvertexdegree(0):"
#    vertices.incrvertexdegree(0)
#    vertices.printinfo()
#    print "** incrvertexdegree(1,3):"
#    vertices.incrvertexdegree(1,3)
#    vertices.printinfo()
#    print "** decrvertexdegree(0):"
#    vertices.decrvertexdegree(0)
#    vertices.printinfo()
#    print "** decrvertexdegree(1,3):"
#    vertices.decrvertexdegree(1,3)
#    vertices.printinfo()

if __name__ == "__main__":
    sys.exit(__main(sys.argv))

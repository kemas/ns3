# svc_nodes.py
# Data structure for service network.
# The network is a directed network where vertex represent services and links represent dependency between services.
# There are two kinds of dependency: full and partial dependency

#import pdb
import sys
import analyzer

NODEGREE = -999

class AltLinks:
    # Class of list of list of vertex indices
    # Two vertices can substitute each other if the indices are listed in the same list of indices

    def __init__(self):
        self._ls = [] # list of list of links
        self._ref = {} # reference dictionary {p: [a, b], ...}
                       # p == _ls[a][b]
        #self._altlength = [] # list of list length

    def getidxaltlink(self, idxvertex):
        # get the index of idxvertex in _ls

        if self._ref.has_key(idxvertex):
            return self._ref[idxvertex]
        else:
            return None

    def addalt(self, idxvertex, idxalt):
        # add an alternative of idxvertex
        # idxvertex may have been added to altlinks (return 1)
        # idxalt has not been added to altlinks (return 2)

        #pdb.set_trace()
        idxls = self.getidxaltlink(idxvertex)
        if idxls != None:
            # idxls != None, list containing idxvertex exists
            # add idxalt to the same list as idxvertex
            i = idxls[0]
            self._ls[i].append(idxalt)
            # add the indices of idxalt to the reference dictionary _ref
            self._ref[idxalt] = [i, len(self._ls[i]) - 1]

            return 1
        else:
            # idxvertex has not been added
            # add both idvertex and idxalt
            self._ls.append([idxvertex, idxalt])
            i = len(self._ls) - 1
            # add to the reference dictionary _ref
            self._ref[idxvertex] = [i, 0]
            self._ref[idxalt] = [i, 1]

            return 2

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

            # update the reference value
            for k in range(i, len(self._ls)):
                for idxvertex in self._ls[k]:
                    self._ref[idxvertex][0] = self._ref[idxvertex][0] - 1
        else:
            # there are more than one remaining indices
            # update the reference value
            for idxvertex in self._ls[i][j:]:
                self._ref[idxvertex][1] = self._ref[idxvertex][1] - 1
#            for k in range(j, len(self._ls[i])):
#                idxvertex = self._ls[i][k]
#                self._ref[idxvertex] = [i, k]

    def delaltbyidxvertex(self, idxvertex):
        # remove idxvertex
        # after deletion, if the same list only has one index, also delete this remaining index
        # idxvertex exists

        # idxvertex is assumed to exist, no checking is needed
        i, j = getidxaltlink(idxvertex)
        self.delaltbyidxls(i, j)

    def printinfo(self):
        print "** altlinks printinfo"
        print self._ls
        print self._ref

class Vertex:
    # class of Vertex in a directed network

    def __init__(self, node, indegree=0, outdegree=0):
        self._data = [node, indegree, outdegree]
        self._outlinks = [] # outgoing links
        self._inlinks = [] # incoming links
        self._channels = []
        self._altlinks = AltLinks() # list of list of vertex indices connected by outgoing links
        self._isactive = True
        self._nbofmandlinks = 0
        self._nbofaltlinks = 0
        self._depth = 0 # initial depth is zero, because no outlink
        self._meandepth = 0.0 # (1 + meandepth of all connected nodes) / number of connected nodes
        self._maxdepthidx = None # the vertex index listed in _outlinks and having the highest depth

    def addtovertices(self, vertices, index):
        self.vertices = vertices
        self.index = index

    def isactive(self):
        return self._isactive

    def deactivate(self):
        # set active status to False
        self._isactive = False
        # remove from list of active vertices
        self.vertices.deactivate(self)

    def getnode(self):
        return self._data[0]

    def getindegree(self):
        return self._data[1]

    def getoutdegree(self):
        return self._data[2]

    def getnbofmandlinks(self):
        return self._nbofmandlinks

    def getnbofaltlinks(self):
        return self._nbofaltlinks

    def getdepth(self):
        return self._depth

    def getmeandepth(self):
        return self._meandepth

    def getmaxdepthidx(self):
        return self._maxdepthidx

    def upddepth(self, depth, meandepth, maxdepthidx):
        self._depth = depth
        self._meandepth = meandepth

        if maxdepthidx:
            self._maxdepthidx = maxdepthidx

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

    # this is redundant with self._data[2]
    def getnbofoutlinks(self):
        return len(self._outlinks)

    # this is redundant with self._data[1]
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

    def isconnectedfrom(self, index):
        return self._inlinks.count(index)

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

        if indexexst != None:
            # add the information of alternate links to altlinks
            self._nbofaltlinks += self._altlinks.addalt(indexexst, index)
        else:
            self._nbofmandlinks += 1

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
                self._nbofaltlinks -= 1
            else:
                # no alternative, deactivate this vertex
                # all incoming and outgoing links will be disconnected
                self._nbofmandlinks -= 1
                # deactivation is not needed, handled in fail()
                # is it necessary to check isactive?
                #if self.isactive():
                #    print "** deactivate aft disc"
                #    self.deactivate()

    def disconnectfrom(self, index):
        # disconnect another vertex from this vertex (connected by inlink)

        # checking the connectivity between this vertex and the vertex at index
        if self.isconnectedfrom(index):
            # get the link id of the vertex
            idxlink = self.getinlinkbyver(index) 
            # remove the vertex from inlinks
            self._inlinks.pop(idxlink)
            # decrement the indegree
            self._decrindegree()

    def printinfo(self):
        print "** vertex printinfo"
        print "Id      : %i" % self._data[0].GetId()
        print "data    : "+ str(self._data)
        print "status  : "+ str(self.isactive())
        print "inlinks : "+ str(self._inlinks)
        print "outlinks: "+ str(self._outlinks)
        self._altlinks.printinfo()

    def printaltlinks(self):
        print self._altlinks._ls

class Vertices:
    def __init__(self):
        self._vertices = []
        self._activevert = []
        self._totdegree = 0 # the sum of the number of indegree for all vertices
                            # this also the same as the sum of the number of outdegree
        self._maxindegree = NODEGREE
        self._maxindegreeidx = None
        self._maxoutdegree = NODEGREE
        self._maxoutdegreeidx = None
        self._maxmandlinks = NODEGREE
        self._maxmandlinksidx = None
        self._maxaltlinks = NODEGREE
        self._maxaltlinksidx = None
        self._maxdepth = 0
        self._maxdepthidx = None
#        self._avgdepth = 0.0
        self._maxmeandepth = 0.0
        self._maxmeandepthidx = None
#        self._avgmeandepth = 0.0
        self._totmandlinks = 0
        self._totaltlinks = 0
        self._nbofremoved = 0
        self._nboffail = 0

        self.analyzer = analyzer.Analyzer()

        ###!!!
        #self.countconnect = 0

    def getmaxindegree(self):
        return self._maxindegree

    def getmaxindegreeidx(self):
        return self._maxindegreeidx

    def getmaxoutdegree(self):
        return self._maxoutdegree

    def getmaxoutdegreeidx(self):
        return self._maxoutdegreeidx

    def getnbofvertices(self):
        return len(self._vertices)

    def getnbofactive(self):
        return len(self._activevert)

    def gettotdegree(self):
        return self._totdegree

    def gettotmandlinks(self):
        return self._totmandlinks

    def gettotaltlinks(self):
        return self._totaltlinks

    def getmaxmandlinks(self):
        return self._maxmandlinks
    
    def getmaxmandlinksidx(self):
        return self._maxmandlinksidx
    
    def getmaxaltlinks(self):
        return self._maxaltlinks

    def getmaxaltlinksidx(self):
        return self._maxaltlinksidx

    def getmaxdepth(self):
        return self._maxdepth

    def getmaxdepthidx(self):
        return self._maxdepthidx

#    def getavgdepth(self):
#        return self._avgdepth

#    def setavgdepth(self, avgdepth):
#        self._avgdepth = avgdepth

    def getmaxmeandepth(self):
        return self._maxmeandepth

    def getmaxmeandepthidx(self):
        return self._maxmeandepthidx

#    def getavgmeandepth(self):
#        return self._avgmeandepth

    def getnbofremoved(self):
        return self._nbofremoved

    def getnboffail(self):
        return self._nboffail

    def getindexbyact(self, actidx):
        return self._activevert[actidx]

    def _updallstats(self, idxsource=None, idxtarget=None, ismandincl=True, isaltincl=True, isdepthincl=True):
        # update values of maxindegree, maxoutdegree, maxmandlinks, maxaltlinks
        # and their corresponding idx (e.g. maxindegreeidx)
        # idxsource is the vertex index where outgoing links are connected from
        # idxtarget is the vertex index where incoming links are connected to

        if idxsource != None or idxtarget != None:

            if idxsource != None:
                vertex = self.getvertex(idxsource)

                if vertex.getoutdegree() > self._maxoutdegree:
                    self._maxoutdegree = vertex.getoutdegree()
                    self._maxoutdegreeidx = idxsource

                if ismandincl and vertex.getnbofmandlinks() > self._maxmandlinks:
                    self._maxmandlinks = vertex.getnbofmandlinks()
                    self._maxmandlinksidx = idxsource

                if isaltincl and vertex.getnbofaltlinks() > self._maxaltlinks:
                    self._maxaltlinks = vertex.getnbofaltlinks()
                    self._maxaltlinksidx = idxsource

                if isdepthincl and vertex.getdepth() > self._maxdepth:
                    self._maxdepth = vertex.getdepth()
                    self._maxdepthidx = idxsource

                if isdepthincl and vertex.getmeandepth() > self._maxmeandepth:
                    self._maxmeandepth = vertex.getmeandepth()
                    self._maxmeandepthidx = idxsource

            if idxtarget != None:
                vertex = self.getvertex(idxtarget)

                if vertex.getindegree() > self._maxindegree:
                    self._maxindegree = vertex.getindegree()
                    self._maxindegreeidx = idxtarget

        else:
            # idxsource and idxtarget are None
            # compare all existing nodes to get the stats

            maxindegree = NODEGREE
            maxindegreeidx = None
            maxoutdegree = NODEGREE
            maxoutdegreeidx = None
            if ismandincl:
                maxmandlinks = NODEGREE
                maxmandlinksidx = None
            if isaltincl:
                maxaltlinks = NODEGREE
                maxaltlinksidx = None

            for idx in range(self.getnbofvertices()):
                vertex = self.getvertex(idx)

                if vertex.getindegree() > maxindegree:
                    maxindegree = vertex.getindegree()
                    maxindegreeidx = idx

                if vertex.getoutdegree() > maxoutdegree:
                    maxoutdegree = vertex.getoutdegree()
                    maxoutdegreeidx = idx

                if ismandincl and vertex.getnbofmandlinks() > maxmandlinks:
                    maxmandlinks = vertex.getnbofmandlinks()
                    maxmandlinksidx = idx

                if isaltincl and vertex.getnbofaltlinks() > maxaltlinks:
                    maxaltlinks = vertex.getnbofaltlinks()
                    maxaltlinksidx = idx

                if isdepthincl and vertex.getdepth() > self._maxdepth:
                    self._maxdepth = vertex.getdepth()
                    self._maxdepthidx = idx

                if isdepthincl and vertex.getmeandepth() > self._maxmeandepth:
                    self._maxmeandepth = vertex.getmeandepth()
                    self._maxmeandepthidx = idx

            self._maxindegree = maxindegree
            self._maxindegreeidx = maxindegreeidx
            self._maxoutdegree = maxoutdegree
            self._maxoutdegreeidx = maxoutdegreeidx
            if ismandincl:
                self._maxmandlinks = maxmandlinks
                self._maxmandlinksidx = maxmandlinksidx
            if isaltincl:
                self._maxaltlinks = maxaltlinks
                self._maxaltlinksidx = maxaltlinksidx

#    def _updmaxindegree(self, idx=None):
#        if idx != None:
#            # only compares current maxindegree with the degree of the vertex at idx
#            vertex = self.getvertex(idx)
#            if vertex.getindegree() > self._maxindegree:
#                self._maxindegree = vertex.getindegree()
#                self._maxindegreeidx = idx
#
#        else:
#            # idx == None, find new max value
#            maxindegree = NODEGREE
#            maxindegreeidx = None
#            for idx in range(self.getnbofvertices()):
#                vertex = self.getvertex(idx)
#                if vertex.getindegree() > maxindegree:
#                    maxindegree = vertex.getindegree()
#                    maxindegreeidx = idx
#
#            self._maxindegree = maxindegree
#            self._maxindegreeidx = maxindegreeidx
#
#    def _updmaxoutdegree(self, idx=None):
#        if idx != None:
#            # only compares current maxoutdegree with the degree of the vertex at idx
#            vertex = self.getvertex(idx)
#            if vertex.getoutdegree() > self._maxoutdegree:
#                self._maxoutdegree = vertex.getoutdegree()
#                self._maxoutdegreeidx = idx
#
#        else:
#            # idx == None, find new max value
#            maxoutdegree = NODEGREE
#            maxoutdegreeidx = None
#            for idx in range(self.getnbofvertices()):
#                vertex = self.getvertex(idx)
#                if vertex.getoutdegree() > maxoutdegree:
#                    maxoutdegree = vertex.getoutdegree()
#                    maxoutdegreeidx = idx
#
#            self._maxoutdegree = maxoutdegree
#            self._maxoutdegreeidx = maxoutdegreeidx
#
#    def _updmaxmandlinks(self, idx=None):
#        if idx != None:
#            # only compares current maxmandlinks with the one of the vertex at idx
#            vertex = self.getvertex(idx)
#            if vertex.getnbofmandlinks() > self._maxmandlinks:
#                self._maxmandlinks = vertex.getnbofmandlinks()
#                self._maxmandlinksidx = idx
#
#        else:
#            # idx == None, find new max value
#            maxmandlinks = NODEGREE
#            maxmandlinksidx = None
#            for idx in range(self.getnbofvertices()):
#                vertex = self.getvertex(idx)
#                if vertex.getnbofmandlinks() > maxmandlinks:
#                    maxmandlinks = vertex.getnbofmandlinks()
#                    maxmandlinksidx = idx
#
#            self._maxmandlinks = maxmandlinks
#            self._maxmandlinksidx = maxmandlinksidx
#
#    def _updmaxaltlinks(self, idx=None):
#        if idx != None:
#            # only compares current maxaltlinks with the one of the vertex at idx
#            vertex = self.getvertex(idx)
#            if vertex.getnbofaltlinks() > self._maxaltlinks:
#                self._maxaltlinks = vertex.getnbofaltlinks()
#                self._maxaltlinksidx = idx
#
#        else:
#            # idx == None, find new max value
#            maxaltlinks = NODEGREE
#            maxaltlinksidx = None
#            for idx in range(self.getnbofvertices()):
#                vertex = self.getvertex(idx)
#                if vertex.getnbofaltlinks() > maxaltlinks:
#                    maxaltlinks = vertex.getnbofaltlinks()
#                    maxaltlinksidx = idx
#
#            self._maxaltlinks = maxaltlinks
#            self._maxaltlinksidx = maxaltlinksidx
#
    def getvertex(self, index):
        return self._vertices[index]

    def addvertex(self, vertex):
        # add a newly created vertex
        # currently not connected to existing vertex
        # no need to update stats

        idxnew = self.getnbofvertices() # new vertex will be appended at the end of the list
        self._vertices.append(vertex)
        vertex.addtovertices(self, idxnew)
        self._activevert.append(idxnew)
        #self._totdegree += vertex.getindegree()

        return idxnew

    def deactivate(self, vertex):
        idx = vertex.index
        self._activevert.pop(self._activevert.index(idx))

    def connect(self, indexp, indexq, channel, indexexst=None):
        # connect vertex p to vertex q

        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        if not vertexp.isconnectedto(indexq):
            poutlinks = vertexp.getnbofoutlinks()

            vertexp.connectto(indexq, channel, indexexst)
            vertexq.connectfrom(indexp)
            self._totdegree += 1

            # update depth vertexp
            depth_p = vertexp.getdepth()
            depth_q = vertexq.getdepth()

            meandepth = (poutlinks * vertexp.getmeandepth() + vertexq.getmeandepth() + 1) / (poutlinks + 1)
            #if depth_p == 0:
            #    vertexp.upddepth(1, indexq)
            if depth_q >= depth_p:
                depth_p = depth_q + 1
            vertexp.upddepth(depth_p, meandepth, indexq)

            # update stats
            self._updallstats(indexp, indexq, ismandincl = (indexexst == None), isaltincl = (indexexst != None))

        if indexexst != None:
            self._totaltlinks += 1
        else:
            self._totmandlinks += 1

        ###!!!debug, why out/inlinks != out/indegree
        # because the snapshot value is pass by reference 
        #print "**"
        #print vertexp._outlinks
        #print vertexp._data
        #print vertexq._inlinks
        #print vertexq._data

        ###!!!
        #self.countconnect += 1

    def disconnect(self, indexp, indexq, isupddepth=False):
        # diconnect the link from vertex p to vertex q
        # not the opposite (from vertex q to vertex p)

        vertexp = self.getvertex(indexp)
        vertexq = self.getvertex(indexq)

        if vertexp.isconnectedto(indexq):
            nbofmandlinks = vertexp.getnbofmandlinks()
            nbofaltlinks = vertexp.getnbofaltlinks()

            vertexp.disconnectto(indexq)
            vertexq.disconnectfrom(indexp)
            self._totdegree -= 1
            self._updallstats()

            # update depth vertexp
            if isupddepth and vertexp.getmaxdepthidx() == indexq:
                # search new maxdepth
                self.upddepth(indexp)

            self._totmandlinks -= nbofmandlinks - vertexp.getnbofmandlinks()
            self._totaltlinks -= nbofaltlinks - vertexp.getnbofaltlinks()

    def upddepth(self, indexp):
        # update the depth of vertex at indexp

        vertexp = self.getvertex(indexp)

        vpmaxdepth = 0; vpmaxdepthidx = None
        totmeandepth = 0.0
        for i in vertexp.itroutlinks():
            idepth = self.getvertex(i).getdepth()

            if idepth >= vpmaxdepth:
                vpmaxdepth = idepth + 1
                vpmaxdepthidx = i

            totmeandepth += self.getvertex(i).getmeandepth() + 1

        meandepth = 0.0
        if vertexp.getnbofoutlinks():
            # nbofoutlinks > 0
            meandepth = totmeandepth / float(vertexp.getnbofoutlinks())

        vertexp.upddepth(vpmaxdepth, meandepth, vpmaxdepthidx)

    def isconnected(self, indexp, indexq):
        # check if vertex p is connected to vertex q
        return self.getvertex(indexp).isconnectedto(indexq)

    def fail(self, index, depth=0):
        # deactivate a node and propagate the failure 
        # to the other fully dependent nodes

        self._nboffail += 1
        #print "_nboffail "+ str(self._nboffail)

        vertex = self.getvertex(index)
        ## deactivate
        #vertex.deactivate()

#        # verbose
#        print "** On fail node **"
#        print "index "+ str(index)
#        vertex.printinfo()

        # propagate failure
        #lsdepth = []
        #inlinks = vertex._inlinks[:] # copy values
        #for idxneighbor in inlinks:
        while len(vertex._inlinks):
            idxneighbor = vertex._inlinks[0]
            neighbor = self.getvertex(idxneighbor)
            #print "in-neighbor "+ str(idxneighbor)
            #if not neighbor.ispartiallydepend(index) and neighbor.isactive():
            if not neighbor.ispartiallydepend(index):
                # neighbor fully depends on vertex at index
                # propagate the failure
                #print "## cascade failure"
                self.fail(idxneighbor)
                #lsdepth.append(self.fail(idxneighbor, depth))
            else:
                # disconnect the other incoming links
                #print "## disconnect inlink"
                self.disconnect(idxneighbor, index)

        #outlinks = vertex._outlinks[:] # copy values
        # disconnect to all outgoing links
        #for idxneighbor in outlinks:
        while len(vertex._outlinks):
            idxneighbor = vertex._outlinks[0]
            #print "out-neighbor "+ str(idxneighbor)
            self.disconnect(index, idxneighbor)

#        # disconnect from all incoming links
#        for idxneighbor in vertex._inlinks:
#            self.disconnect(idxneighbor, index)
#            #self.disconnect(index, idxneighbor)

        # deactivate
        vertex.deactivate()

#        ###
#        if lsdepth:
#            return max(lsdepth) + 1
#        else:
#            return 1    

    def dofail(self, index):
        self._nbofremoved += 1
        self.fail(index)
        #print self.fail(index)

        # verbose
        #self.printinfo()

    def printinfo(self):
        print "=========================="
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


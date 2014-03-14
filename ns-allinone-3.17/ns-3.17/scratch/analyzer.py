# analyzer.py
# Data structure and routines for analyzing the simulation result

import numpy as np
import matplotlib.pyplot as plt
import json

class Analyzer:
    def __init__(self):
        self.lastid = -1
        self.nodescreated = []
        self.nodesremoved = []
        self.nodesfail = []
        self.linkscreated = []
        self.linksfail = []
        self.altcreated = []
        self.altfail = []
        self.mandcreated = []
        self.mandfail = []

    def advancetime(self):
        # advance to the next timestep
        # append an element to each list

        if self.lastid >= 0:
            # not a first element
            self.nodescreated.append(self.nodescreated[self.lastid])
            self.nodesremoved.append(self.nodesremoved[self.lastid])
            self.nodesfail.append(self.nodesfail[self.lastid])
            self.linkscreated.append(self.linkscreated[self.lastid])
            self.linksfail.append(self.linksfail[self.lastid])
            self.altcreated.append(self.altcreated[self.lastid])
            self.altfail.append(self.altfail[self.lastid])
            self.mandcreated.append(self.mandcreated[self.lastid])
            self.mandfail.append(self.mandfail[self.lastid])

        else:
            # first element, add 0
            self.nodescreated.append(0)
            self.nodesremoved.append(0)
            self.nodesfail.append(0)
            self.linkscreated.append(0)
            self.linksfail.append(0)
            self.altcreated.append(0)
            self.altfail.append(0)
            self.mandcreated.append(0)
            self.mandfail.append(0)

        self.lastid += 1

    def getcreatednodes(self):
        return self.nodescreated[self.lastid]

    def getnodesremoved(self):
        return self.nodesremoved[self.lastid]

    def getnodesfail(self):
        return self.nodesfail[self.lastid]

    def getlinkscreated(self):
        return self.linkscreated[self.lastid]

    def getlinksfail(self):
        return self.linksfail[self.lastid]

    def getaltcreated(self):
        return self.altcreated[self.lastid]

    def getaltfail(self):
        return self.altfail[self.lastid]

    def getmandcreated(self):
        return self.mandcreated[self.lastid]

    def getmandfail(self):
        return self.mandfail[self.lastid]

    def addnodes(self, n):
        self.nodescreated[self.lastid] = n

    def removenodes(self, n):
        self.nodesremoved[self.lastid] = n

    def failnodes(self, n):
        self.nodesfail[self.lastid] = n

    def createlinks(self, n):
        self.linkscreated[self.lastid] = n

    def faillinks(self, n):
        self.linksfail[self.lastid] = n

    def createalts(self, n):
        self.createlinks(n)
        self.altcreated[self.lastid] = n

    def failalts(self, n):
        self.faillinks(n)
        self.altfail[self.lastid] = n

    def createmands(self, n):
        self.createlinks(n)
        self.mandcreated[self.lastid] = n

    def failmands(self, n):
        self.faillinks(n)
        self.mandfail[self.lastid] = n

    def grow(self, nodes, mands, alts):
        self.advancetime()
        self.addnodes(nodes)
        self.createmands(mands)
        self.createalts(alts)

    def fail(self, removed, fail, mands, alts):
        self.advancetime()
        self.removenodes(removed)
        self.failnodes(fail)
        self.failmands(mands)
        self.failalts(alts)

    def plotfailure(self):
        # nodes removal
        found = False; i = 0
        while not found and i < len(self.nodesremoved):
            if self.nodesremoved[i] > 0:
                found = True;
            else:
                i += 1

        if not found:
            return

        x1 = self.nodesremoved[i:]
        y1 = self.nodesfail[i:]

        x2 = x1
        y2 = x1
        plt.plot(x1, y1, 'bo', x2, y2, 'r-')

        plt.show()

    def savetofile(self, filename='svcsim.json', isall=False, isnodescreated=True, isnodesremoved=True, isnodesfail=True, islinkscreated=True, islinksfail=True, isaltcreated=True, isaltfail=True, ismandcreated=True, ismandfail=True):
        obj = {}
        if isall or isnodescreated:
            obj['nodescreated'] = self.nodescreated
        if isall or isnodesremoved:
            obj['nodesremoved'] = self.nodesremoved
        if isall or isnodesfail:
            obj['nodesfail'] = self.nodesfail
        if isall or islinkscreated:
            obj['linkscreated'] = self.linkscreated
        if isall or islinksfail:
            obj['linksfail'] = self.linksfail
        if isall or isaltcreated:
            obj['altcreated'] = self.altcreated
        if isall or isaltfail:
            obj['altfail'] = self.altfail
        if isall or ismandcreated:
            obj['mandcreated'] = self.mandcreated
        if isall or ismandfail:
            obj['mandfail'] = self.mandfail

        f = open(filename, 'w')
        try:
            json.dump(obj, f)
        finally:
            f.close()


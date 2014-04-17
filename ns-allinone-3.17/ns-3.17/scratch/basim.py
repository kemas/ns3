# -*-  Mode: Python; -*-
#  Copyright (c) 2013 Ishida & Matsubara Lab., Kyoto University
# 
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License version 2 as
#  published by the Free Software Foundation;
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# 
#  Authors: Kemas Muslim Lhaksmana <kemas.muslim@ai.soc.i.kyoto-uc.ac.jp>
#----------------------------------------------------------------------------
# basim.py
# A simulation of a scale free network based on Barabasi-Albert (BA) model
# Created   : 27/8/2013
# Modified  :
#----------------------------------------------------------------------------

import sys
import random

import ns.applications
import ns.core
import ns.visualizer
import ns.network
import ns.point_to_point
try:
    import ns.visualizer
except ImportError:
    pass
import sf_nodes
import sf_routines
import bamodel

MAX_M0 = 100
MAX_MADD = 100
TIME = 100
MAX_TIME = 100000
FREQ = 1
MAX_FREQ = 10

def main(argv):
    cmd = ns.core.CommandLine()

    cmd.m0 = None
    cmd.AddValue("m0", "Initial (small) number of nodes")

    cmd.m_add = None
    cmd.AddValue("m_add", "Number of links to be connected to a new node in every timestep (m_add <= m0)")

    cmd.time = None
    cmd.AddValue("time", "How long (seconds) the network will be growing")

    cmd.freq = None
    cmd.AddValue("freq", "How many times m_add nodes will be added to the network for each second")

    cmd.Parse(argv)

    if cmd.m0 is None:
        m0 = bamodel.M0
    else:
        m0 = int(cmd.m0)
        if m0 > MAX_M0:
            print "Invalid argument: m0 should not be higher than %d" % MAX_M0
            sys.exit()

    if cmd.m_add is None:
        m_add = bamodel.M_ADD
    else:
        m_add = int(cmd.m_add)
        if m_add > m0:
            print "Invalid argument: m_add should not be higher than m0"
            sys.exit()
        elif m_add > MAX_MADD:
            print "Invalid argument: m_add should not be higher than %d" % MAX_MADD
            sys.exit()

    if cmd.time is None:
        time = TIME
    else:
        time = int(cmd.time)
        if time > MAX_TIME:
            print "Invalid argument: time should not be higher than %d" % MAX_TIME
            sys.exit()

    if cmd.freq is None:
        freq = FREQ
    else:
        freq = int(cmd.freq)
        if freq > MAX_FREQ:
            print "Invalid argument: freq should not be higher than %d" % MAX_FREQ
            sys.exit()

    vertices = sf_nodes.Vertices()
    bamodel.initnodes(vertices, m0)

    step = time * freq
    if step >= 10000:
        lbinsbase = 1.2
    elif step >= 1000:
        lbinsbase = 1.1
    elif step >= 100:
        lbinsbase = 1.05
    else:
        lbinsbase = 1.01

    #ns.core.Simulator.Stop(ns.core.Seconds(30.0))
    for i in range(time):
        for j in range(freq):
            ns.core.Simulator.Schedule(ns.core.Seconds(i), bamodel.grow, vertices, m_add)
    #ns.core.Simulator.Schedule(ns.core.Seconds(time+1), sf_routines.drawloglogdist, vertices, lbinsbase, True)
    ns.core.Simulator.Schedule(ns.core.Seconds(time+1), sf_routines.drawhistogram, vertices, 100)

    ns.core.Simulator.Stop(ns.core.Seconds(time + 2))
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))


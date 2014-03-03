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
# asim.py
# A simulation of a scale free network based on Chen-Shi A model
# Created   : 30/8/2013
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
import amodel

MAX_ALPHA = 10
MAX_M0 = 100
MAX_MADD = 100
MAX_LINKADD = 100
MAX_LINKREWIRE = 100
STEP = 10
MAX_STEP = 10000

def main(argv):
    cmd = ns.core.CommandLine()

    cmd.alpha = None
    cmd.AddValue("alpha", "Initial attractiveness value")

    cmd.m0 = None
    cmd.AddValue("m0", "Initial (small) number of nodes")

    cmd.m_add = None
    cmd.AddValue("m_add", "The number of links to be connected to a new node in every timestep")

    cmd.l_add = None
    cmd.AddValue("l_add", "The number of links to be added in every timestep")

    cmd.l_rewire = None
    cmd.AddValue("l_rewire", "The number of links to be rewired in every timestep")

    cmd.step = None
    cmd.AddValue("step", "How many times m_add nodes will be added to the network")

    cmd.Parse(argv)

    if cmd.alpha is None:
        alpha = amodel.ALPHA
    else:
        alpha = int(cmd.alpha)
        if alpha > MAX_ALPHA:
            print "Invalid argument: alpha should not be higher than %d" % MAX_ALPHA
            sys.exit()

    if cmd.m0 is None:
        m0 = amodel.M0
    else:
        m0 = int(cmd.m0)
        if m0 > MAX_M0:
            print "Invalid argument: m0 should not be higher than %d" % MAX_M0
            sys.exit()
        elif m0 < 2:
            print "Invalid argument: m0 should be at least 2"
            sys.exit()

    if cmd.m_add is None:
        m_add = amodel.M_ADD
    else:
        m_add = int(cmd.m_add)
        if m_add > m0:
            print "Invalid argument: m_add should not be higher than m0"
            sys.exit()
        elif m_add > MAX_MADD:
            print "Invalid argument: m_add should not be higher than %d" % MAX_MADD
            sys.exit()

    if cmd.l_add is None:
        l_add = amodel.L_ADD
    else:
        l_add = int(cmd.l_add)
        if l_add > MAX_LINKADD:
            print "Invalid argument: l_add should not be higher than %d" % MAX_LINKADD
            sys.exit()
    
    if cmd.l_rewire is None:
        l_rewire = amodel.L_REWIRE
    else:
        l_rewire = int(cmd.l_rewire)
        if l_rewire > MAX_LINKREWIRE:
            print "Invalid argument: l_rewire should not be higher than %d" % MAX_LINKREWIRE
            sys.exit()
    
    if cmd.step is None:
        step = STEP
    else:
        step = int(cmd.step)
        if step > MAX_STEP:
            print "Invalid argument: step should not be higher than %d" % MAX_STEP
            sys.exit()

    # initialize the network with m0 nodes
    vertices = sf_nodes.Vertices()
    amodel.initnodes(vertices, m0)

    #step = time * freq
    if step >= 10000:
        lbinsbase = 1.2
    elif step >= 1000:
        lbinsbase = 1.1
    elif step >= 100:
        lbinsbase = 1.05
    else:
        lbinsbase = 1.01

    for i in range(step):
        ns.core.Simulator.Schedule(ns.core.Seconds(i), amodel.grow, vertices, alpha, l_add, m_add, l_rewire)
    ns.core.Simulator.Schedule(ns.core.Seconds(step + 1), sf_routines.drawloglogdist, vertices, lbinsbase, True)

    ns.core.Simulator.Stop(ns.core.Seconds(step + 2))
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

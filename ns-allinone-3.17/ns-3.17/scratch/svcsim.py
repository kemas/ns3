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
# svcsim.py
# A simulation of a scale free service network
# Created   : 2014/2/26
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
import svc_nodes
import svcmodel
import svc_routines

MAX_MINIT = 10010
MAX_MADD = 10
MAX_MDEP = 21
MAX_MALT = 21
#MAX_ALPHA = 1000
TIMEGROW = 100
MAX_TIMEGROW = 100000
TIMEFAIL = 10
MAX_TIMEFAIL = 100000
FREQ = 1
MAX_FREQ = 10
FILENAME = 'svcsim.json'
MODEL_SF = 'sf' # scale-free

def main(argv):
    cmd = ns.core.CommandLine()

    cmd.comp = None
    cmd.AddValue("comp", "The probability to find a composite service in the network")

    cmd.m_init = None
    cmd.AddValue("m_init", "Initial (small) number of nodes")

    cmd.m_add = None
    cmd.AddValue("m_add", "Number of nodes to be added every timestep")

    cmd.m_dep = None
    cmd.AddValue("m_dep", "The upper limit of number of links to be created of each added node (m_dep <= m_init + 1)")

    cmd.m_alt = None
    cmd.AddValue("m_alt", "The upper limit of number of alternate links to be created of each added link (m_alt <= m_init + 1)")

    cmd.alpha = None
    cmd.AddValue("alpha", "The inital attractiveness")

    cmd.timegrow = None
    cmd.AddValue("timegrow", "The duration (seconds) for the network to grow")

    cmd.timefail = None
    cmd.AddValue("timefail", "The duration (seconds) when failure is performed to the network")

    cmd.freq = None
    cmd.AddValue("freq", "How many times m_add nodes will be added to the network for each second")

    cmd.filename = None
    cmd.AddValue("filename", "File name to save the result in json format")

    cmd.model = None
    cmd.AddValue("model", "The network model to generate (scale-free: sf, exponential: exp, random: rand)")

    cmd.Parse(argv)

    if cmd.comp is None:
        comp = svcmodel.COMP
    else:
        comp = int(cmd.comp)
        if comp < 0.0 or comp > 1.0:
            print "Invalid argument: comp should be between 0.0 to 1.0"
            sys.exit()

    if cmd.m_init is None:
        m_init = svcmodel.M_INIT
    else:
        m_init = int(cmd.m_init)
        if m_init > MAX_MINIT:
            print "Invalid argument: m_init should not be higher than %d" % MAX_MINIT
            sys.exit()

    if cmd.m_add is None:
        m_add = svcmodel.M_ADD
    else:
        m_add = int(cmd.m_add)
        if m_add > MAX_MADD:
            print "Invalid argument: m_add should not be higher than %d" % MAX_MADD
            sys.exit()

    if cmd.m_dep is None:
        m_dep = svcmodel.M_DEP
    else:
        m_dep = int(cmd.m_dep)
        if m_dep > m_init + 1:
            print "Invalid argument: m_dep should not be higher than m_init + 1"
            sys.exit()
        elif m_dep > MAX_MDEP:
            print "Invalid argument: m_dep should not be higher than %d" % MAX_MDEP
            sys.exit()

    if cmd.m_alt is None:
        m_alt = svcmodel.M_ALT
    else:
        m_alt = int(cmd.m_alt)
        if m_alt > m_init + 1:
            print "Invalid argument: m_alt should not be higher than m_init + 1"
            sys.exit()
        elif m_alt > MAX_MALT:
            print "Invalid argument: m_alt should not be higher than %d" % MAX_MALT
            sys.exit()

    if cmd.alpha is None:
        alpha = svcmodel.ALPHA
    else:
        alpha = int(cmd.alpha)

    if cmd.timegrow is None:
        timegrow = TIMEGROW
    else:
        timegrow = int(cmd.timegrow)
        if timegrow > MAX_TIMEGROW:
            print "Invalid argument: timegrow should not be higher than %d" % MAX_TIMEGROW
            sys.exit()

    if cmd.timefail is None:
        timefail = TIMEFAIL
    else:
        timefail = int(cmd.timefail)
        if timefail > MAX_TIMEFAIL:
            print "Invalid argument: timefail should not be higher than %d" % MAX_TIMEFAIL
            sys.exit()

    if cmd.freq is None:
        freq = FREQ
    else:
        freq = int(cmd.freq)
        if freq > MAX_FREQ:
            print "Invalid argument: freq should not be higher than %d" % MAX_FREQ
            sys.exit()

    if cmd.filename is None:
        filename = FILENAME
    else:
        filename = cmd.filename

    if cmd.model is None:
        model = MODEL_SF
    else:
        model = cmd.model
        if model not in ['sf', 'exp', 'rand']:
            print "Possible arguments for network model parameter are 'sf', 'exp', and 'rand' for scale-free, exponential, and random, respectively"
            sys.exit()

    # prepare the network
    vertices = svc_nodes.Vertices()
    # initialize the network with some number of nodes
    svcmodel.initnetwork(vertices, m_init)

#    # set lbinsbase value for loglog plotting
#    step = timegrow * freq
#    if step >= 10000:
#        lbinsbase = 1.2
#    elif step >= 1000:
#        lbinsbase = 1.1
#    elif step >= 100:
#        lbinsbase = 1.05
#    else:
#        lbinsbase = 1.01

    ns.core.Simulator.Schedule(ns.core.Seconds(0), svcmodel.print_params, vertices, m_init, comp, m_add, m_dep, m_alt, alpha, timegrow, timefail, freq)

    # network growth
    for i in range(timegrow):
        for j in range(freq):
            ns.core.Simulator.Schedule(ns.core.Seconds(i), svcmodel.grow, vertices, comp, m_add, m_dep, m_alt, alpha, model)

#    ns.core.Simulator.Schedule(ns.core.Seconds(timegrow + 1), svc_routines.drawhistogram, vertices, 20, False)
#    ns.core.Simulator.Schedule(ns.core.Seconds(timegrow + 2), svc_routines.drawloglogdist, vertices, lbinsbase, True)
    ns.core.Simulator.Schedule(ns.core.Seconds(timegrow), svcmodel.print_stats, vertices)
    ns.core.Simulator.Schedule(ns.core.Seconds(timegrow), vertices.analyzer.takesnapshot, vertices)
    ns.core.Simulator.Schedule(ns.core.Seconds(timegrow), vertices.analyzer.loaddegreedist, vertices)

    # network failure
    timelimit = timegrow + 1 + timefail
    for i in range(timegrow + 1, timelimit):
        for j in range(freq):
            ns.core.Simulator.Schedule(ns.core.Seconds(i), svcmodel.randomfail, vertices)
    ###!!!
    #ns.core.Simulator.Schedule(ns.core.Seconds(timelimit), vertices.analyzer.takesnapshot, vertices)

    ns.core.Simulator.Schedule(ns.core.Seconds(timelimit), svcmodel.print_aftermath, vertices)
    #ns.core.Simulator.Schedule(ns.core.Seconds(timelimit), vertices.analyzer.loaddegreedist, vertices)
    ns.core.Simulator.Schedule(ns.core.Seconds(timelimit), vertices.analyzer.savetofile, filename)

    ns.core.Simulator.Stop(ns.core.Seconds(timelimit + 1))
    ns.core.Simulator.Run()
    ns.core.Simulator.Destroy()

    print ""
    print "Simulation is complete."
    if filename:
        print "Saved to %s" % (filename)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))


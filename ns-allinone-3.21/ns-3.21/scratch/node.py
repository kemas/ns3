# /*
#  * This program is free software; you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License version 2 as
#  * published by the Free Software Foundation;
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#  */

import ns.applications
import ns.core
import ns.internet
import ns.network
import ns.point_to_point

nodes = []
for i in range(5):
    nodes.append(ns.network.Node())


for i in range(5):
    for j in range(5):
        if i != j:
            p2ph = ns.point_to_point.PointToPointHelper()
            p2ph.Install(nodes[i], nodes[j])

print "channels: "+ str(ns.network.ChannelList.GetNChannels())

node = nodes[0]
print "node id: "+ str(node.GetId())
devdel = node.GetDevice(2)
channel = devdel.GetChannel()
print "channel: "+ str(channel.GetId())
for i in range(channel.GetNDevices()):
    adev = channel.GetDevice(i)
    print "  channel: "+ str(adev.GetChannel().GetId())
    print "  node id: "+ str(adev.GetNode().GetId())
    adev.Dispose()

#channel.Dispose()
#devdel.Dispose()

print "channels: "+ str(ns.network.ChannelList.GetNChannels())
print "iterating on channellist"
for i in range(ns.network.ChannelList.GetNChannels()):
    print ns.network.ChannelList.GetChannel(i).GetId()
    print ns.network.ChannelList.GetChannel(i).GetDevice(0).GetNode().GetId()

for i in range(node.GetNDevices()):
    if node.GetDevice(i).GetChannel():
        print node.GetDevice(i).GetChannel().GetId()

print "***"
node = nodes[3]
print "node id: "+ str(node.GetId())
print "ndevices: "+ str(node.GetNDevices())
for i in range(node.GetNDevices()):
    if node.GetDevice(i).GetChannel():
        print node.GetDevice(i).GetChannel().GetId()

ns.core.Simulator.Run()
ns.core.Simulator.Destroy()


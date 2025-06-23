#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def create_L2switch_network():

    net = Mininet(topo=None, link=TCLink)

    switch1 = net.addSwitch('s1',cls=OVSKernelSwitch, failMode='standalone')

    host1 = net.addHost('h1', ip='10.0.0.1')
    host2 = net.addHost('h2', ip='10.0.0.2')

    net.addLink(switch1, host1)
    net.addLink(switch1, host2)

    net.build()

    net.get('s1').start([])

    # switch1.cmd('ovs-ofctl add-flow \'table=0 actions=learn(table=1,hard_timeout=10, \
    #    NXM_OF_ETH_DST[]=NXM_OF_ETH_SRC[],output:NXM_OF_IN_PORT[]), resubmit(,1)')
    # switch1.cmd()
    
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    create_L2switch_network()

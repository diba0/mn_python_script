#!/usr/bin/env python

"""
Simple example of setting network and CPU parameters

NOTE: link params limit BW, add latency, and loss.
There is a high chance that pings WILL fail and that
iperf will hang indefinitely if the TCP handshake fails
to complete.
"""

from sys import argv
from functools import partial

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, RemoteController, OVSSwitch
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel, info

# It would be nice if we didn't have to do this:
# pylint: disable=arguments-differ

class SingleSwitchTopo( Topo ):
    "Single switch connected to n hosts."
    def build( self, n=2, lossy=True ):
        switch = self.addSwitch('s1')
        for h in range(n):
            # Each host gets 50%/n of system CPU
            host = self.addHost('h%s' % (h + 1))
            if lossy:
                # 10 Mbps, 5ms delay, 10% packet loss
                self.addLink(host, switch,
                             bw=10, delay='5ms', loss=10, use_htb=True)
            else:
                # 10 Mbps, 5ms delay, no packet loss
                self.addLink(host, switch,
                             bw=10, delay='5ms', loss=0, use_htb=True)


def perfTest( lossy=False ):
    "Create network and run simple performance test"
    topo = SingleSwitchTopo( n=4, lossy=lossy )
    switch = partial(OVSSwitch, protocols='OpenFlow13')
    controller = partial(RemoteController)
    net = Mininet( topo=topo, switch=switch, controller=controller,
                   host=CPULimitedHost, link=TCLink )
    net.start()
    info( "Dumping host connections\n" )
    dumpNodeConnections(net.hosts)
    info("Testing network connectivity\n")
    net.pingAll()
    info( "Testing bandwidth between h1 and h4 (lossy=%s)\n" % lossy )
    h1, h4 = net.get('h1', 'h4')
    net.iperf( ( h1, h4 ), l4Type='UDP' )
    # Debugging
    h1.cmd('jobs')
    h4.cmd('jobs')
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    # Debug for now
    if 'testmode' in argv:
        setLogLevel( 'debug' )
    # Prevent test_simpleperf from failing due to packet loss
    perfTest()


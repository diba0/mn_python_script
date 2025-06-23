#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel


def create_Network():

    net = Mininet(topo=None, switch=OVSSwitch, link=TCLink)
    
    # add switches
    host2 = net.addHost('h2')
    host3 = net.addHost('h3')
    host4 = net.addHost('h4')
    host5 = net.addHost('h5')
    
    # add hosts
    host1 = net.addHost('h1', ip='10.0.0.1/24', mac='11:11:11:11:11:11')
    host6 = net.addHost('h6', ip='10.0.6.6/24', mac='66:66:66:66:66:66')
    
    # add links
    net.addLink(host2, host3, delay='5ms', bw=10)
    net.addLink(host2, host5, delay='20ms', bw=10)
    net.addLink(host2, host4, delay='5ms', bw=20)
    net.addLink(host3, host5, delay='5ms', bw=10)
    net.addLink(host4, host5, delay='10ms', bw=20)
    
    net.addLink(host1, host2, delay='5ms', bw=20)
    net.addLink(host6, host5, delay='5ms', bw=20)

    net.build()

    # cmd: add interface ip
    host2.cmd('ifconfig h2-eth0 10.0.1.2/24')
    host2.cmd('ifconfig h2-eth1 10.0.2.2/24')
    host2.cmd('ifconfig h2-eth2 10.0.3.2/24')
    host2.cmd('ifconfig h2-eth3 10.0.0.2/24')
    host3.cmd('ifconfig h3-eth0 10.0.1.3/24')
    host3.cmd('ifconfig h3-eth1 10.0.4.3/24')
    host4.cmd('ifconfig h4-eth0 10.0.3.4/24')
    host4.cmd('ifconfig h4-eth1 10.0.5.4/24')
    host5.cmd('ifconfig h5-eth0 10.0.2.5/24')
    host5.cmd('ifconfig h5-eth1 10.0.4.5/24')
    host5.cmd('ifconfig h5-eth2 10.0.5.5/24')
    host5.cmd('ifconfig h5-eth3 10.0.6.5/24')
    # cmd: add host default route
    host1.cmd('ip route add default via 10.0.0.2')
    host6.cmd('ip route add default via 10.0.6.5')
    # cmd: add switch to host static route
    host2.cmd('ip route add 10.0.6.6 via 10.0.2.5')
    host3.cmd('ip route add 10.0.0.1 via 10.0.1.2')
    host3.cmd('ip route add 10.0.6.6 via 10.0.4.5')
    host4.cmd('ip route add 10.0.0.1 via 10.0.3.2')
    host4.cmd('ip route add 10.0.6.6 via 10.0.5.5')
    host5.cmd('ip route add 10.0.0.1 via 10.0.2.2')
    # cmd: add switch qos route
    # host2.cmd('ip rule add tos 0x08 table 1 priority 1')
    # host2.cmd('ip rule add tos 0x10 table 2 priority 2')
    # host2.cmd('ip rule add tos 0x02 table 3 priority 3')
    host2.cmd('iptables -t mangle -A PREROUTING -m dscp --dscp 0x20 -j MARK --set-mark 0x04')
    host2.cmd('iptables -t mangle -A PREROUTING -m dscp --dscp 0x10 -j MARK --set-mark 0x02')
    host2.cmd('iptables -t mangle -A PREROUTING -m dscp --dscp 0x08 -j MARK --set-mark 0x01')
    host2.cmd('ip rule add fwmark 0x01 table 3')
    host2.cmd('ip rule add fwmark 0x02 table 1')
    host2.cmd('ip rule add fwmark 0x04 table 2')
    host2.cmd('ip route add table 1 10.0.6.6 via 10.0.3.4')
    host2.cmd('ip route add table 2 10.0.6.6 via 10.0.1.3')
    host2.cmd('ip route add table 3 10.0.6.6 via 10.0.2.5')

    # host5.cmd('ip rule add tos 0x08 table 1 priority 1')
    # host5.cmd('ip rule add tos 0x10 table 2 priority 2')
    # host5.cmd('ip rule add tos 0x02 table 3 priority 3')
    host5.cmd('iptables -t mangle -A PREROUTING -m dscp --dscp 0x20 -j MARK --set-mark 0x04')
    host5.cmd('iptables -t mangle -A PREROUTING -m dscp --dscp 0x10 -j MARK --set-mark 0x02')
    host5.cmd('iptables -t mangle -A PREROUTING -m dscp --dscp 0x08 -j MARK --set-mark 0x01')
    host5.cmd('ip rule add fwmark 0x01 table 3')
    host5.cmd('ip rule add fwmark 0x02 table 1')
    host5.cmd('ip rule add fwmark 0x04 table 2')
    host5.cmd('ip route add table 1 10.0.0.1 via 10.0.5.4')
    host5.cmd('ip route add table 2 10.0.0.1 via 10.0.4.3')
    host5.cmd('ip route add table 3 10.0.0.1 via 10.0.2.2')

    # cmd: enable ip_forward 
    host2.cmd('sysctl net.ipv4.ip_forward=1')
    host3.cmd('sysctl net.ipv4.ip_forward=1')
    host4.cmd('sysctl net.ipv4.ip_forward=1')
    host5.cmd('sysctl net.ipv4.ip_forward=1')

    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_Network()
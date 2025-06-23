#!/usr/bin/env python3

from mininet.topo import Topo
from mininet.link import TCLink

class FatTreeTopo(Topo):
    " Simple Data Center Topology "

    " L1:core ovs, L2:aggregation ovs, L3:edge ovs "
    def build(self, L1=2):
        L2 = L1 * 2
        L3 = L2
        core_ovs = []
        aggregation_ovs = []
        edge_ovs = []

        # add core ovs
        for i in range(L1):
            switch = self.addSwitch('c{}'.format(i+1))
            core_ovs.append(switch)

        # add aggregation ovs
        for i in range(L2):
            switch = self.addSwitch('a{}'.format(L1+i+1))
            aggregation_ovs.append(switch)

        # add edge ovs
        for i in range(L3):
            switch = self.addSwitch('e{}'.format(L1+L2+i+1))
            edge_ovs.append(switch)

        # add links between core and aggregation ovs
        for i in range(L1):
            switch1 = core_ovs[i]
            for j in range(L2):
                switch2 = aggregation_ovs[j]
                if j == 0 or j == 2 :
                    self.addLink(switch1, switch2, bw=100, delay='1ms', loss=90)
                else:
                    self.addLink(switch1, switch2, bw=50, delay='10ms',loss=80)
                # self.addLink(switch1, switch2)
                
        # add links between aggregation and edge ovs
        for i in range(0, L2, 2):
            for switch1 in aggregation_ovs[i:i+2]:
                for switch2 in edge_ovs[i:i+2]:
                    self.addLink(switch1, switch2, bw=10, delay='15ms', loss=80)
                    # self.addLink(switch1, switch2)

        # add hosts and its links with edge ovs
        count = 1
        for switch in edge_ovs:
            for i in range(2):
                host = self.addHost('h{}'.format(count))
                self.addLink(switch, host)
                count += 1

topos = {'fattreetopo': FatTreeTopo}

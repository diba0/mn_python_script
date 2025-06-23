#!/usr/bin/env python

from mininet.topo import Topo
from mininet.cli import CLI

class NormalTopo( Topo ):
    
    def build(self):
    	# add switches
        switch1 = self.addSwitch('s1',failMode='standalone')
        switch2 = self.addSwitch('s2',failMode='standalone')
        
        # add hosts
        host1 = self.addHost('h1', ip="192.168.0.1")
        host2 = self.addHost('h2', ip="192.168.0.2")
        
        # add links
        
        
        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(switch1,switch2)

topos = { 'normaltopo': NormalTopo }

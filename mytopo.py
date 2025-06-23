#!/usr/bin/env python

from mininet.topo import Topo
from mininet.cli import CLI

class MyTopo( Topo ):
    
    def build( self, k=2):
    	# add switches
        switch1 = self.addSwitch('s1',failMode='standalone')
        switch2 = self.addSwitch('s2',failMode='standalone')
        switch3 = self.addSwitch('s3',failMode='standalone')
        switch4 = self.addSwitch('s4',failMode='standalone')
        switch5 = self.addSwitch('s5',failMode='standalone')
        
        # add hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
        
        # add links
        self.addLink(switch1, switch2, delay='2ms')
        self.addLink(switch1, switch4, delay='10ms')
        self.addLink(switch2, switch3, delay='2ms')
        self.addLink(switch3, switch5, delay='2ms')
        self.addLink(switch4, switch5, delay='10ms')
        
        self.addLink(host1, switch1, delay='5ms')
        self.addLink(host2, switch2, delay='5ms')
        self.addLink(host3, switch5, delay='5ms')

topos = { 'mytopo': MyTopo }

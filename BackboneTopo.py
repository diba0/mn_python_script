#!/usr/bin/env python

from mininet.topo import Topo
import random

NUMBER_OF_BACKBONE_CORE_OVS = 5
NUMBER_OF_BACKBONE_AGGREGATION_OVS = 10
NUMBER_OF_DATA_CENTER_CORE_OVS = 2
NUMBER_OF_DATA_CENTER_AGGREGATION_OVS = 4
NUMBER_OF_DATA_CENTER_EDGE_OVS = 4

class MyTopo(Topo):
    
    def build(self):
        "Backbone network topology."
        backbone_core_ovs = []
        backbone_aggregation_ovs = []
        switch_count = 1
    	# add backbone core ovs switches
        for i in range(NUMBER_OF_BACKBONE_CORE_OVS):
            switch = self.addSwitch('sw-bc-%d' % switch_count)
            switch_count += 1
            backbone_core_ovs.append(switch)
        # add backbone core links
        for i in range(NUMBER_OF_BACKBONE_CORE_OVS):
            for j in range(i+1, NUMBER_OF_BACKBONE_CORE_OVS):
                self.addLink(backbone_core_ovs[i], backbone_core_ovs[j], bw=1000, delay=str(random.randint(50,100))+'ms', loss=0.01)
        # add backbone aggregation ovs switches
        for i in range(NUMBER_OF_BACKBONE_AGGREGATION_OVS):
            switch = self.addSwitch('sw-ba-%d' % switch_count)
            switch_count += 1
            backbone_aggregation_ovs.append(switch)
        # add backbone aggregation links
        for i in range(NUMBER_OF_BACKBONE_CORE_OVS):
            for j in range(i*2, i*2+2):
                self.addLink(backbone_core_ovs[i], backbone_aggregation_ovs[j], bw=500, delay=str(random.randint(25,50))+'ms', loss=0.1)
        
        # add data center core ovs switches
        data_center_core_ovs = []
        for i in range(NUMBER_OF_DATA_CENTER_CORE_OVS):
            switch = self.addSwitch('sw-dcc-%d' % switch_count)
            switch_count += 1
            data_center_core_ovs.append(switch)
        # add data center aggregation ovs switches
        data_center_aggregation_ovs = []
        for i in range(NUMBER_OF_DATA_CENTER_AGGREGATION_OVS):
            switch = self.addSwitch('sw-dca-%d' % switch_count)
            switch_count += 1
            data_center_aggregation_ovs.append(switch)
        # add data center edge ovs switches
        data_center_edge_ovs = []
        for i in range(NUMBER_OF_DATA_CENTER_EDGE_OVS):
            switch = self.addSwitch('sw-dce-%d' % switch_count)
            switch_count += 1
            data_center_edge_ovs.append(switch)
        # add data center core and aggregation links
        for i in range(NUMBER_OF_DATA_CENTER_CORE_OVS):
            for j in range(NUMBER_OF_DATA_CENTER_AGGREGATION_OVS):
                self.addLink(data_center_core_ovs[i], data_center_aggregation_ovs[j], bw=100, delay=str(random.randint(10,25))+'ms', loss=0.2)
        # add data center aggregation and edge links
        for i in range(0,NUMBER_OF_DATA_CENTER_AGGREGATION_OVS, 2):
            for switch1 in data_center_aggregation_ovs[i:i+2]:
                for switch2 in data_center_edge_ovs[i:i+2]:
                    self.addLink(switch1, switch2, bw=50, delay=str(random.randint(5,10))+'ms',loss=0.5)
        # add hosts and its links with edge ovs
        host_count = 1
        for switch in data_center_edge_ovs:
            for i in range(2):
                host = self.addHost('h%d' % host_count)
                self.addLink(switch, host, bw=50, delay=str(random.randint(1,5))+'ms',loss=0.5)
                host_count += 1
        # add links between backbone and data center
        for i in range(2):
            for j in range(2):
                self.addLink(backbone_aggregation_ovs[i], data_center_core_ovs[j], bw=80, delay=str(random.randint(20,40))+'ms', loss=0.2)
        
        # add three local network , each has four switches
        local_switches = []
        for i in range(3):
            local_switches.append([])
            for j in range(4):
                switch = self.addSwitch('sw-l-%d' % switch_count)
                switch_count += 1
                local_switches[i].append(switch)
        # add links between local switches[i][0] and its 2 hosts
        for i in range(3):
            for j in range(2):
                host = self.addHost('h%d' % host_count)
                self.addLink(local_switches[i][0], host, bw=50, delay=str(random.randint(5,10))+'ms', loss=0.5)
                host_count += 1
        # add links between local switches and backbone aggregation switches
        for i in range(3):
            for j in range(2+2*i, 4+2*i):
                for k in range(4):
                    self.addLink(backbone_aggregation_ovs[j], local_switches[i][k], bw=80, delay=str(random.randint(20,40))+'ms', loss=0.2)
        


topos = { 'mytopo': MyTopo }

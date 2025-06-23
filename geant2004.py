#!/usr/bin/env python

from mininet.topo import Topo

class GEANT2004Topo(Topo):
    def build(self):
        # 添加交换机 s1 - s23
        switches = {}
        for i in range(1, 24):
            sw = 's' + str(i)
            switches[sw] = self.addSwitch(sw, failMode='standalone')

        # 添加主机，每个交换机连接一个主机 h1 - h23
        for i in range(1, 24):
            host = self.addHost('h' + str(i))
            self.addLink(host, switches['s' + str(i)])

        # 添加链路：格式 (src, dst, bandwidth in Mbps)
        links = [
            ('s1', 's3', 100),
            ('s1', 's7', 100),
            ('s1', 's16', 100),
            ('s2', 's4', 100),
            ('s2', 's7', 100),
            ('s2', 's12', 100),
            ('s2', 's13', 100),
            ('s2', 's18', 25),
            ('s2', 's23', 25),
            ('s3', 's10', 100),
            ('s3', 's11', 25),
            ('s3', 's14', 1.55),
            ('s3', 's21', 100),
            ('s4', 's16', 100),
            ('s5', 's8', 25),
            ('s5', 's16', 25),
            ('s6', 's7', 1.55),
            ('s6', 's19', 1.55),
            ('s7', 's17', 100),
            ('s7', 's19', 25),
            ('s7', 's21', 100),
            ('s8', 's9', 25),
            ('s9', 's15', 25),
            ('s9', 's16', 100),
            ('s10', 's11', 25),
            ('s10', 's12', 100),
            ('s10', 's16', 100),
            ('s10', 's17', 100),
            ('s12', 's22', 100),
            ('s13', 's14', 1.55),
            ('s13', 's17', 100),
            ('s13', 's19', 25),
            ('s15', 's20', 25),
            ('s17', 's20', 100),
            ('s17', 's23', 25),
            ('s18', 's21', 25),
            ('s20', 's22', 25)
        ]

        for src, dst, bw in links:
            self.addLink(switches[src], switches[dst], bw=bw)

topos = { 'geant2004topo': GEANT2004Topo }


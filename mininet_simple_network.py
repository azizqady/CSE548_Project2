from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import info, setLogLevel
setLogLevel("info")


net = Mininet(controller=RemoteController, switch=OVSSwitch)

#info('*** Adding controllers\n')
c1 = net.addController('c1', port=6650)
c2 = net.addController('c2', port=6630)

#info('*** Adding docker containers\n')
d1 = net.addHost('d1', mac='00:00:00:00:00:01', ip='10.0.2.10', dimage="ubuntu:trusty")
d2 = net.addHost('d2', mac='00:00:00:00:00:02', ip='10.0.2.20', dimage="ubuntu:trusty")
d3 = net.addHost('d3', mac='00:00:00:00:00:03', ip='192.168.2.30', dimage="ubuntu:trusty")
d4 = net.addHost('d4', mac='00:00:00:00:00:04', ip='192.168.2.40', dimage="ubuntu:trusty")

#info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')

#info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(d1, s2)
net.addLink(d2, s1)
net.addLink(d3, s2)
net.addLink(d4, s2)

#info('*** change d1-eth1 MAC and IP\n')
d1.intf('d1-eth1').setMAC('00:00:00:00:00:05')
d1.intf('d1-eth1').setIP('192.168.2.10','24')

info('*** Starting network\n')
net.start()

#info('*** Testing connectivity\n')
#net.ping([d1, d2, d3, d4])


CLI(net)
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
import math

def getDelay(la1, lo1, la2, lo2):
    first_product = math.sin(float(la1)) * math.sin(float(la2))
    second_product_first_part = math.cos(float(la1)) * math.cos(float(la2))
    second_product_second_part = math.cos((float(lo2)) - (float(lo1)))
    distance = math.radians(math.acos(first_product + (second_product_first_part * second_product_second_part))) * 6378.137
    # t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))
    # t         = ( distance       * 1000              ) / ( 1.97 * 10**8   / 1000         )
    delay = "'" + (str((distance * 1000) / 197000)) + "ms'"
    return delay    

def OS3ENetwork():

    net = Mininet(topo=None, switch=OVSKernelSwitch, link=TCLink)

    # add routers
    Sunnyvale = net.addHost('s1')
    Nashville = net.addHost('s2')
    Raleigh = net.addHost('s3')
    Chicago = net.addHost('s4')
    El_Paso = net.addHost('s5')
    Denver = net.addHost('s6')
    Dallas = net.addHost('s7')
    Louisville = net.addHost('s8')
    Vancouver = net.addHost('s9')
    Washington_DC = net.addHost('s10')
    Indianapolis = net.addHost('s11')
    Pittsburgh = net.addHost('s12')
    Baton_Rouge = net.addHost('s13')
    Albuquerque = net.addHost('s14')
    Los_Angeles = net.addHost('s15')
    Atlanta = net.addHost('s16')
    Memphis = net.addHost('s17')
    Jacksonville = net.addHost('s18')
    Miami = net.addHost('s19')
    Kansas_City = net.addHost('s20')
    Missoula = net.addHost('s21')
    Philadelphia = net.addHost('s22')
    Tucson = net.addHost('s23')
    Buffalo = net.addHost('s24')
    Houston = net.addHost('s25')
    Boston = net.addHost('s26')
    Minneapolis = net.addHost('s27')
    New_York = net.addHost('s28')
    Salt_Lake_City = net.addHost('s29')
    Cleveland = net.addHost('s30')
    Jackson = net.addHost('s31')
    Portland = net.addHost('s32')
    Seattle = net.addHost('s33')
    Ashburn = net.addHost('s34')

    routers ={Sunnyvale, Nashville, Raleigh, Chicago, El_Paso, Denver, Dallas, Louisville, Vancouver, Washington_DC, Indianapolis, Pittsburgh, Baton_Rouge, Albuquerque, Los_Angeles, Atlanta, Memphis, Jacksonville, Miami, Kansas_City, Missoula, Philadelphia, Tucson, Buffalo, Houston, Boston, Minneapolis, New_York, Salt_Lake_City, Cleveland, Jackson, Portland, Seattle, Ashburn}

    # add control switch
    control_switch = net.addSwitch('s35', failMode='standalone')

    # add edges between router and control switch
    for router in routers:
        net.addLink(router, control_switch, bw=1, delay='1ms')

    # ... and now hosts
    Sunnyvale_host = net.addHost('h1', ip='10.0.1.1')
    Nashville_host = net.addHost('h2', ip='10.0.2.1')
    Raleigh_host = net.addHost('h3', ip='10.0.3.1')
    Chicago_host = net.addHost('h4', ip='10.0.4.1')
    El_Paso_host = net.addHost('h5', ip='10.0.5.1')
    Denver_host = net.addHost('h6', ip='10.0.6.1')
    Dallas_host = net.addHost('h7', ip='10.0.7.1')
    Louisville_host = net.addHost('h8', ip='10.0.8.1')
    Vancouver_host = net.addHost('h9', ip='10.0.9.1')
    Washington_DC_host = net.addHost('h10', ip='10.0.10.1')
    Indianapolis_host = net.addHost('h11', ip='10.0.11.1')
    Pittsburgh_host = net.addHost('h12', ip='10.0.12.1')
    Baton_Rouge_host = net.addHost('h13', ip='10.0.13.1')
    Albuquerque_host = net.addHost('h14', ip='10.0.14.1')
    Los_Angeles_host = net.addHost('h15', ip='10.0.15.1')
    Atlanta_host = net.addHost('h16', ip='10.0.16.1')
    Memphis_host = net.addHost('h17', ip='10.0.17.1')
    Jacksonville_host = net.addHost('h18', ip='10.0.18.1')
    Miami_host = net.addHost('h18', ip='10.0.19.1')
    Kansas_City_host = net.addHost('h20', ip='10.0.20.1')
    Missoula_host = net.addHost('h21', ip='10.0.21.1')
    Philadelphia_host = net.addHost('h22', ip='10.0.22.1')
    Tucson_host = net.addHost('h23', ip='10.0.23.1')
    Buffalo_host = net.addHost('h24', ip='10.0.24.1')
    Houston_host = net.addHost('h25', ip='10.0.25.1')
    Boston_host = net.addHost('h26', ip='10.0.26.1')
    Minneapolis_host = net.addHost('h27', ip='10.0.27.1')
    New_York_host = net.addHost('h28', ip='10.0.28.1')
    Salt_Lake_City_host = net.addHost('h29', ip='10.0.29.1')
    Cleveland_host = net.addHost('h30', ip='10.0.30.1')
    Jackson_host = net.addHost('h31', ip='10.0.31.1')
    Portland_host = net.addHost('h32', ip='10.0.32.1')
    Seattle_host = net.addHost('h33', ip='10.0.33.1')
    Ashburn_host = net.addHost('h34', ip='10.0.34.1')

    # add control host
    control_host = net.addHost('h35', ip='10.0.0.35')

    # add edges between switch and corresponding host
    net.addLink(Sunnyvale, Sunnyvale_host)
    net.addLink(Nashville, Nashville_host)
    net.addLink(Raleigh, Raleigh_host)
    net.addLink(Chicago, Chicago_host)
    net.addLink(El_Paso, El_Paso_host)
    net.addLink(Denver, Denver_host)
    net.addLink(Dallas, Dallas_host)
    net.addLink(Louisville, Louisville_host)
    net.addLink(Vancouver, Vancouver_host)
    net.addLink(Washington_DC, Washington_DC_host)
    net.addLink(Indianapolis, Indianapolis_host)
    net.addLink(Pittsburgh, Pittsburgh_host)
    net.addLink(Baton_Rouge, Baton_Rouge_host)
    net.addLink(Albuquerque, Albuquerque_host)
    net.addLink(Los_Angeles, Los_Angeles_host)
    net.addLink(Atlanta, Atlanta_host)
    net.addLink(Memphis, Memphis_host)
    net.addLink(Jacksonville, Jacksonville_host)
    net.addLink(Miami, Miami_host)
    net.addLink(Kansas_City, Kansas_City_host)
    net.addLink(Missoula, Missoula_host)
    net.addLink(Philadelphia, Philadelphia_host)
    net.addLink(Tucson, Tucson_host)
    net.addLink(Buffalo, Buffalo_host)
    net.addLink(Houston, Houston_host)
    net.addLink(Boston, Boston_host)
    net.addLink(Minneapolis, Minneapolis_host)
    net.addLink(New_York, New_York_host)
    net.addLink(Salt_Lake_City, Salt_Lake_City_host)
    net.addLink(Cleveland, Cleveland_host)
    net.addLink(Jackson, Jackson_host)
    net.addLink(Portland, Portland_host)
    net.addLink(Seattle, Seattle_host)
    net.addLink(Ashburn, Ashburn_host)

    # add edges between control switch and control host
    net.addLink(control_switch, control_host)

    # add edges between switches
    net.addLink(Vancouver, Seattle, bw=1, delay=getDelay(49.260440, -123.114034, 47.603560, -122.329439))
    net.addLink(Seattle, Missoula, bw=1, delay=getDelay(47.603560, -122.329439, 46.872780, -113.996234))
    net.addLink(Missoula, Minneapolis, bw=1, delay=getDelay(46.872780, -113.996234, 44.979035, -93.264929))
    net.addLink(Minneapolis, Chicago, bw=1, delay=getDelay(44.979035, -93.264929, 41.884150, -87.632409))
    net.addLink(Seattle, Salt_Lake_City, bw=1, delay=getDelay(47.603560, -122.329439, 40.759505, -111.888229))
    net.addLink(Seattle, Portland, bw=1, delay=getDelay(47.603560, -122.329439, 45.511795, -122.675629))
    net.addLink(Portland, Sunnyvale, bw=1, delay=getDelay(45.511795, -122.675629, 37.371612, -122.038258))
    net.addLink(Sunnyvale, Salt_Lake_City, bw=1, delay=getDelay(37.371612, -122.038258, 40.759505, -111.888229))
    net.addLink(Sunnyvale, Los_Angeles, bw=1, delay=getDelay(37.371612, -122.038258, 34.053490, -118.245319))
    net.addLink(Los_Angeles, Salt_Lake_City, bw=1, delay=getDelay(34.053490, -118.245319, 40.759505, -111.888229))
    net.addLink(Los_Angeles, Tucson, bw=1, delay=getDelay(34.053490, -118.245319, 32.221553, -110.969754))
    net.addLink(Tucson, El_Paso, bw=1, delay=getDelay(32.221553, -110.969754, 31.759165, -106.487494))
    net.addLink(Salt_Lake_City, Denver, bw=1, delay=getDelay(40.759505, -111.888229, 39.740010, -104.992259))
    net.addLink(Denver, Albuquerque, bw=1, delay=getDelay(39.740010, -104.992259, 35.084180, -106.648639))
    net.addLink(Albuquerque, El_Paso, bw=1, delay=getDelay(35.084180, -106.648639, 31.759165, -106.487494))
    net.addLink(Denver, Kansas_City, bw=1, delay=getDelay(39.740010, -104.992259, 39.102960, -94.583062))
    net.addLink(Kansas_City, Chicago, bw=1, delay=getDelay(39.102960, -94.583062, 41.884150, -87.632409))
    net.addLink(Kansas_City, Dallas, bw=1, delay=getDelay(39.102960, -94.583062, 32.778155, -96.795404))
    net.addLink(Dallas, Houston, bw=1, delay=getDelay(32.778155, -96.795404, 29.760450, -95.369784))
    net.addLink(El_Paso, Houston, bw=1, delay=getDelay(31.759165, -106.487494, 29.760450, -95.369784))
    net.addLink(Houston, Jackson, bw=1, delay=getDelay(29.760450, -95.369784, 32.298690, -90.180489))
    net.addLink(Jackson, Memphis, bw=1, delay=getDelay(32.298690, -90.180489, 35.149680, -90.048929))
    net.addLink(Memphis, Nashville, bw=1, delay=getDelay(35.149680, -90.048929, 36.167783, -86.778365))
    net.addLink(Houston, Baton_Rouge, bw=1, delay=getDelay(29.760450, -95.369784, 30.443335, -91.186994))
    net.addLink(Baton_Rouge, Jacksonville, bw=1, delay=getDelay(30.443335, -91.186994, 30.331380, -81.655799))
    net.addLink(Chicago, Indianapolis, bw=1, delay=getDelay(41.884150, -87.632409, 39.766910, -86.149964))
    net.addLink(Indianapolis, Louisville, bw=1, delay=getDelay(39.766910, -86.149964, 38.254860, -85.766404))
    net.addLink(Louisville, Nashville, bw=1, delay=getDelay(38.254860, -85.766404, 36.167783, -86.778365))
    net.addLink(Nashville, Atlanta, bw=1, delay=getDelay(36.167783, -86.778365, 33.748315, -84.391109))
    net.addLink(Atlanta, Jacksonville, bw=1, delay=getDelay(33.748315, -84.391109, 30.331380, -81.655799))
    net.addLink(Jacksonville, Miami, bw=1, delay=getDelay(30.331380, -81.655799, 25.728985, -80.237419))
    net.addLink(Chicago, Cleveland, bw=1, delay=getDelay(41.884150, -87.632409, 41.504365, -81.690459))
    net.addLink(Cleveland, Buffalo, bw=1, delay=getDelay(41.504365, -81.690459, 42.885440, -78.878464))
    net.addLink(Buffalo, Boston, bw=1, delay=getDelay(42.885440, -78.878464, 42.358635, -71.056699))
    net.addLink(Boston, New_York, bw=1, delay=getDelay(42.358635, -71.056699, 40.714550, -74.007124))
    net.addLink(New_York, Philadelphia, bw=1, delay=getDelay(40.714550, -74.007124, 39.952270, -75.162369))
    net.addLink(Philadelphia, Washington_DC, bw=1, delay=getDelay(39.952270, -75.162369, 38.890370, -77.031959))
    net.addLink(Cleveland, Pittsburgh, bw=1, delay=getDelay(41.504365, -81.690459, 40.438335, -79.997459))
    net.addLink(Pittsburgh, Ashburn, bw=1, delay=getDelay(40.438335, -79.997459, 39.051631, -77.483151))
    net.addLink(Ashburn, Washington_DC, bw=1, delay=getDelay(39.051631, -77.483151, 38.890370, -77.031959))
    net.addLink(Washington_DC, Raleigh, bw=1, delay=getDelay(38.890370, -77.031959, 35.785510, -78.642669))
    net.addLink(Raleigh, Atlanta, bw=1, delay=getDelay(35.785510, -78.642669, 33.748315, -84.391109))

    net.build()

    net.get('s35').start([])

    # cmd: add interface ip
    for router in routers:
        router.cmd('ifconfig ' + router.name + '-eth0 10.0.0.' + router.name[1:] + '/24')
        router.cmd('ifconfig ' + router.name + '-eth1 10.0.' + router.name[1:] + '.2/24')
    Vancouver.cmd('ifconfig ' + Vancouver.name + '-eth2 10.0.35.' + Vancouver.name[1:] + '/24')
    Seattle.cmd('ifconfig ' + Seattle.name + '-eth2 10.0.35.' + Seattle.name[1:] + '/24')
    
    Seattle.cmd('ifconfig ' + Seattle.name + '-eth3 10.0.36.' + Seattle.name[1:] + '/24')
    Missoula.cmd('ifconfig ' + Missoula.name + '-eth2 10.0.36.' + Missoula.name[1:] + '/24')
    
    Missoula.cmd('ifconfig ' + Missoula.name + '-eth3 10.0.37.' + Missoula.name[1:] + '/24')
    Minneapolis.cmd('ifconfig ' + Minneapolis.name + '-eth2 10.0.37.' + Minneapolis.name[1:] + '/24')
    
    Minneapolis.cmd('ifconfig ' + Minneapolis.name + '-eth3 10.0.38.' + Minneapolis.name[1:] + '/24')
    Chicago.cmd('ifconfig ' + Chicago.name + '-eth2 10.0.38.' + Chicago.name[1:] + '/24')
    
    Seattle.cmd('ifconfig ' + Seattle.name + '-eth4 10.0.39.' + Seattle.name[1:] + '/24')
    Salt_Lake_City.cmd('ifconfig ' + Salt_Lake_City.name + '-eth2 10.0.39.' + Salt_Lake_City.name[1:] + '/24')
    
    Seattle.cmd('ifconfig ' + Seattle.name + '-eth5 10.0.40.' + Seattle.name[1:] + '/24')
    Portland.cmd('ifconfig ' + Portland.name + '-eth2 10.0.40.' + Portland.name[1:] + '/24')
    
    Portland.cmd('ifconfig ' + Portland.name + '-eth3 10.0.41.' + Portland.name[1:] + '/24')
    Sunnyvale.cmd('ifconfig ' + Sunnyvale.name + '-eth2 10.0.41.' + Sunnyvale.name[1:] + '/24')
    
    Sunnyvale.cmd('ifconfig ' + Sunnyvale.name + '-eth3 10.0.42.' + Sunnyvale.name[1:] + '/24')
    Salt_Lake_City.cmd('ifconfig ' + Salt_Lake_City.name + '-eth3 10.0.42.' + Salt_Lake_City.name[1:] + '/24')
    
    Sunnyvale.cmd('ifconfig ' + Sunnyvale.name + '-eth4 10.0.43.' + Sunnyvale.name[1:] + '/24')
    Los_Angeles.cmd('ifconfig ' + Los_Angeles.name + '-eth2 10.0.43.' + Los_Angeles.name[1:] + '/24')
    
    Los_Angeles.cmd('ifconfig ' + Los_Angeles.name + '-eth3 10.0.44.' + Los_Angeles.name[1:] + '/24')
    Salt_Lake_City.cmd('ifconfig ' + Salt_Lake_City.name + '-eth4 10.0.44.' + Salt_Lake_City.name[1:] + '/24')
    
    Los_Angeles.cmd('ifconfig ' + Los_Angeles.name + '-eth4 10.0.45.' + Los_Angeles.name[1:] + '/24')
    Tucson.cmd('ifconfig ' + Tucson.name + '-eth2 10.0.45.' + Tucson.name[1:] + '/24')
    
    Tucson.cmd('ifconfig ' + Tucson.name + '-eth3 10.0.46.' + Tucson.name[1:] + '/24')
    El_Paso.cmd('ifconfig ' + El_Paso.name + '-eth2 10.0.46.' + El_Paso .name[1:] + '/24')
    
    Salt_Lake_City.cmd('ifconfig ' + Salt_Lake_City.name + '-eth5 10.0.47.' + Salt_Lake_City.name[1:] + '/24')
    Denver.cmd('ifconfig ' + Denver.name + '-eth2 10.0.47.' + Denver.name[1:] + '/24')
    
    Denver.cmd('ifconfig ' + Denver.name + '-eth3 10.0.48.' + Denver.name[1:] + '/24')
    Albuquerque.cmd('ifconfig ' + Albuquerque.name + '-eth2 10.0.48.' + Albuquerque.name[1:] + '/24')

    Albuquerque.cmd('ifconfig ' + Albuquerque.name + '-eth3 10.0.49.' + Albuquerque.name[1:] + '/24')
    El_Paso.cmd('ifconfig ' + El_Paso.name + '-eth3 10.0.49.' + El_Paso.name[1:] + '/24')

    Denver.cmd('ifconfig ' + Denver.name + '-eth4 10.0.50.' + Denver.name[1:] + '/24')
    Kansas_City.cmd('ifconfig ' + Kansas_City.name + '-eth2 10.0.50.' + Kansas_City.name[1:] + '/24')

    Kansas_City.cmd('ifconfig ' + Kansas_City.name + '-eth3 10.0.51.' + Kansas_City.name[1:] + '/24')
    Chicago.cmd('ifconfig ' + Chicago.name + '-eth3 10.0.51.' + Chicago.name[1:] + '/24')

    Kansas_City.cmd('ifconfig ' + Kansas_City.name + '-eth4 10.0.52.' + Kansas_City.name[1:] + '/24')
    Dallas.cmd('ifconfig ' + Dallas.name + '-eth2 10.0.52.' + Dallas.name[1:] + '/24')

    Dallas.cmd('ifconfig ' + Dallas.name + '-eth3 10.0.53.' + Dallas.name[1:] + '/24')
    Houston.cmd('ifconfig ' + Houston.name + '-eth2 10.0.53.' + Houston.name[1:] + '/24')

    El_Paso.cmd('ifconfig ' + El_Paso.name + '-eth4 10.0.54.' + El_Paso.name[1:] + '/24')
    Houston.cmd('ifconfig ' + Houston.name + '-eth3 10.0.54.' + Houston.name[1:] + '/24')

    Houston.cmd('ifconfig ' + Houston.name + '-eth4 10.0.55.' + Houston.name[1:] + '/24')
    Jackson.cmd('ifconfig ' + Jackson.name + '-eth2 10.0.55.' + Jackson.name[1:] + '/24')

    Jackson.cmd('ifconfig ' + Jackson.name + '-eth3 10.0.56.' + Jackson.name[1:] + '/24')
    Memphis.cmd('ifconfig ' + Memphis.name + '-eth2 10.0.56.' + Memphis.name[1:] + '/24')

    Memphis.cmd('ifconfig ' + Memphis.name + '-eth3 10.0.57.' + Memphis.name[1:] + '/24')
    Nashville.cmd('ifconfig ' + Nashville.name + '-eth2 10.0.57.' + Nashville.name[1:] + '/24')

    Houston.cmd('ifconfig ' + Houston.name + '-eth5 10.0.58.' + Houston.name[1:] + '/24')
    Baton_Rouge.cmd('ifconfig ' + Baton_Rouge.name + '-eth2 10.0.58.' + Baton_Rouge.name[1:] + '/24')

    Baton_Rouge.cmd('ifconfig ' + Baton_Rouge.name + '-eth3 10.0.59.' + Baton_Rouge.name[1:] + '/24')
    Jacksonville.cmd('ifconfig ' + Jacksonville.name + '-eth2 10.0.59.' + Jacksonville.name[1:] + '/24')

    Chicago.cmd('ifconfig ' + Chicago.name + '-eth4 10.0.60.' + Chicago.name[1:] + '/24')
    Indianapolis.cmd('ifconfig ' + Indianapolis.name + '-eth2 10.0.60.' + Indianapolis.name[1:] + '/24')

    Indianapolis.cmd('ifconfig ' + Indianapolis.name + '-eth3 10.0.61.' + Indianapolis.name[1:] + '/24')
    Louisville.cmd('ifconfig ' + Louisville.name + '-eth2 10.0.61.' + Louisville.name[1:] + '/24')

    Louisville.cmd('ifconfig ' + Louisville.name + '-eth3 10.0.62.' + Louisville.name[1:] + '/24')
    Nashville.cmd('ifconfig ' + Nashville.name + '-eth3 10.0.62.' + Nashville.name[1:] + '/24')

    Nashville.cmd('ifconfig ' + Nashville.name + '-eth4 10.0.63.' + Nashville.name[1:] + '/24')
    Atlanta.cmd('ifconfig ' + Atlanta.name + '-eth2 10.0.63.' + Atlanta.name[1:] + '/24')

    Atlanta.cmd('ifconfig ' + Atlanta.name + '-eth3 10.0.64.' + Atlanta.name[1:] + '/24')
    Jacksonville.cmd('ifconfig ' + Jacksonville.name + '-eth3 10.0.64.' + Jacksonville.name[1:] + '/24')

    Jacksonville.cmd('ifconfig ' + Jacksonville.name + '-eth4 10.0.65.' + Jacksonville.name[1:] + '/24')
    Miami.cmd('ifconfig ' + Miami.name + '-eth2 10.0.65.' + Miami.name[1:] + '/24')

    Chicago.cmd('ifconfig ' + Chicago.name + '-eth5 10.0.66.' + Chicago.name[1:] + '/24')
    Cleveland.cmd('ifconfig ' + Cleveland.name + '-eth2 10.0.66.' + Cleveland.name[1:] + '/24')

    Cleveland.cmd('ifconfig ' + Cleveland.name + '-eth3 10.0.67.' + Cleveland.name[1:] + '/24')
    Buffalo.cmd('ifconfig ' + Buffalo.name + '-eth2 10.0.67.' + Buffalo.name[1:] + '/24')

    Buffalo.cmd('ifconfig ' + Buffalo.name + '-eth3 10.0.68.' + Buffalo.name[1:] + '/24')
    Boston.cmd('ifconfig ' + Boston.name + '-eth2 10.0.68.' + Boston.name[1:] + '/24')

    Boston.cmd('ifconfig ' + Boston.name + '-eth3 10.0.69.' + Boston.name[1:] + '/24')
    New_York.cmd('ifconfig ' + New_York.name + '-eth2 10.0.69.' + New_York.name[1:] + '/24')

    New_York.cmd('ifconfig ' + New_York.name + '-eth3 10.0.70.' + New_York.name[1:] + '/24')
    Philadelphia.cmd('ifconfig ' + Philadelphia.name + '-eth2 10.0.70.' + Philadelphia.name[1:] + '/24')

    Philadelphia.cmd('ifconfig ' + Philadelphia.name + '-eth3 10.0.71.' + Philadelphia.name[1:] + '/24')
    Washington_DC.cmd('ifconfig ' + Washington_DC.name + '-eth2 10.0.71.' + Washington_DC.name[1:] + '/24')

    Cleveland.cmd('ifconfig ' + Cleveland.name + '-eth4 10.0.72.' + Cleveland.name[1:] + '/24')
    Pittsburgh.cmd('ifconfig ' + Pittsburgh.name + '-eth2 10.0.72.' + Pittsburgh.name[1:] + '/24')

    Pittsburgh.cmd('ifconfig ' + Pittsburgh.name + '-eth3 10.0.73.' + Pittsburgh.name[1:] + '/24')
    Ashburn.cmd('ifconfig ' + Ashburn.name + '-eth2 10.0.73.' + Ashburn.name[1:] + '/24')

    Ashburn.cmd('ifconfig ' + Ashburn.name + '-eth3 10.0.74.' + Ashburn.name[1:] + '/24')
    Washington_DC.cmd('ifconfig ' + Washington_DC.name + '-eth3 10.0.74.' + Washington_DC.name[1:] + '/24')

    Washington_DC.cmd('ifconfig ' + Washington_DC.name + '-eth4 10.0.75.' + Washington_DC.name[1:] + '/24')
    Raleigh.cmd('ifconfig ' + Raleigh.name + '-eth2 10.0.75.' + Raleigh.name[1:] + '/24')

    Raleigh.cmd('ifconfig ' + Raleigh.name + '-eth3 10.0.76.' + Raleigh.name[1:] + '/24')
    Atlanta.cmd('ifconfig ' + Atlanta.name + '-eth4 10.0.76.' + Atlanta.name[1:] + '/24')

    # start ipv4 forwarding
    for router in routers:
        router.cmd('sysctl -w net.ipv4.ip_forward=1')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    OS3ENetwork()
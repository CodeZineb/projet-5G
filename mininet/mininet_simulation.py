from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel
import time

def simple_topology():
    net = Mininet(controller=Controller)

    print("📡 Création du réseau...")
    net.addController('c0')
    
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    print("🚀 Démarrage du réseau...")
    net.start()

    print("⏳ Test de connectivité...")
    net.pingAll()

    print("📊 Mesure du débit entre h1 et h2...")
    h1.cmd('iperf -s -u &')
    time.sleep(1)
    result = h2.cmd('iperf -c {} -u -t 5'.format(h1.IP()))
    print(result)

    print("🛑 Arrêt du réseau...")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simple_topology()

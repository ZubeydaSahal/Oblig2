#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel

# Definerer en enkel topologi med 2 hoster og 1 switch
class SimpleTopo(Topo):
    def build(self):
        # Legg til  hoster
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Legg til en switch
        s1 = self.addSwitch('s1')

        #kobler hostene til switchen
        self.addLink(h1, s1)
        self.addLink(h2, s1)

# når filen kjører starter vi mininet
if __name__ == '__main__':
    setLogLevel('info')  # Vis loggmeldinger i terminal
    net = Mininet(topo=SimpleTopo())  # Bruk topologien vi lagde
    net.start()  # Start nett

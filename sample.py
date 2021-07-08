"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):

    def build ( self ):

        hconfig = {'inNameSpace':True}
        host_link_config = {}
#       http_link_config = {'bw': 10}
#	video_link_config = {'bw': 1000}
       

        # Create switch nodes
        for i in range(5):
            sconfig = {'dpid': "%016x" % (i+1)}
            self.addSwitch('s%d' % (i+1), **sconfig)

	# Create host nodes
        for i in range(7):
            self.addHost('h%d' % (i+1), **hconfig)

        # Add Switch Links
        self.addLink('s1', 's4')#, **http_link_config)
        self.addLink('s2', 's3')#, **http_link_config)
        self.addLink('s3', 's4')#, **http_link_config)
        self.addLink('s4', 's5')#, **video_link_config)
        #self.addLink('s4', 's6', **video_link_config)


	 # Add links
        self.addLink( 'h1', 's1', **host_link_config)
        self.addLink( 'h2', 's1', **host_link_config)
        self.addLink( 'h3', 's2', **host_link_config)
        self.addLink( 'h4', 's2', **host_link_config)
        self.addLink( 'h5', 's4', **host_link_config)
        self.addLink( 'h6', 's4', **host_link_config)
        self.addLink( 'h7', 's5', **host_link_config)
        #self.addLink( 'h8', 's5', **host_link_config)
        #self.addLink( 'h9', 's6', **host_link_config)
	#self.addLink( 'h10', 's6', **host_link_config)

topos = { 'mytopo': ( lambda: MyTopo() ) }

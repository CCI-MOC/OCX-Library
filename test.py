import api
# Socks
import socks
import socket

enpoint_list = ['http://140.247.152.200:5000/v2.0']

tenant_name ='admin'
username = 'xuh'
password = 'xuhang0507'


# Set up SOCKS proxy usage:
s = socks.socksocket()

# Set up the Port number as the one used for connecting Harvard Cluster
socks.set_default_proxy(socks.SOCKS5, 'localhost', 5507)
socket.socket = socks.socksocket


session_list = api.init_sessions(tenant_name, username, password, enpoint_list)
nova_client_list  = api.init_nova_clients('1.1', session_list)
for nova in nova_client_list:
	print nova.images.list()

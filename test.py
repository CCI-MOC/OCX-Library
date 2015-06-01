import api
# Socks
import socks
import socket

url_list = ['http://140.247.152.207:5000/v2.0']

tenant_name ='moc-ops-experiments'
username = 'xuh'
password = 'xuhang0507'


session_list = api.init_sessions(tenant_name, username, password, url_list)

nova_client_list  = api.init_nova_clients('2', session_list)
for nova in nova_client_list:
	print nova.flavors.list()

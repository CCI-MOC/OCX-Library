import phaseOneOCX
# Socks
url_list = ['http://140.247.152.150:5000/v2.0', 'http://140.247.152.35:5000/v2.0' , 'http://140.247.152.189:5000/v2.0']

tenant_name ='admin'
username = 'admin'
password = 'ocx'


session_list = phaseOneOCX.init_sessions(username, password,tenant_name,url_list)

nova_client_list  = phaseOneOCX.init_nova_clients('2', session_list)
for nova in nova_client_list:
	print nova.flavors.list()


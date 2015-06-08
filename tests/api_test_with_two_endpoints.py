import api
# Socks
url_list = ['http://140.247.152.150:5000/v2.0', 'http://140.247.152.35:5000/v2.0' , 'http://140.247.152.189:5000/v2.0']

tenant_name ='admin'
username = 'admin'
password = 'ocx'


session_list = phaseOneOCX.init_sessions(username, password,tenant_name,url_list)

#nova
nova_client_list  = phaseOneOCX.init_nova_clients('2', session_list)
nova_service_object_list = phaseOneOCX.nova_service_version_2(nova_client_list,"flavors")
for service in nova_service_object_list:
	print service.list()

#keystone
keystone_client_list = phaseOneOCX.init_keystone_clients(username, password,tenant_name,url_list)
keystone_service_object_list = phaseOneOCX.keystone_service(keystone_client_list,"users")
for keystone in keystone_service_object_list:
	for member in keystone.list():
		print member.name

#glance
glance_client_list = phaseOneOCX.init_glance_clients(keystone_client_list)
glance_service_object_list = phaseOneOCX.glance_service(glance_client_list,"images")
for service in glance_service_object_list:
	print list(service.list())[0]['name']

#cinder
cinder_client_list = phaseOneOCX.init_cinder_clients(keystone_client_list)
cinder_service_object_list = phaseOneOCX.cinder_service(cinder_client_list,"volumes")
for service in cinder_service_object_list:
	print service.list()
	
#swift
swift_client_list = phaseOneOCX.init_swift_clients(keystone_client_list)
swift_service_object_list = phaseOneOCX.swift_service(swift_client_list,"head_account")
for service in swift_service_object_list:
	print service
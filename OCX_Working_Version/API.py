from keystoneclient.auth.identity import v2
import novaclient.v2.client as nvclient
import keystoneclient.v2_0.client as ksclient
from keystoneclient import session
from novaclient import client
import glanceclient.v2.client as glclient
from cinderclient import client as cinder_client
from swiftclient import client as swift_client


#Session
def init_sessions(username, password,tenant_name, auth_urls):
	session_list = []
	for url in auth_urls:

		auth = v2.Password(auth_url=url,
	                       username=username,
	                       password=password,
	                       tenant_name=tenant_name)

		sess = session.Session(auth=auth)
		session_list.append(sess)

	return session_list


def init_nova_clients(version, session_list):
	nova_client_list = []
	for session in session_list:
		print session_list.index(session)
		#nova = client.Client(version, session = session)
		nova = getattr(client,"Client")(version,session=session)
		#print nova
		#myfunction = getattr(nova, "flavors")
		#print myfunction.list()
		nova_client_list.append(nova)

	return nova_client_list

#result = getattr(obj,"method")(nova_client_list)

#myclient = getattr(client, Client)(client init args)

#myfunction = getattr(myclient, function_name)

#myreturnval = myclient.myfunction(func arg list)

def nova_service(nova_client_list,service):
	for nova in nova_client_list:
		service_object = getattr(nova,service)
		print service_object
		
		
def nova_service_version_2(nova_client_list,service):
	service_list_object = []
	for nova in nova_client_list:
		service_object = getattr(nova,service)
		service_list_object.append(service_object)
	return service_list_object
	
#keystone
def init_keystone_clients(username, password,tenant_name,auth_urls):
	keystone_client_list=[]
	for url in auth_urls:
 		keystone = ksclient.Client(auth_url = url, username = username,
 			password = password, tenant_name = tenant_name)
 		keystone_client_list.append(keystone)

	return keystone_client_list
	
def keystone_service(keystone_client_list,service):
	service_list_object = []
	for keystone in keystone_client_list:
		service_object = getattr(keystone,service)
		service_list_object.append(service_object)
	return service_list_object

#glance
def init_glance_clients(keystone_client_list):
	glance_client_list = []
	for keystone in keystone_client_list:
		glance_endpoint = keystone.service_catalog.url_for(service_type='image')
		glance = glclient.Client(glance_endpoint, token = keystone.auth_token)
		glance_client_list.append(glance)

	return glance_client_list

def glance_service(glance_client_list,service):
	service_list_object = []
	for glance in glance_client_list:
		service_object = getattr(glance,service)
		service_list_object.append(service_object)
	return service_list_object
	
#cinder
def init_cinder_clients(keystone_client_list):
	cinder_client_list = []
	for keystone in keystone_client_list:
		cinder = cinder_client.Client('1',keystone.username,keystone.password,keystone.tenant_name,keystone.auth_url)
		cinder_client_list.append(cinder)
	return cinder_client_list
	
def cinder_service(cinder_client_list,service):
	service_list_object = []
	for cinder in cinder_client_list:
		service_object = getattr(cinder,service)
		service_list_object.append(service_object)
	return service_list_object
	
#swift
def init_swift_clients(keystone_client_list):
	swift_client_list = []
	for keystone in keystone_client_list:
		swift = swift_client.Connection(auth_version ='2.0', user= keystone.username,key= keystone.password,tenant_name = keystone.tenant_name,authurl= keystone.auth_url)
		swift_client_list.append(swift)
	return swift_client_list
	
def swift_service(swift_client_list,service):
	service_list_object = []
	for swift in swift_client_list:
		service_object = getattr(swift,service)
		service_list_object.append(service_object)
	return service_list_object

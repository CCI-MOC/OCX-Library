from keystoneclient.auth.identity import v2
import novaclient.v2.client as nvclient
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient

from keystoneclient import session
from novaclient import client


#Session
def init_sessions(username, password,tenant_name,auth_urls):
	session_list =[]
	for url in auth_urls:

		auth = v2.Password(auth_url=url,
	                       username=username,
	                       password=password,
	                       tenant_name=tenant_name)

		sess = session.Session(auth=auth)
		session_list.append(sess)

	return session_list
#keystone
def init_keystone_clients(username, password,tenant_name,auth_urls):
	keystone_client_list=[]
	for url in auth_urls:
 		keystone = ksclient.Client(auth_url = url, username = username,
 			password = password, tenant_name = tenant_name)
 		keytone_client_list.append(keystone)

	return keystone_client_list
#glance
def init_glance_clients(keystone_client_list):
	glance_client_list = []
	for keystone in keystone_client_list:
		glance_endpoint = keystone.service_catalog.url_for(service_type='image')
		glance = glclient.Client(glance_endpoint, token = keystone.auth_token)
		glance_client_list.append(glance)

	return glance_client_list

#nova
def init_nova_clients(version, session_list):
	nova_client_list = []
	for session in session_list:
		nova = client.Client(version, session=session_list)
		nova_client_list.append(nova)

	return nova_client_list

## Need to Discuss
#nova
def init_cinder_clients():

	return cinder_client_list	
#token
# def init_tokens(username, password,tenant_name,auth_urls):
# 	token_list = []
# 	for url in auth_urls:
# 		keystone = ksclient.Client(auth_url = url, username = username,
# 			password = password, tenant_name = tenant_name)
# 		token = keystone.auth_tokens
# 		token_list.append(token)
	
# 	return token_list

    Status API Training Shop Blog About 


from keystoneclient.auth.identity import v2
import novaclient.v1_1.client as nvclient
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient

from keystoneclient import session
from novaclient import client


session_list = []
def init_sessions(tenant_name, username, password, auth_urls):
	
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
		nova = client.Client(version, session)
		nova_client_list.append(nova)

	return nova_client_list


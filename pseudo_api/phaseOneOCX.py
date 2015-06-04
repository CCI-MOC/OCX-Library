from keystoneclient.auth.identity import v2
import novaclient.v2.client as nvclient
import keystoneclient.v2_0.client as ksclient
from keystoneclient import session
from novaclient import client


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
		nova = client.Client(version, session = session)
		nova_client_list.append(nova)

	return nova_client_list


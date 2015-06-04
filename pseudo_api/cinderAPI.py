from cinderclient import client as CClient
class AuthInfo:
    username = none
	password = none
	tenant_name = none
	auth_url = none
	
	def __init__(self,username,password,tenant_name,auth_url):
	    self.username = username
		self.password = password
		self.tenant_name = tenant_name
		self.auth_url = auth_url
	
def cinder_client_api(list_of_AuthInfo)
    cinder_client_list = []
    for authinfo_obj in list_of_AuthInfo:
	    cinder = client.Client('1', username = authinfo_obj.username, password = authinfo_obj.password, tenant_name = authinfo_obj.tenant_name,auth_url = authinfo_obj.auth_url)
		cinder_client_list.append(cinder)
	return cinder_client_list
from keystoneclient.auth.identity import v2
# import novaclient.v2.client as nvclient
# import glanceclient.v2.client as glclient
# import keystoneclient.v2_0.client as ksclient

from keystoneclient import session
from novaclient import client
import api 

# url_list = ['http://140.247.152.150:5000/v2.0', 'http://140.247.152.35:5000/v2.0' ]

# tenant_name ='admin'
# username = 'admin'
# password = 'ocx'


# session_list = api.init_sessions(username, password,tenant_name,url_list)

# nova_client_list  = api.init_nova_clients('2', session_list)
# for nova in nova_client_list:
# 	print nova.flavors.list()

url = 'http://140.247.152.207:5000/v2.0'

tenant_name ='admin'
username = 'xuh'
password = 'xuhang0507'

auth = v2.Password(auth_url=url,
                   username=username,
                   password=password,
                   tenant_name=tenant_name)

sess = session.Session(auth=auth)

nova = client.Client("2", session=sess,timeout=0)

print nova.flavors.list()

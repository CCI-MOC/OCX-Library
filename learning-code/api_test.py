from keystoneclient.auth.identity import v2
# import novaclient.v2.client as nvclient
# import glanceclient.v2.client as glclient
# import keystoneclient.v2_0.client as ksclient

from keystoneclient import session
from novaclient import client

#import socket
#import socks
import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 7000)
socket.socket = socks.socksocket

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.settimeout(10)

url = 'http://140.247.152.207:5000/v2.0'

tenant_name ='moc-ops-experiments'
username = 'guptaankita'
password = 'os'

auth = v2.Password(auth_url=url,
                   username=username,
                   password=password,
                   tenant_name=tenant_name)

sess = session.Session(auth=auth)

nova = client.Client("2", session=sess)

print nova.flavors.list()

nova.servers.add_fixed_ip('463f0964-491b-4fcd-8258-aff9825e49e5')

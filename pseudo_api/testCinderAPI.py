import cinderAPI
auth_info_list = []
# enter your credentials 
auth_info = AuthInfo() 
auth_info_list.append(auth_info)
cinder_list = cinderAPI.cinder_client_api
for cinder_client in cinder_list:
    cinder_client.volumes.list()
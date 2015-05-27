#function for using functionalities of nova client api
/*where list of keystone token is the token for each unique endpoint and each 
endpoint has same username, password and tenant_name*/
```python
function novaClientAPI(project_name, keystone_token_list):
    /*to use functionalities of nova API, we need to create a nova client first*/
    For token in keystone_token_list
        new_nova_client = create_nova_client(project_name,token)
        nova_client_list.add(new_nova_client)
    /*to get the list of VMs*/
    for nova_client in nova_client_list
        endpoint_VMs = nova_client.list()
        all_VMs_list.add(all_VMs)
```
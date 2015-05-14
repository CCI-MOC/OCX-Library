# USAGE:
The first call of every service is to open a client with the service.
Every subsequent call is made on the client. For example:
nova_client = ocx.create_nova_client(project, keystone_token)
my_vm = nova_client.default_create_vm(vm_name)

# Library APIs:
### Service Directory API
#### Operational API 
* create_service(service_name, endpoint, optional_args?)
    return success/failure
* delete_service(service_name)
    return success/failure
* update_service(service_name, config_options)
    return success/failure

#### Query API 
* list_services(filter=None)
    return json list of services
* show_service(service_name)
    return json info of services


### Keystone API
#### Operational API 
* create_keystone_client(user_name, password)
    return keystone client for further operations
* get_token(user_name, password)
    return keystone token for opening rest of clients for projects
* add_user_to_project(user_name, project, token)
    return success/failure
* remove_user_from_project(user_name, project, token) 
    return success/failure

#### Query API 
* list_projects(token)
    return list of projects

### Nova API
#### Operational API 
* create_nova_client(project, keystone_token)
    return nova client for further operations
* create_vm(vm_name, image, flavor, security_groups, key_name, nics)
    return success/failure
* default_create_vm(vm_name)
    return success/failure
* delete_vm(vm_name)
    return success/failure
* attach_volume(vm_name, volume_name) 
    return success/failure

#### Query API 
* list_project_vms(project)
    return full list of vms, from all nova instances
* show_vm(vm_name)
    return json blob of vm details (maybe optional args for specific details)

### Neutron API
#### Operational API 
* create_neutron_client(project, keystone_token)
    return neutron client for further operations
* create_network(network_name, subnet)
    return success/failure
* delete_network(network_name)
    return success/failure
* create_router(router_name, private_subnet, public_subnet)
    return success/failure
* delete_router(router_name)
    return success/failure
* create_port(port_name, vm_name, network_name)
    return success/failure
* delete_port(port_name)
    return success/failure

#### Query API 
* list_networks()
* list_routers()
* list_ports()
* show_topology()?

### Cinder API
#### Operational API 
* create_cinder_client(project, keystone_token)
* create_volume()
* delete_volume()
* create_snapshot()
* delete_snapshot()

#### Query API 
* list_volumes()
* list_snapshots()

### Swift API
#### Operational API 
* create_swift_client(project, keystone_token)
* create_container()
* delete_container()
* upload_object()
* download_object()
* delete_object()

#### Query API
* list_containers()
* list_objects()

### Glance API
#### Operational API 
* create_glance_client(project, keystone_token)
* upload_image()
* delete_image()

#### Query API
* list_images()

TODO:

- think about how to aggregate services at a higher level - not re-implementing calls
- look at keystone service dir api for inspiration
- think about minimum set of meta-data necessary for a service
- want updates for not just subscribed services
- where to store project specific endpoint - sd?

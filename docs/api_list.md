# USAGE:
The first call of every service is to open a client with the service.
Every subsequent call is made on the client. For example:
nova_client = ocx.create_nova_client(project, keystone_token)
my_vm = nova_client.default_create_vm(vm_name)

# Library APIs:
### Service Directory API
#### Operational API 
* create_service(service_name, endpoint, optional_args?)
    return success OR failure
* delete_service(service_name)
    return success OR failure
* update_service(service_name, config_options)
    return success OR failure

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
    return success OR failure
* remove_user_from_project(user_name, project, token) 
    return success OR failure

#### Query API 
* list_projects(token)
    return list of projects

### Nova API
#### Operational API 
* create_nova_client(project, keystone_token)
    return nova client for further operations
* create_vm(vm_name, image, flavor, security_groups, key_name, nics)
    return success OR failure
* default_create_vm(vm_name)
    return success OR failure
* delete_vm(vm_name)
    return success OR failure
* attach_volume(vm_name, volume_name) 
    return success OR failure

#### Query API 
* list_vms()
    return full list of vms, from all nova instances
* show_vm(vm_name)
    return json blob of vm details (maybe optional args for specific details)

### Neutron API
#### Operational API 
* create_neutron_client(project, keystone_token)
    return neutron client for further operations
* create_network(network_name, subnet)
    return success OR failure
* delete_network(network_name)
    return success OR failure
* create_router(router_name, private_subnet, public_subnet)
    return success OR failure
* delete_router(router_name)
    return success OR failure
* create_port(port_name, vm_name, network_name)
    return success OR failure
* delete_port(port_name)
    return success OR failure

#### Query API 
* list_networks()
    return json list of networks
* list_routers(network_name=ALL)
    return json list of routers
* list_ports(subnet=ALL)
    return json list of ports 
* show_topology()?
    return json list of connections?

### Cinder API
#### Operational API 
* create_cinder_client(project, keystone_token)
    return cinder client for further operations
* create_volume(volume_name, size, initial_data)
    return volume_url OR failure
* delete_volume(volume_name)
    return success OR failure
* upload_volume(volume_name, volume_url)
    return new_volume_url OR failure
* create_snapshot(volume_name)
    return volume_url OR failure
* delete_snapshot(volume_name)
    return success OR failure

#### Query API 
* list_volumes()
    return json list of volumes
* list_snapshots()
    return json list of snapshots 

### Swift API
#### Operational API 
* create_swift_client(project, keystone_token)
    return swift client for further operations OR failure
* create_container(container_name, size, initial_data)
    return container_url OR failure
* delete_container(container_name)
    return success OR failure
* upload_container(container_name, container_url)
    return new_container_url OR failure
* upload_object(container_name, object_name)
    return object_url OR failure
* download_object(container_name, object_name)
    return object OR failure
* delete_object(container_name, object_name)
    return success OR failure

#### Query API
* list_containers()
    return json list of containers OR failure
* list_objects(container_name)
    return json list of objects OR failure

### Glance API
#### Operational API 
* create_glance_client(project, keystone_token)
    return glance client for further operations OR failure
* upload_image(image_name, image_url)
    return new_image_url OR failure
* delete_image(image_name)
    return success OR failure

#### Query API
* list_images()
    return json list of images OR failure

TODO:

- think about how to aggregate services at a higher level - not re-implementing calls
- look at keystone service dir api for inspiration
- think about minimum set of meta-data necessary for a service
- want updates for not just subscribed services
- where to store project specific endpoint - sd?

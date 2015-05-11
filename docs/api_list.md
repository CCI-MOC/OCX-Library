# Library APIs:
### Service Directory API
#### Operational API 
* create_service()
* delete_service()
* create_endpoint()
* delete_endpoint()

#### Query API 
* list_services()
* show_service()
* list_free_services()

### Keystone API
#### Operational API 
* get_token()
* add_user_to_project()
* remove_user_from_project() 

#### Query API 
* list_projects()

### Nova API
#### Operational API 
* create_vm()
* default_create_vm()
* delete_vm()
* attach_volume() 
* create_firewall_rule()
* delete_firewall_rule()

#### Query API 
* list_project_vms()
* show_vm()

### Neutron API
#### Operational API 
* create_network()
* delete_network()
* create_router()
* delete_router()
* create_port()
* delete_port()

#### Query API 
* list_networks()
* list_routers()
* list_ports()
* show_topology()?

### Cinder API
#### Operational API 
* create_volume()
* delete_volume()
* create_snapshot()
* delete_snapshot()

#### Query API 
* list_volumes()
* list_snapshots()

### Swift API
#### Operational API 
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
* upload_image()
* delete_image()

#### Query API
* list_images()


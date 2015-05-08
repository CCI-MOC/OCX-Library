# Library APIs:
## Keystone API
### Operational API 
* get_token()

### Query API 
* list_projects()
* add_user_to_project()
* remove_user_from_project() 

## Service Directory API
### Operational API 
* create_service()
* delete_service()

### Query API 
* list_services()
* list_free_services()

## Nova API
### Operational API 
* create_vm()
* default_create_vm()
* delete_vm()
* attach_volume() 

### Query API 
* list_project_vms()

## Neutron API
### Operational API 
* create_network()
* delete_network()
* create_router()
* delete_router()
* create_firewall_rule()
* delete_firewall_rule()

### Query API 
* list_networks()
* list_routers()
* show_topology()?

## Cinder API
### Operational API 
* create_volume()
* delete_volume()
* take_snapshot()
* delete_snapshot()

### Query API 
* list_volumes()
* list_snapshots()

## Swift API
### Operational API 
* create_container()
* delete_container()
* upload_object()
* download_object()
* delete_object()

### Query API
* list_containers()
* list_objects()

## Swift API

## Glance API
### Operational API 
* upload_image()
* delete_image()

### Query API
* list_images()


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

		create(name, image, flavor, meta=None, files=None, reservation_id=None, min_count=None, max_count=None, security_groups=None, userdata=None, key_name=None, availability_zone=None, block_device_mapping=None, block_device_mapping_v2=None, nics=None, scheduler_hints=None, config_drive=None, disk_config=None, **kwargs)		
			Create (boot) a new server.
			Parameters: * name - Something to name the server.
						* image - The Image to boot with
						* flavor - The Flavor to boot onto.
						* meta - A dict of arbitrary key/value metadata to store for this server. 
						Both keys and values must be <=255 characters.
						* file - A dict of files to overrwrite on the server upon boot. 
						Keys are file names (i.e. /etc/passwd) and values are the file contents 
						(either as a string or as a file-like object). 
						A maximum of five entries is allowed, and each file must be 10k or less.
						* reservation_id – a UUID for the set of servers being requested.
						* min_count – (optional extension) The minimum number of servers to launch.
						* max_count – (optional extension) The maximum number of servers to launch
						* security_groups – A list of security group names
						* userdata – user data to pass to be exposed by the metadata server this can be a file type object as well or a string.
						* key_name – (optional extension) name of previously created keypair to inject into the instance.
						* availability_zone – Name of the availability zone for instance placement.
						* block_device_mapping – (optional extension) A dict of block device mappings for this server.
						* block_device_mapping_v2 – (optional extension) A dict of block device mappings for this server.
						* nics – (optional extension) an ordered list of nics to be added to this server, with information about connected networks, fixed IPs, port etc.
						* scheduler_hints – (optional extension) arbitrary key-value pairs specified by the client to help boot an instance
						* config_drive – (optional extension) value for config drive either boolean, or volume-id
						* disk_config – (optional extension) control how the disk is partitioned when the server is created. possible values are ‘AUTO’ or ‘MANUAL’.	
			Location in novaclient: Server

		create_image(server, image_name, metadate=None)
			Snapshot a server. 
			Parameters: * server - The Server (or its ID) to share onto.
						* image_name - Name to give the snapshot image
						* metadata - Metadata to give newly-created image entity





* default_create_vm()
		
* delete_vm()

		 delete(server)      
		 	Delete (i.e. shut down and delete the image) this server.
		 	Parameter: server
		 	Location in novaclient: Servers
		 
		 force_delete(server)
		 	Force delete the server
		 	Parameter: server
		 	Location in novaclient: Servers
		 

* get_vm()

		get(server)
			Get a server
			Parameters: server - ID of the Server to get
			Return type: Server
			Location in novaclient: Servers

* get_vm_password()

		get_password(serer,private_key = None)
			Get admin password of an server
			Parameters: * server - the Sever(or its ID) for which the admin password is to be returned
						* private_ket - The private key to decrypt password (optional)
			Return: the admin password of an instance in the clear if private_key is provided, returns the ciphered password otherwise.
			Location in novaclient: Servers


* reboot_vm()

		reboot(server, reboot_type="SOFT")
			Reboot a server
			Parameters: * server - The Server (or its ID) to share onto.
						* reboot_type - either REBOOT_SOFT for a software-level reboot, or REBOOT_HARD for a virtual power cycle hard reboot.
			Location in novaclient: Servers			

* resize_vm()

		resize(server, flavor, disk_config=None, **kwargs)
			Resize a server's resources
			Parameters: * server - The Server (or its ID) to share onto.
						* flavor - the Flavor(or its ID) to resize to.
						* disk_config - partitioning mode to use on the rebuilt server. Valid values are ‘AUTO’ or ‘MANUAL’
			Location in novaclient: Servers
			Detail: Until a resize event is confirmed with confirm_resize(), the old server will be kept around and you’ll be able to roll back to the old flavor quickly with revert_resize(). All resizes are automatically confirmed after 24 hours.


* start_vm()

		start(server)
			Start the server
			Location in novaclient: Servers


* stop_vm()
		
		stop(server)
			Stop the server
			Location in novaclient: Servers

* suspend_vm()

		suspend(server)
			Suspend the server
			Location in novaclient: Servers

* list_volume()

		list(detailed=Ture, search_opts=None)
			Get a list of all volumes.
			Return type:list of Volume
			Location in novaclient: Volume

* attach_volume() 

		create_server_volume(server_id , volume_id, device)
			Attach a volume identified by the volume ID to the given server ID
			Parameters: * server_id – The ID of the server
						* volume_id – The ID of the volume to attach
						* device – The device name
			Return type: Volume

### Query API 
* list_project_vms()

	

* list_volumes()
		
		list(detailed=True, search_opts=None)
		Get a list of all volumes.
		Return type:list of Volume








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


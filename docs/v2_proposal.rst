=======================
OCX-Library V2 Proposal
=======================

Purpose
-------
* Enables the OpenStack API to address multiple OpenStack endpoints
* Acts as a wrapper around underlying "python-[service]client" 
  - Must import all of the client libraries for all services used, in addition to ours

Code control flow:
------------------
* Iterated call:
    - First call
        + Initialize x keystone clients (first one with credentials, rest using SAML)
        + Initialize x service clients, one for each keystone client
        + Call the function with kwargs on the x service clients
    - Every subsequent call, until clients time out
        + Retrieve the service clients stored in the user's running software 
        + Call the function with kwargs on the x service clients
* Single call:
    - Initialize the keystone client on your "home" keystone, and one client from the keystone of the provider of the service you would like to use (eventually using SAML for 2nd)
    - Initialize service client with 2nd keystone client
    - Call function on the underlying service
    
* Once clients time out, we inform the user, and ask if they would like to re-initialize the clients

Necessary Functions:
--------------------
* Iterated
    - init_keystone_clients(home_auth_url, auth_url_dict, user_name, password)
        + return keystone_client_dict
    - init_service_clients(keystone_client_dict, service)
        + return service_client_dict [dict of nova clients, neutron clients, etc...]
    - call_services(service_client_dict, function, args, kwargs)
        + return aggregate_of_return_values
* Single service
    - init_keystone_client(home_auth_url, remote_auth_url, user_name, password)
        + return remote_keystone_client
    - init_service_client(remote_keystone_client, service)
        + return service_client 
    - call_service(service_client, function, args, kwargs)
        + return underlying_function_return 
* Cross-OpenStack functions
    - list_services(keystone_client_dict, service=ALL)
        + return dict_of_authorized_services
    - create_private_network( args? )
        + return success / failure?

Issues to be addressed:
-----------------------
* Currently every call is being done on every endpoint or one endpoint... should we try to limit this scope? Have an easy function to grab a set of service clients based on keys in dict? 
    - make a new set of clients for a more limited scope?
* Different services might take different lengths of time to return, or might not return at all...
    - Try-catch to avoid a user's program hanging?
    - Asynchronous calls?
* Client time-out is based on keystone token timeout length, might happen at different intervals for different clients in our list...
    - Better error handling for specifically telling if its the service thats not returning or that you are no longer authorized?

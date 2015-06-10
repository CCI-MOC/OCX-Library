=======================
OCX-Library V2 Proposal
=======================

The intention of this library is to act as a wrapper around the underlying client libraries.
A user will import all of the "python-[service]client" libraries they would like to use, in addition to ours. 
Our library relies on the existance of the other client libraries in the python environment.

Code control flow:
------------------
* First call
    - initialize x keystone clients
    - initialize x service clients, one for each keystone client
    - call the function with kwargs on the x service clients
* Every subsequent call, until clients time out
    - retrieve the service clients stored in the user's running software 
    - call the function with kwargs on the x service clients
* Once clients time out, we inform the user, and ask if they would like to re-initialize the clients

Necessary Functions:
--------------------
* init_keystone_clients(auth_url_list, user_name, password)
    - return keystone_client_list
* init_service_clients(keystone_client_list, service)
    - return service_client_list [list of nova clients, neutron clients, etc...]
* call_service(service_client_list, function, args, kwargs)
    - return aggregate_of_return_values

Issues to be addressed:
-----------------------
* Currently every call is being done on every endpoint you want to initialize... should we try to limit this scope? At which point? 
    - Some easy way to filter the list of their clients passed to a service function call?
        + For instance, want to create a new nova instance in one of our initialized clients, not in every nova we have access to...
    - make a new set of clients for a more limited scope?
* Different services might take different lengths of time to return, or might not return at all...
    - Try-catch to avoid a user's program hanging?
    - Asynchronous calls?
* Client time-out is based on keystone token timeout length, might happen at different intervals for different clients in our list...
    - Better error handling for specifically telling if its the service thats not returning or that you are no longer authorized?

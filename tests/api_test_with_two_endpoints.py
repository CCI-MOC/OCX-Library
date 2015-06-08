# Copyright 2013-2014 Massachusetts Open Cloud Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.  See the License for the specific language
# governing permissions and limitations under the License.

"""Unit tests for api.py"""

from ocx-library import api
import pytest




url_list = ['http://140.247.152.150:5000/v2.0', 'http://140.247.152.35:5000/v2.0' , 'http://140.247.152.189:5000/v2.0']

tenant_name ='admin'
username = 'admin'
password = 'ocx'


session_list = api.init_sessions(username, password,tenant_name,url_list)

#nova
nova_client_list  = api.init_nova_clients('2', session_list)
nova_service_object_list = api.nova_service_version_2(nova_client_list,"flavors")
for service in nova_service_object_list:
	print service.list()

#keystone
keystone_client_list = api.init_keystone_clients(username, password,tenant_name,url_list)
keystone_service_object_list = api.keystone_service(keystone_client_list,"users")
for keystone in keystone_service_object_list:
	for member in keystone.list():
		print member.name

#glance
glance_client_list = api.init_glance_clients(keystone_client_list)
glance_service_object_list = api.glance_service(glance_client_list,"images")
for service in glance_service_object_list:
	print list(service.list())[0]['name']

#cinder
cinder_client_list = api.init_cinder_clients(keystone_client_list)
cinder_service_object_list = api.cinder_service(cinder_client_list,"volumes")
for service in cinder_service_object_list:
	print service.list()
	
#swift
swift_client_list = api.init_swift_clients(keystone_client_list)
swift_service_object_list = api.swift_service(swift_client_list,"head_account")
for service in swift_service_object_list:
	print service
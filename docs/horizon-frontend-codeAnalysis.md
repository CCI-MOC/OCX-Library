## horizon code analysis 

### Section 1
### Overview 

The code is located in: 
**https://github.com/openstack/horizon/**

	The basic structure of the code is:
	*	horizon-master
		*	doc
		*	horizon
		*	openstack_dashboard
		*	tools



	
	The front end part is mostly located in:
	*	horizon-master
		*	openstack_dashboard
			*	dashboards
				*	admin
					*	defaults
						*	templates
						*	panel.py
						*	tables.py
						*	tabs.py
						*	tests.py
						*	urls.py
						*	views.py
						*	workflows.py

### Section 2
### Tutorial: add a montoring panel to the dashboard(html page)

##### Step 1: declare panel
	
Go to: 
horizon-master - openstack_dashboard - dashboards - admin - dashboard.py

Open the dashboard.py and you will see a class called
**class SystemPanels**
This is where they define different panels.
So you should add "monitoring" into the list 
now the code looks like this:

	class SystemPanels(horizon.PanelGroup):
    slug = "admin"
    name = _("System")
    panels = ('overview', 'metering', 'hypervisors', 'aggregates',
              'instances', 'volumes', 'flavors', 'images',
              'networks', 'routers', 'defaults', 'metadata_defs', 'info', 'monitoring')


#### Step 2:create the "mintoring" folder 

Go to:horizon-master - openstack_dashboard - dashboards - admin
in the admin directory, there are list of folders, for example:

*	admin
	*	aggregates
	*	defaults
	*	flavors
	*	hypervisors
	*	images

now create a empty folder under the admin directory , named as "monitoring"
now under the admin, it should look like 

*	admin
	*	monitoring
	*	aggregates
	*	defaults
	*	flavors
	*	hypervisors
	*	images


#### Step 2:creates the panel.py

Go to: horizon-master - openstack_dashboard - dashboards - admin - monitoring , which is the folder you created in step 2
in the monitoring folder, create a new file called panel.py
write the following code:

	 from django.utils.translation import ugettext_lazy as - # noqa
     import horizon
     from openstack_dashboard.dashboards.admin import dashboard

     class Monitoring(horizon.Panel):
     	name = _("Monitoring")
     	slug = 'monitoring'

     dashboard.Admin.register(Monitoring)


#### Step 3: create the url.py

Go to: horizon-master - openstack_dashboard - dashboards - admin - monitoring folder
create a file named urls.py

write the following code:
	
	in the monitoring directory, created urls.py
	
	from django.conf.urls.defaults import patterns # noqa
	from django.conf.urls.defaults import url # noqa
	from .views import IndexView

	urlpatterns = patterns('',
		url(r'^$', IndexView.as_view(), name= 'index')


#### Step 4: create the tables.py

Go to: horizon-master - openstack_dashboard - dashboards - admin - monitoring folder
create a file named tables.py

write the following code:

	import logging
	from django.utils.translation import ugettext_lazy as _ # noqa
	from horizon import tables

	LOG = logging.getLogger(_name_)

	class MonitoringTable(tables.DataTable):
		resources = tables.Column("resources", verbose_name=_("Resources"))
		percent = tables.Column("percent", verbose_name=_("Percent"))

		class Meta:
			name = 'monitoring'
			verbose_name = _("Monitoring")

#### Step 5: create the view.py

Go to: horizon-master - openstack_dashboard - dashboards - admin - monitoring folder
create a file named views.py

write the following code:

	import logging

	from django.utils.translation import ugettext_lazy as _ # noqa
	from horizon import tables
	from openstack_dashboard.dashboards.admin.monitoring impot tables as project_tables

	LOG = logging.getLogger(_name_)

	class IndexView(tables.DataTableView):
		table_class = project_tables.MonitoringTable
		template_name = 'admin/monitoring/index.html'
		def get_data(self):
			resources = []
			return resources











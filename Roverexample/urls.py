from django.conf.urls import patterns, include, url
from dogapp.views import search, listall, addNew

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Roverexample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^time/$', current_datetime),
	
    url(r'^admin/', include(admin.site.urls)),
	url(r'^search/$', search),
	url(r'^listall/$', listall),
	url(r'^addNew/$', addNew),
)

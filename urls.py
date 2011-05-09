import os.path
from django.conf.urls.defaults import *
from bookmarks.views import *

site_media = os.path.join(
	os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
	url(r'^$', main_page),
	url(r'^user/(\w+)/$', user_page),
	url(r'^login/$','django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':site_media}),
)

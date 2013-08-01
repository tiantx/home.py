from django.conf.urls import patterns,url

urlpatterns = patterns('rest.views',
	(r'^snippets/$', 'snippet_list'),
	(r'^snippet/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)

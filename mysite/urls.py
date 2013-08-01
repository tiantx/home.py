from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.index'),
   url(r'^uploads/(?P<path>.*)$',
       'django.views.static.serve',
       {'document_root':settings.CKEDITOR_UPLOAD_PATH}),
   (r'^ckeditor/', include('ckeditor.urls')),
   (r'^ckeditor_test$', 'mysite.views.ckeditor_test'),
   (r'^rest_test/', include('rest.urls')),
   (r'^ajax_index/$', 'mysite.views.ajax_index'),
   (r'^ajax_echo/$', 'mysite.views.ajax'),
)

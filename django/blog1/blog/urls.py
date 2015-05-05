from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sblog/', include('sblog.urls')),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'./static'}),
    (r'^aaa/(?P<path>.*)$','django.views.static.serve',{'document_root':"./templates"}),
    
)

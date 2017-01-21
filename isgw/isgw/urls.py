from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isgw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^deviceinfo$', 'Smartelec.views.deviceInfo',name="deviceInfo"),
    url(r'^userinfo$', 'Smartelec.views.userInfo',name="userInfo"),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isgw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^weather$', 'Smartelec.views.datagerator', name='datagerator') , 

    url(r'^rate$', 'Smartelec.views.realgenerator', name='realgenerator') , 
    url(r'^ideal$', 'Smartelec.views.ideal_rate', name='realgenerator') , 
)

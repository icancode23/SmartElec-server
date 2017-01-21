from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isgw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^weather$', 'Smartelec.views.datagerator', name='datagerator') , 

    url(r'^rate$', 'Smartelec.views.realgenerator', name='realgenerator') , 
    url(r'^ideal$', 'Smartelec.views.ideal_surplus', name='realgenerator') , 

    url(r'^deviceinfo$', 'Smartelec.views.deviceInfo',name="deviceInfo"),
    url(r'^userinfo$', 'Smartelec.views.userInfo',name="userInfo"),
<<<<<<< HEAD
    url(r'^weather$', 'Smartelec.views.datagerator',name="datagenerator"),
    url(r'^rate$', 'Smartelec.views.realgenerator',name="realgenerator"),
    url(r'^ideal$', 'Smartelec.views.ideal_rate',name="realgenerator1"),
=======
    url(r'^exact$', 'Smartelec.views.exact',name="exact"),

>>>>>>> 372453d2999a244ac536ba8d5ba0e6dca286fb87
)

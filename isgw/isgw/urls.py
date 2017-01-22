from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isgw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^weather$', 'Smartelec.views.datagerator', name='datagerator') , #giving 3 coordinates, 
    url(r'^idealsurplus$', 'Smartelec.views.ideal_surplus', name='realgenerator') , #giving ideal surplus ammount for the day

    url(r'^deviceinfo$', 'Smartelec.views.deviceInfo',name="deviceInfo"),
    url(r'^userinfo$', 'Smartelec.views.userInfo',name="userInfo"),

    url(r'^exactprice$', 'Smartelec.views.exactPrice',name="exactprice"), #exact price at the moment
    url(r'^idealrate$', 'Smartelec.views.exact',name="exact"),#giving ideal minimum price for comparison


)

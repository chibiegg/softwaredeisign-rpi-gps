from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'gpsnow.views.index', name='index'),
    url(r'^trasponder/waypoint/$', 'gpsnow.transponder.views.add_waypoint', name='add_waypoint'),
    url(r'^api/waypoints/latest/$', 'gpsnow.views.waypoint_latest', name='waypoint_latest'),
    url(r'^api/transponders/$', 'gpsnow.views.list_transponders', name='list_transponders'),
    url(r'^api/transponders/([^/]+)/marker.png$', 'gpsnow.views.transponder_marker', name='transponder_marker'),
    url(r'^api/transponders/([^/]+)/marker_disabled.png$', 'gpsnow.views.transponder_marker', kwargs={"disabled":True}, name='transponder_marker_disabled'),

    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()


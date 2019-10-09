from django.conf.urls import url
from meyita import views

urlpatterns = [
    #cal urls
    url(r'^cal/$', views.calList.as_view(), name=views.calList.name),
    url(r'^cal/(?P<pk>[0-9]+)$', views.calDetail.as_view(), name=views.calDetail.name),
    #cpl urls
    url(r'^cpl/$', views.cplList.as_view(), name=views.cplList.name),
    url(r'^cpl/(?P<pk>[0-9]+)$', views.cplDetail.as_view(), name=views.cplDetail.name),
    #cpb urls
    url(r'^cpb/$', views.cpbList.as_view(), name=views.cpbList.name),
    url(r'^cpb/(?P<pk>[0-9]+)$', views.cpbDetail.as_view(), name=views.cpbDetail.name),
    #cdl urls
    url(r'^cdl/$', views.cdlList.as_view(), name=views.cdlList.name),
    url(r'^cdl/(?P<pk>[0-9]+)$', views.cdlDetail.as_view(), name=views.cdlDetail.name),
    #base url
    url(r'^$', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
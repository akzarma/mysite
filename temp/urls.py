from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "home"

urlpatterns = [


    url(r'^$', views.home, name="home"),

    url(r'^action/$', views.action, name="action"),

    #all student list page /test/all
    url(r'^all/$', views.test, name='all_students'),

    # /test/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='student-delete'),


    # /test/19
    url(r'^(?P<student_id>[0-9]+)/$', views.DetailView, name='details'),

    # # /test/status=true   or false
    # url(r'^/status=(?P<submit_status>)/$', views.homecheck, name='check'),



]




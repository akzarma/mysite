from django.conf.urls import url
from . import views

app_name = "home"

urlpatterns = [


    url(r'^$', views.home, name="home"),

    url(r'^action/$', views.action, name="action"),

    #all student list page /test/details
    url(r'^details/$', views.DetailView.as_view(), name='details'),

    #ye abhi baaki hai .............................krra hu abhi
    url(r'student/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student-update'),

]


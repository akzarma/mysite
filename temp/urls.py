from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "home"

urlpatterns = [

    url(r'^$', views.home, name="home"),


    # all student list page /test/all/grid
    url(r'^all/grid/$', views.grid_view, name='all_students_grid'),

    url(r'^all/list/$', views.list_view, name='all_students_list'),

    # /test/2/delete
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='student-delete'),

    # /test/19
    url(r'^(?P<student_id>[0-9]+)/$', views.detail_view, name='details'),

    # /test/19
    url(r'^update/(?P<student_id>[0-9]+)/$', views.update, name='update'),

    url(r'^login/$', views.login, name='login'),

]

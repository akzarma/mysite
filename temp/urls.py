from django.conf.urls import url
from . import views

app_name = "home"

urlpatterns = [

    # url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.home, name="home"),
    #
    url(r'^action/$', views.action, name="action")
]

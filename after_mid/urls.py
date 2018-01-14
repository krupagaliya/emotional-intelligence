
from django.conf.urls import url
from django.contrib import admin
from Fi import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^sa2/',views.sao2,name="sao2"),
    url(r'^instant-result/',views.instantResult,name="instantResult"),
    url(r'^$', views.index, name="index"),
    url("", views.index, name="index"),




]

from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^products/$', views.machine_products),
    url(r'^sale/$', views.sale),
    url(r'^login/$', views.login),
    url(r'^signup/$', views.signup),
    ]
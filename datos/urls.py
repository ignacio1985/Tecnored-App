from django.conf.urls import url
from . import views

app_name = 'datos'

urlpatterns = [
    url(r'^$', views.lista_datos, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.detalle_datos, name="detail"),
]
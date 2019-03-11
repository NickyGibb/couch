from django.conf.urls import url
from dice import views


urlpatterns=[
     url(r'^$', views.home, name = 'home'),
]

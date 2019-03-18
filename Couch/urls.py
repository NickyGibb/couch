"""Couch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from dice import views
from django.conf.urls.static import static
from machina.app import board
from registration.backends.simple.views import RegistrationView


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^dice/about/$', views.about, name = 'about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
    url(r'^dice/', include('dice.urls')),
    url(r'^dice/user/$',views.user, name = 'user'),
    url(r'^dice/game/$', views.game, name = 'game'),
    url(r'^dice/forum/', include(board.urls)),
    url(r'^dice/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^dice/logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^dice/admin/', admin.site.urls),
    url(r'^dice/register/$', views.register, name='register'),
    url(r'^dice/password/$', views.change_password, name='change_password'),
    url(r'^dice/register_profile/$', views.register_profile, name='register_profile'),
    url(r'^dice/profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^dice/events/$', views.events, name='events'),
    url(r'^dice/createevent/$', views.create_event, name='create_event'),
    url(r'^accounts/', include('registration.backends.simple.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from dice import views
from django.conf.urls.static import static
from machina.app import board


urlpatterns=[
     url(r'^home', views.home, name = 'home'),
     url(r'^about', views.about, name = 'about'),
     url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name = 'show_category'),
     url(r'^user/$',views.user, name = 'user'),
     url(r'^game/$', views.game, name = 'game'),
     url(r'^forum/', include(board.urls)),
     url(r'^login/$', views.user_login, name='login'),
     url(r'^logout/$', views.user_logout, name='logout'),
     url(r'^admin/', admin.site.urls),
     url(r'^register/$', views.register, name='register'),
     url(r'^password/$', views.change_password, name='change_password'),
     url(r'^register_profile/$', views.register_profile, name='register_profile'),
     url(r'^profile/$', views.profile, name='profile'),
     url(r'^events/$', views.events, name='events'),
     url(r'^createevent/$', views.create_event, name='create_event'),
     url(r'^like/$', views.like_game, name='like_game'),
     url(r'^dislike/$', views.dislike_game, name='dislike_game'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

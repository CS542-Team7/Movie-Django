from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^movie_all/$', views.movie_all, name='movie_all'),
    url(r'^actor_all/$', views.actor_all, name='actor_all'),
    url(r'^movie_detail/', views.movie_detail, name='movie_detail'),
    url(r'^actor_detail/', views.actor_detail, name='actor_detail'),
    url(r'^movie_search', views.movie_search, name='movie_search'),
    url(r'^actor_search', views.actor_search, name='actor_search'),
    url(r'^favorite/', views.favorite, name='favorite'),
]

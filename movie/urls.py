from django.conf.urls import url
from . import views
from . import models

urlpatterns = [
    url(r'^movie_all/(?P<page>\d*)', views.whole_list, {'model': models.Movie}, name='whole_list'),
    url(r'^actor_all/(?P<page>\d*)', views.whole_list, {'model': models.Actor}, name='whole_list'),
    url(r'^movie_detail/(?P<id>.*)', views.detail, {'model': models.Movie}, name='movie_detail'),
    url(r'^actor_detail/(?P<id>.*)', views.detail, {'model': models.Actor}, name='actor_detail'),
    url(r'^search/(?P<pattern>.*)', views.search, name='search'),
    url(r'^favorite/(?P<movie_id>.*)', views.favorite, name='favorite'),
]


from django.urls import path
# from watchlist.views import

from . import views

urlpatterns = [
    path("list", views.movie_list, name='movie_list'),
    path("<int:index>", views.movie_detail, name='movie_detail')
]

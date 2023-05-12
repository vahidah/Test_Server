from django.urls import path
from watchlist.api.views import (WatchListAV, WatchDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewList,
                                 ReviewDetail, ReviewCreate, ReviewAllList)
from . import views

urlpatterns = [
    path("list", WatchListAV.as_view(), name='movie_list'),
    path("<int:index>", WatchDetailAV.as_view(), name='movie_detail'),
    path("stream/", StreamPlatformListAV.as_view(), name='stream'),
    path("stream/<int:index>", StreamPlatformDetailAV.as_view(), name='stream'),
    # path("review", ReviewList.as_view(), name='review-list'),
    path("stream/<int:pk>/review", ReviewList.as_view(), name='review-list'),
    path("stream/<int:pk>/review-create", ReviewCreate.as_view(), name='review-create'),
    path("review/<int:pk>", ReviewDetail.as_view(), name='review-detail'),
    path("review/list", ReviewAllList.as_view(), name='review-detail'),
]

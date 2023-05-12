from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins

from watchlist.models import WatchList, StreamPlatform, Review
from watchlist.api.serializer import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist.api.permissions import AdminOrReadOnly, ReviewOrReadOnly


# Create your views here.


class ReviewCreate(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)

        user = self.request.user
        review_query = Review.objects.filter(watch=movie, review_user=user)

        if review_query.exists():
            raise ValidationError("you have already reviewed this movie")

        movie.rating = (movie.rating * movie.number_rating + serializer.validated_data['rating']) / (movie.number_rating + 1)
        movie.number_rating = movie.number_rating + 1

        movie.save()

        serializer.save(watch=movie, review_user = user)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watch=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewOrReadOnly]




# class ReviewDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
#     def delet(self, request, *args, **kwargs):
#         return self.delet(request, *args, **kwargs)
#
#
class ReviewAllList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serialized = WatchListSerializer(movies, many=True)
        return Response(serialized.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request, index):
        try:
            movie = WatchList.objects.get(pk=index)
        except WatchList.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = WatchListSerializer(movie)
        return Response(serialized.data)

    def put(self, request, index):
        movie = WatchList.objects.get(pk=index)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, index):
        movie = WatchList.objects.get(pk=index)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformListAV(APIView):

    def get(self, request):
        streamPlatforms = StreamPlatform.objects.all()
        serialized = StreamPlatformSerializer(streamPlatforms, many=True)
        return Response(serialized.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):

    def get(self, request, index):
        try:
            steamPlatform = StreamPlatform.objects.get(pk=index)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serialized = StreamPlatformSerializer(steamPlatform)
        return Response(serialized.data)

    def put(self, request, index):
        steamPlatform = StreamPlatform.objects.get(pk=index)
        serializer = StreamPlatformSerializer(steamPlatform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, index):
        steamPlatform = StreamPlatform.objects.get(pk=index)
        steamPlatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serialized = MovieSerializer(movies, many=True)
#         return Response(serialized.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, index):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=index)
#         except Movie.DoesNotExist:
#             return Response ({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serialized = MovieSerializer(movie)
#         return Response(serialized.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=index)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=index)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

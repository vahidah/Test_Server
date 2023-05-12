from django.shortcuts import render
# from watchlist.models import Movie
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = list(movies.values())
#     response = {'movies': data}
#     return JsonResponse(response)
#
#
# def movie_detail(request, index):
#     movie = Movie.objects.get(pk=index)
#
#     response = {
#         'name' : movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#
#     return JsonResponse(response)

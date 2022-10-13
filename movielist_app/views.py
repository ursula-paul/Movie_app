# from urllib import response
# from django.shortcuts import render
# from movielist_app.models import Movie
# from django.http import JsonResponse



# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies':list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_details(request,pk):
#     movie = Movie.objects.get(pk=pk)
#     data ={
#         'movies':movie.name,
#         'Descripton':movie.description,
#         'Active':movie.active
        
#     }
#     return JsonResponse(data)
    
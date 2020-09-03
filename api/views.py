from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # allows us to create custom methods for GET/POST/etc. -The detail attribute allows us to decide if it's a specific model or a list (True = specifc, False = List)
    # Right now, we set the pk to None as default if it's not provided
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            response = {'message': 'it\'s working', 'data': request.data, 'movie_title': movie.title}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'you need to provide a number of stars', 'data': request.data}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

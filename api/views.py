from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all();
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication, )

    # @action(detail=True, methods=['POST'])
    # def register(self, request, pk=None):
    #     if 'username' in request.data:
    #         # user = 

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )

    # allows us to create custom methods for GET/POST/etc. -The detail attribute allows us to decide if it's a specific model or a list (True = specifc, False = List)
    # Right now, we set the pk to None as default if it's not provided
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            # Right now we are statically assigning user to id=1 or the first user
            # user = User.objects.get(id=1)
            user = request.user

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated' , 'data': request.data, 'result': serializer.data, 'username': user.username}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created' , 'data': request.data, 'result': serializer.data, 'username': user.username}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'you need to provide a number of stars', 'data': request.data}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication, )

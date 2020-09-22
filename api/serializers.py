from rest_framework import serializers
from .models import Movie, Rating

class MovieSerializer(serializers.ModelSerializer):
    # This meta class determines what will be in the serializer
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')

class RatingSerializer(serializers.ModelSerializer):
    # This meta class determines what will be in the serializer
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'movie')
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Rating

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name')
        # password = serializers.CharField(write_only=True)
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

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
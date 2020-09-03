from django.db import models
from django.contrib.auth.models import User
# You can use validators for determining range of values
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

class Rating(models.Model):
    # if movie is removed, then remove the rating (cascading)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # if we already have a rating for a movie for that user, it will reject the entry because of this meta class
    class Meta:
        unique_together = (('user', 'movie'))
        index_together = (('user', 'movie'))

from django.db import models
from django.contrib.auth.models import User

# eventually want all categories of sg, slope, rating, distance, etc etc
class GolfRound(models.Model):
    course = models.CharField(max_length=100)
    score = models.SmallIntegerField
    date_posted = models.DateField
    total_strokes_gained = models.FloatField
    golfer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.total_strokes_gained
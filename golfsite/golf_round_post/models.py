from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# eventually want all categories of sg, slope, rating, distance, etc etc
class GolfRound(models.Model):
    course = models.CharField(max_length=100, default='No Course Info')
    score = models.SmallIntegerField(default=100)
    date_posted = models.DateField(default=timezone.now)
    total_strokes_gained = models.FloatField(default=0.0)
    golfer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.total_strokes_gained)
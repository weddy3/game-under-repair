from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# TODO fill in all necessary params and double check logic

class GolfShot(models.Model):
    stroke_number = models.SmallIntegerField()
    lie = models.TextField()
    distance_remaining = models.SmallIntegerField()
    penalty = models.BooleanField()
    expected_strokes_to_hole_out = models.FloatField()


class GolfHole(models.Model):
    shot = models.ForeignKey(GolfShot, on_delete=models.CASCADE)
    score = models.SmallIntegerField()
    par = models.SmallIntegerField()
    distance = models.SmallIntegerField()
    total_strokes_gained = models.FloatField(default=0.0)
    ott_strokes_gained = models.FloatField(default=0.0)
    app_strokes_gained = models.FloatField(default=0.0)
    atg_strokes_gained = models.FloatField(default=0.0)
    put_strokes_gained = models.FloatField(default=0.0)
    hole_number_in_golfers_round = models.SmallIntegerField()


class GolfCourse(models.Model):
    name = models.TextField()
    distance = models.SmallIntegerField()
    tee = models.TextField()
    slope = models.SmallIntegerField()
    rating = models.FloatField()
    city = models.TextField()
    state = models.TextField()


class GolfRound(models.Model):
    course = models.OneToOneField(GolfCourse, on_delete=models.CASCADE, primary_key=True)
    score = models.SmallIntegerField(default=100)
    date_posted = models.DateField(default=timezone.now)
    total_strokes_gained = models.FloatField(default=0.0)
    ott_strokes_gained = models.FloatField(default=0.0)
    app_strokes_gained = models.FloatField(default=0.0)
    atg_strokes_gained = models.FloatField(default=0.0)
    put_strokes_gained = models.FloatField(default=0.0)
    golfer = models.ForeignKey(User, on_delete=models.CASCADE)
    hole = models.ForeignKey(GolfHole, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.total_strokes_gained)
    

    def get_absolute_url(self):
        # Redirects to detail view following creation of a golf round in the UI
        return reverse('golf-round-detail', kwargs={'pk': self.pk})
    
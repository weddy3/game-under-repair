from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class GolfShot(models.Model):
    stroke_number = models.SmallIntegerField(null=True)
    lie = models.CharField(max_length=10)
    distance_remaining = models.SmallIntegerField(null=True)
    penalty = models.BooleanField(null=True)
    expected_strokes_to_hole_out = models.FloatField(null=True)


class GolfHole(models.Model):
    score = models.SmallIntegerField(null=True)
    par = models.SmallIntegerField(null=True)
    distance = models.SmallIntegerField(null=True)
    total_strokes_gained = models.FloatField(null=True)
    ott_strokes_gained = models.FloatField(null=True)
    app_strokes_gained = models.FloatField(null=True)
    atg_strokes_gained = models.FloatField(null=True)
    put_strokes_gained = models.FloatField(null=True)
    hole_number_in_golfers_round = models.SmallIntegerField(null=True)
    shot = models.ForeignKey(GolfShot, on_delete=models.CASCADE)


class GolfTees(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    distance = models.SmallIntegerField(null=True)
    slope = models.SmallIntegerField(null=True)
    rating = models.FloatField(null=True)


class GolfCourse(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    tees = models.ForeignKey(GolfTees, on_delete=models.CASCADE)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=2)


class GolfRound(models.Model):
    course = models.OneToOneField(GolfCourse, on_delete=models.CASCADE)
    score = models.SmallIntegerField(null=True)
    date_posted = models.DateField(default=timezone.now)
    total_strokes_gained = models.FloatField(null=True)
    ott_strokes_gained = models.FloatField(null=True)
    app_strokes_gained = models.FloatField(null=True)
    atg_strokes_gained = models.FloatField(null=True)
    put_strokes_gained = models.FloatField(null=True)
    golfer = models.ForeignKey(User, on_delete=models.CASCADE)
    hole = models.ForeignKey(GolfHole, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.total_strokes_gained)
    

    def get_absolute_url(self):
        # Redirects to detail view following creation of a golf round in the UI
        return reverse('golf-round-detail', kwargs={'pk': self.pk})
    
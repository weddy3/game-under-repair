from django.db import models

class courseName(models.Model):
    course_id = models.IntegerField(primary_key=True, max_length=5)
    course_name = models.TextField(max_lenth=25)
    city = models.TextField(max_length=15)
    state = models.TextField(max_length=2)
    postcode = models.TextField(max_length=5)
    address = models.TextField(max_length=30)


class CourseInfo(models.Model):
    coure_info_id = models.IntegerField(primary_key=True, max_length=5)
    course_id = models.ForeignKey(to=courseName, on_delete=models.CASCADE)
    par = models.IntegerField(max_length=2)
    tee = models.TextField(max_length=7)
    total_distance = models.IntegerField(max_length=4)
    rating = models.FloatField(max_length=3)
    slope = models.IntegerField(max_length=3)


class HoleInfo(models.Model):
    hole_info_id = models.IntegerField(primary_key=True, max_length=7)
    course_id = models.ForeignKey(to=courseName, on_delete=models.CASCADE)
    tee = models.TextField(max_length=7)
    hole = models.IntegerField(max_length=2)
    par = models.IntegerField(max_length=1)
    distance = models.IntegerField(max_length=3)
    handicap = models.IntegerField(max_length=2)


class RoundInfo(models.Model):
    round_id = models.IntegerField(primary_key=True, max_length=5)
    course_id = models.ForeignKey(to=courseName, on_delete=models.CASCADE)
    tee_played = models.TextField(max_length=7)
    score = models.IntegerField(max_length=3)
    date_played = models.DateField()


class HoleEntry(models.Model):
    hole_entry_id = models.IntegerField(primary_key=True, max_length=10)
    hole_info_id = models.ForeignKey(to=HoleInfo, on_delete=models.CASCADE)
    round_id = models.ForeignKey(to=RoundInfo, on_delete=models.CASCADE)
    hole_number = models.IntegerField(max_length=2)
    score = models.IntegerField(max_length=2)
    score_to_par = 
    # need to figure out how to best input variable amount of shots and related info (par 3,4,5 models for entry?)
    fairway_in_regulation = 
    fairway_miss = 
    green_in_regulation =
    green_miss = 
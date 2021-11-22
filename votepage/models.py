from django.db import models


class voteoption(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)
    reg_no = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    year_of_study = models.PositiveIntegerField()
    course_and_dept = models.CharField(max_length=100)

class receive(models.Model):
    reg_no = models.CharField(max_length=100)
    selection = models.CharField(max_length=100)
    mail = models.EmailField(max_length=254)

class received_feedback(models.Model):
    response = models.TextField()

class updates(models.Model):
    news_update = models.TextField()
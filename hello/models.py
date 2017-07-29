from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Keywords(models.Model):
    email = models.EmailField()
    keywords = models.CharField(max_length=100)

class AppNums(models.Model):
    email = models.EmailField()
    appnums = models.CharField(max_length=100)

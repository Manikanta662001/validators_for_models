from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def check_for_a(value):
    if value[0].lower()=='a':
        raise ValidationError('started with a')















class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[check_for_a])

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    email=models.EmailField(default='cricket@gmail.com')
    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.author
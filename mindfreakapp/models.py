from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):

    user = models.ForeignKey(User,  on_delete = models.CASCADE,default='')
    questiontitle = models.CharField(max_length=1000)
    subject = models.CharField(max_length=500)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    correctans = models.CharField(max_length=500)
    level = models.CharField(max_length=500)
    description = models.CharField(max_length=1500)


    def __str__(self):
        return self.questiontitle

class Content(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    subject = models.CharField(max_length=500)
    topicname = models.CharField(max_length=1000)
    description = models.CharField(max_length=1500)
    level = models.CharField(max_length=500)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.topicname

from django.db import models


def teacher_models(models.Model):

    Teacher = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)

def student_models(models.Model):

    Student = models.CharField(max_length=100)
    Class =  models.CharField(max_length=100)

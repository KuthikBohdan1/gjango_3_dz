from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    description = models.CharField(max_length=100, verbose_name="опис")

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Class (models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=1)

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_class = models.CharField(Class , on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name



class Schedule(models.Model):
    clas = models.FreignKey(Subject, on_delete=models.CASCADE)
from django.db import models

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100, verbose_name="Ім'я вчителя")
    subject = models.CharField(max_length=100, verbose_name="Предмет")

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=100, verbose_name="Ім'я студента")
    student_class = models.CharField(max_length=100, verbose_name="Клас")

    def __str__(self):
        return self.student_name

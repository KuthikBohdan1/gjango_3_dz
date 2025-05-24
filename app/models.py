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
        return self.student



class Schedule(models.Model):
    DAYS = (
        ('Monday', 'Понеділок'),
        ('Tuesday', 'Вівторок' ),
        ('Wednesday', 'Середа'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятния'),
        ('Saturday', 'Субота'),
        ('Sunday', 'Неділя')
        )

    week_day = models.CharField(max_length=15, choices=DAYS)
    start_time = models.CharField(max_length=20)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

##

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)





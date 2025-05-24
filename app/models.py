from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

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
        return f'день {self.date}, {self.start_time} ,придмет {self.subject}'
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)




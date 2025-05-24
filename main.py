import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()
from app.models import Class, Subject, Teacher, Student, Schedule, Grade    

work = True
while work == True:
    print("""
        1. додати придмет
        2. додати вчителя
        3. додати клас
        4. додати учня
        0. вийти


""")
    
    chois = int(input("Введіть номер дії: "))
    if chois == 0:
        work = False

    if chois == 1:
        name = input("назва придмету: ")
        description = input("опис: ")
        check = Subject.objects.filter(name = name).first()
        if check:
            print("вже існує")

        else:
            Subject.objects.create(name=name, description=description)


    if chois == 2:
        name = input("імя: ")   
        last_name = input("призвище: ")
        subject = input("предмет: ")
        check = subject.objects.filter(name = subject).first()
        if check:
            Teacher.objects.cereate(name = name, last_name = last_name, subject = check)

        else:
            print("такого придмету немає")


        
    if chois == 3:  
        name = input("назва придмету: ")
        year = int(input("опис: "))
        check = Class.objects.filter(name = name).first()
        if check:
            print("вже існує")

        else:
            Class.objects.create(name=name, year= year)
            print("клас додано")


    if chois == 4:

        pass
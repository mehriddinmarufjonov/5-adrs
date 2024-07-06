from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    parents_phone_number = models.CharField(max_length=13)
    telegram_link = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
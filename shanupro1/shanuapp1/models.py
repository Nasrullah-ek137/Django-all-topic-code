from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)

    '''def __str__(self):
        return self.stuname'''
    
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)


class Student1(models.Model):
    name=models.CharField(max_length=70)
    roll=models.IntegerField(unique=True,null=False)
    city=models.CharField(max_length=70)
    marks=models.IntegerField()
    pass_date=models.DateField()

class CommonInfo(models.Model):
    name=models.CharField(max_length=70)
    age=models.IntegerField()
    date=models.DateField()
    class Meta:
        abstract=True

class Student2(CommonInfo):
    fees=models.IntegerField()
    date=None

class Teacher(CommonInfo):
    salary=models.IntegerField()

class Contractor(CommonInfo):
    date=models.DateTimeField()
    payment=models.IntegerField()
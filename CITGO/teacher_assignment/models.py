from django.db import models


# Create your models here.
class Teacher(models.Model):
    teacherID = models.IntegerField(null = False, primary_key = True)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Event(models.Model):
    eventID= models.IntegerField(null=False, primary_key = True)
    status= models.BooleanField(null = True)
    eventName = models.CharField(max_length=200)
    eventDate= models.DateField(null=False)
    registrationDate = models.DateField(null = False)
    slots= models.IntegerField(null= False)

    def __str__(self):
        return self.title

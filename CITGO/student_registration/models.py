from django.db import models

# Create your models here.


class Student(models.Model):
    StudentID = models.IntegerField(max_length=15, null=False, primary_key=True)
    StudentName = models.CharField(max_length=255, null=False)
    Year = models.IntegerField(max_length=10, null=False)
    Course = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.StudentName







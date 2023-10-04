from django.db import models


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects_taught = models.ManyToManyField('Event', related_name='teachers_assigned', blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

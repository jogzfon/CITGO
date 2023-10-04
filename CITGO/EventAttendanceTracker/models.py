from django.db import models

# Create your models here.

class AttendanceTracker(models.Model):
    trackingId = models.IntegerField(max_length=15, null=False,primary_key = True)
    students_attending = models.CharField(max_length = 256)
   # studentID = models.ForeignKey()
   # ticketID = models.ForeignKey()
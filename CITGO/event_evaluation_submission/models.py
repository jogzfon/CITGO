from django.db import models
from CITGO.teacher_assignment.models import Teacher, Event

# Create your models here.
class FeedBack(models.Model):
    feedbackID = models.IntegerField(null=False, primary_key=True)
    feedback = models.CharField(max_length=500, null=False)
    studentID = models.ManyToManyRel()
    teacherID = models.ManyToManyRel(Teacher)
    eventID = models.ForeignKey(Event)

from django.db import models

# Create your models here.


class Ticket(models.Model):
    ticketID = models.IntegerField(null=False, primary_key=True)
    price = models.IntegerField(null=False)
    status = models.BooleanField(null=False)
    # eventID = models.ForeignKey


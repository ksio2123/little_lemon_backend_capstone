from django.db import models
# from django.db.models import Model, CharField, DecimalField, PositiveSmallIntegerField

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    inventory = models.PositiveSmallIntegerField(db_index=True)

class BookingItem(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    no_of_guests = models.PositiveSmallIntegerField(db_index=True)
    booking_date = models.DateTimeField(db_index=True)
from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.


class input(models.Model):
    name = CharField(max_length=50)
    age = IntegerField()
    city = CharField(max_length=50)
    state = CharField(max_length=50)
    check = IntegerField(null=True)

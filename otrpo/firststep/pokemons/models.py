from django.db import models

# Create your models here.


class fightRezult(models.Model):
    rezult = models.TextField()

class pokemonfeedback(models.Model):
    FIO = models.TextField(max_length=50)
    comment = models.TextField(max_length=200)
    pokemon_name = models.TextField()
    start = models.IntegerField()


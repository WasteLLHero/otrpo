from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class fightRezult(models.Model):
    rezult = models.TextField()
    time = models.DateField()
    round_count = models.IntegerField()
    first_pokemon = models.TextField()
    second_pokemon = models.TextField()
    user_id = models.ManyToManyField(User, null=True)
    winner = models.TextField()

class pokemonfeedback(models.Model):
    email = models.TextField(max_length=50)
    comment = models.TextField(max_length=200)
    pokemon_name = models.TextField()
    star = models.IntegerField()


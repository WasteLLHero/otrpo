# Generated by Django 4.0 on 2023-10-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0004_pokemonfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonfeedback',
            name='start',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]

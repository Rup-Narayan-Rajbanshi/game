# Generated by Django 3.2.6 on 2021-09-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_game', '0009_score_is_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_housefull',
            field=models.BooleanField(default=False),
        ),
    ]

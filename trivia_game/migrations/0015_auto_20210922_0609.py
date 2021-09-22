# Generated by Django 3.2.6 on 2021-09-22 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_game', '0014_alter_game_no_of_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='trivia_game.question'),
        ),
        migrations.AlterField(
            model_name='score',
            name='user_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score', to='trivia_game.usergame'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='useranswer', to='trivia_game.answer'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useranswer', to='trivia_game.question'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='user_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useranswer', to='trivia_game.usergame'),
        ),
    ]
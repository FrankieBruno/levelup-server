# Generated by Django 4.2.1 on 2023-05-08 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('maker', models.CharField(max_length=55)),
                ('number_of_players', models.IntegerField()),
                ('skill_level', models.IntegerField()),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gametype')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=55)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField()),
                ('attendees', models.ManyToManyField(related_name='gamer_events_attending', to='levelupapi.gamer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
    ]

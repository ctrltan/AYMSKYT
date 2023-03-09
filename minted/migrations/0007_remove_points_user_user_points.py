# Generated by Django 4.1.5 on 2023-03-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minted', '0006_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='points',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minted.points'),
        ),
    ]

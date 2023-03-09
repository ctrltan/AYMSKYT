# Generated by Django 4.1.5 on 2023-03-08 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minted', '0008_alter_user_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='points',
        ),
        migrations.AddField(
            model_name='points',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='points', to=settings.AUTH_USER_MODEL),
        ),
    ]

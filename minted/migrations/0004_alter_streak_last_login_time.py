# Generated by Django 4.1.5 on 2023-02-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minted', '0003_alter_user_streak_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='last_login_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
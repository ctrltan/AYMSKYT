# Generated by Django 4.1.5 on 2023-02-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minted', '0009_alter_user_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='minted.spendinglimit'),
        ),
    ]

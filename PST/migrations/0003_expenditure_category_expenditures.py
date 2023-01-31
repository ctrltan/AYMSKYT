# Generated by Django 4.1.5 on 2023-01-29 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PST', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=200)),
                ('receipt_image', models.FileField(blank=True, upload_to='uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='expenditures',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PST.expenditure'),
        ),
    ]
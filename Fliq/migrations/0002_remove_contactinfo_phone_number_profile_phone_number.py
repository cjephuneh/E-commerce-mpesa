# Generated by Django 4.1.7 on 2023-03-27 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fliq', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(default=1),
        ),
    ]

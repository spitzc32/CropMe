# Generated by Django 3.1.5 on 2021-04-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='ave_temperature',
            field=models.FloatField(default=0),
        ),
    ]
# Generated by Django 3.1.5 on 2021-04-10 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210411_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]

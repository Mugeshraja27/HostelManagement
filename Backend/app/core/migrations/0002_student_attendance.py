# Generated by Django 3.2.4 on 2022-01-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='attendance',
            field=models.CharField(default='000.000', max_length=5),
        ),
    ]

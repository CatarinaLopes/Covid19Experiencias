# Generated by Django 3.0.5 on 2020-04-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='user_name',
            field=models.CharField(default='', max_length=25),
        ),
    ]

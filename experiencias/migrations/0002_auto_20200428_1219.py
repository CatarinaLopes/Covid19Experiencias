# Generated by Django 3.0.5 on 2020-04-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]
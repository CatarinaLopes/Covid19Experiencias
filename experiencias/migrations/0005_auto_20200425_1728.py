# Generated by Django 3.0.5 on 2020-04-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0004_auto_20200425_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]

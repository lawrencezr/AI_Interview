# Generated by Django 2.1.7 on 2019-05-30 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190530_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='user_name',
        ),
    ]

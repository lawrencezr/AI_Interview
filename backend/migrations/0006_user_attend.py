# Generated by Django 2.1.7 on 2019-05-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20190521_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attend',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 2.1.7 on 2019-05-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190518_1634'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test_Video',
            new_name='Train_Video',
        ),
        migrations.AddField(
            model_name='admin',
            name='actual_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='admit',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='performance',
            name='url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='actual_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

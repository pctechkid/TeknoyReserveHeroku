# Generated by Django 4.0.2 on 2022-03-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_meetingrooms_isavailable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingrooms',
            name='meeting_room',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]

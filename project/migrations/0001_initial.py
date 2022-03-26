# Generated by Django 4.0.2 on 2022-03-21 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('aid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRooms',
            fields=[
                ('room_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('meeting_room', models.CharField(max_length=100, unique=True)),
                ('isAvailable', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('timein', models.TimeField()),
                ('timeout', models.TimeField()),
                ('numpersons', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.meetingrooms')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.users', to_field='username')),
            ],
        ),
    ]
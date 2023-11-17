# Generated by Django 4.2.5 on 2023-09-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('gender', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=100)),
                ('uname', models.CharField(max_length=50)),
                ('passw', models.CharField(max_length=30)),
                ('cu_num', models.IntegerField()),
            ],
        ),
    ]

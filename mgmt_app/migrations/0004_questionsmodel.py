# Generated by Django 4.2.5 on 2023-09-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt_app', '0003_newdiseasesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='questionsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=50)),
                ('quest', models.CharField(max_length=500)),
            ],
        ),
    ]
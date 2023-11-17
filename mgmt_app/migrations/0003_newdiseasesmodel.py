# Generated by Django 4.2.5 on 2023-09-12 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt_app', '0002_customerregmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='newdiseasesmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='mgmt_app/static')),
                ('symtom', models.CharField(max_length=500)),
                ('remedy', models.CharField(max_length=600)),
            ],
        ),
    ]

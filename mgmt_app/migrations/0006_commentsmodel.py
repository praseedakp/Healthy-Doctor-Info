# Generated by Django 4.2.5 on 2023-09-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt_app', '0005_answermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
    ]

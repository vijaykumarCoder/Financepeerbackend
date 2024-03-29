# Generated by Django 3.2.5 on 2022-04-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('upload', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TestMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=2000, null=True)),
                ('body', models.TextField(max_length=2000, null=True)),
                ('jsondata', models.JSONField(null=True)),
            ],
        ),
    ]

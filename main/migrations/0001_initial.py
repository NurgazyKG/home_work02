# Generated by Django 4.1 on 2022-08-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('Speed', models.IntegerField()),
                ('Year', models.DateField()),
            ],
        ),
    ]

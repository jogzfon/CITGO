# Generated by Django 4.2.5 on 2023-10-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentID', models.IntegerField(max_length=15, primary_key=True, serialize=False)),
                ('StudentName', models.CharField(max_length=255)),
                ('Year', models.IntegerField(max_length=10)),
                ('Course', models.CharField(max_length=255)),
            ],
        ),
    ]

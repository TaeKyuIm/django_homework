# Generated by Django 4.0.4 on 2022-05-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('student_id', models.IntegerField()),
                ('answer1', models.TextField()),
                ('answer2', models.TextField()),
                ('answer3', models.TextField()),
                ('answer4', models.TextField()),
                ('answer5', models.TextField()),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-16 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_course_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

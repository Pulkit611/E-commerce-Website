# Generated by Django 3.2.4 on 2021-06-20 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='dec',
            new_name='desc',
        ),
    ]

# Generated by Django 3.2.17 on 2023-02-03 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_rename_person_persons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persons',
            new_name='Person',
        ),
    ]

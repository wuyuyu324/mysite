# Generated by Django 2.0 on 2020-10-14 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='nickename',
            new_name='nickname',
        ),
    ]

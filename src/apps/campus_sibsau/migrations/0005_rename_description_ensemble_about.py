# Generated by Django 3.2.1 on 2021-08-08 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus_sibsau', '0004_alter_joiningensemble_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ensemble',
            old_name='description',
            new_name='about',
        ),
    ]

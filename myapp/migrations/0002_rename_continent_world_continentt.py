# Generated by Django 5.0.6 on 2024-06-17 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='world',
            old_name='continent',
            new_name='continentt',
        ),
    ]
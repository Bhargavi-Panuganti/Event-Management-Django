# Generated by Django 5.0.6 on 2024-06-21 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_myuser_venue_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
    ]
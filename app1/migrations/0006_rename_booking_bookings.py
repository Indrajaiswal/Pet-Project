# Generated by Django 4.0.3 on 2023-10-03 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_appointement_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Bookings',
        ),
    ]
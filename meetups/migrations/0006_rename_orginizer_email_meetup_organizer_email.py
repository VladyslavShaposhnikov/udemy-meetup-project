# Generated by Django 4.2 on 2023-05-02 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_meetup_date_meetup_orginizer_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='orginizer_email',
            new_name='organizer_email',
        ),
    ]

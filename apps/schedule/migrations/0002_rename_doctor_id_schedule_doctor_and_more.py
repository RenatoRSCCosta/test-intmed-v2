# Generated by Django 4.1 on 2022-08-23 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='doctor_id',
            new_name='doctor',
        ),
        migrations.RenameField(
            model_name='schedules',
            old_name='available',
            new_name='availabe',
        ),
        migrations.RenameField(
            model_name='schedules',
            old_name='schedule_id',
            new_name='schedule',
        ),
    ]
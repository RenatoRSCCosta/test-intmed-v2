# Generated by Django 4.1 on 2022-09-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_alter_schedule_doctor_alter_schedules_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='schedule.schedule'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-19 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_alter_schedules_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules_schedule', to='schedule.schedule'),
        ),
    ]

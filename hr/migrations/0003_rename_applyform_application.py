# Generated by Django 5.1.2 on 2025-04-22 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_job_alter_applyform_additional_info_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplyForm',
            new_name='Application',
        ),
    ]

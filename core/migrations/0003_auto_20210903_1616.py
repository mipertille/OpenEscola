# Generated by Django 3.2.5 on 2021-09-03 16:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_alter_subject_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='update_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]

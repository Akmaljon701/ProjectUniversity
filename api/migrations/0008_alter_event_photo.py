# Generated by Django 5.1 on 2024-08-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_event_alter_employee_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(upload_to='events/', verbose_name='Rasm'),
        ),
    ]

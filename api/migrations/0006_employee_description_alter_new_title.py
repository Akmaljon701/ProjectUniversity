# Generated by Django 5.1 on 2024-08-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_employee_status_alter_message_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Sarlavha'),
        ),
    ]

# Generated by Django 5.1 on 2024-08-09 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=50, verbose_name='F.I.O')),
                ('phone', models.CharField(max_length=13, verbose_name='Telefon raqam')),
                ('message', models.TextField(verbose_name='Xabar')),
                ('status', models.CharField(choices=[('YANGI', 'Yangi'), ('ESKI', 'Eski')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('XODIM', 'Xodim'), ('TALABA', 'Talaba'), ('PROFESSOR', 'Professor')], max_length=100, verbose_name='Turi'),
        ),
    ]

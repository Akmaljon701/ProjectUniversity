# Generated by Django 5.1 on 2024-08-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_event_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Sarlavha')),
                ('description', models.TextField(default='', verbose_name="Ma'lumot")),
                ('photo', models.ImageField(upload_to='events/', verbose_name='Rasm')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Vaqt')),
            ],
            options={
                'verbose_name_plural': "5.Mehmon ma'ruzalari",
            },
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendaruser',
            name='gender',
            field=models.CharField(blank=True, choices=[('-', '---'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
    ]

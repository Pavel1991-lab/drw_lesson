# Generated by Django 4.2.8 on 2023-12-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modified_at',
            field=models.TimeField(auto_now=True, verbose_name='время последнего обновления'),
        ),
    ]

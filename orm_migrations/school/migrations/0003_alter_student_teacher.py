# Generated by Django 4.0.2 on 2022-03-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20220319_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='student', to='school.Teacher'),
        ),
    ]
# Generated by Django 5.1 on 2024-08-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cego47700', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localarmazenamento',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='materialcampanha',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 5.0 on 2024-08-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cego47700', '0008_alter_municipio_area_km2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='area_km2',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]

# Generated by Django 3.2.10 on 2021-12-27 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localities_osm', '0004_auto_20190624_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localityosmnode',
            options={'managed': True, 'verbose_name': 'OSM Node', 'verbose_name_plural': 'OSM Node'},
        ),
        migrations.AlterModelOptions(
            name='localityosmway',
            options={'managed': True, 'verbose_name': 'OSM Way', 'verbose_name_plural': 'OSM Way'},
        ),
    ]

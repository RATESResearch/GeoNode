# Generated by Django 2.2.16 on 2021-05-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvesting', '0011_harvester_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvestableresource',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='harvestableresource',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

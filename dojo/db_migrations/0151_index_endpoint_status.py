# Generated by Django 3.2.12 on 2022-02-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0150_dedupe_endpoint_status'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='endpoint_status',
            constraint=models.UniqueConstraint(fields=('finding', 'endpoint'), name='endpoint-finding relation'),
        ),
    ]
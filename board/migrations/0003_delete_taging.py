# Generated by Django 3.2.22 on 2023-11-28 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_tag_taging'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Taging',
        ),
    ]
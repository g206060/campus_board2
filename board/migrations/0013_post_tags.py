# Generated by Django 3.2.22 on 2023-11-30 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_delete_taging'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='board.Tag', verbose_name='タグ'),
        ),
    ]

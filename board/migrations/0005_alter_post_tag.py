# Generated by Django 3.2.22 on 2023-11-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='board.Tag', verbose_name='タグ'),
        ),
    ]

# Generated by Django 3.2.22 on 2023-12-03 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_alter_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='学科')),
            ],
        ),
        migrations.CreateModel(
            name='GradeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='学年')),
            ],
        ),
        migrations.CreateModel(
            name='TypeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='種別')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='post',
            name='departmenttags',
            field=models.ManyToManyField(to='board.DepartmentTag', verbose_name='学科'),
        ),
        migrations.AddField(
            model_name='post',
            name='gradetags',
            field=models.ManyToManyField(to='board.GradeTag', verbose_name='学年'),
        ),
        migrations.AddField(
            model_name='post',
            name='typetags',
            field=models.ManyToManyField(to='board.TypeTag', verbose_name='種別'),
        ),
    ]

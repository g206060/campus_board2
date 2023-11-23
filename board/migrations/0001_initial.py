# Generated by Django 3.2.22 on 2023-11-17 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=256, verbose_name='掲示板名')),
                ('board_img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='デフォルト画像')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=256, verbose_name='タイトル')),
                ('post_overview', models.TextField(null=True, verbose_name='概要')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='掲載開始')),
                ('ended_at', models.DateTimeField(verbose_name='掲載終了')),
                ('post_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('post_upload', models.FileField(blank=True, null=True, upload_to='file/%y/%m/%d', verbose_name='ファイル')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='board.board', verbose_name='掲示板名')),
            ],
        ),
    ]

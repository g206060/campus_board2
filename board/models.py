from django.db import models
from accounts.models import CustomUser

import os

class Board(models.Model):
	"""掲示板モデル"""
	board_name = models.CharField(verbose_name='掲示板名', max_length=256)
	board_img = models.ImageField(verbose_name='デフォルト画像', null=True, blank=True)
	def __str__(self):
		return self.board_name
		
class GradeTag(models.Model):
	"""学年タグモデル"""
	name = models.CharField(verbose_name='学年', max_length=256)
	def __str__(self):
		return self.name
		
class DepartmentTag(models.Model):
	"""学科タグモデル"""
	name = models.CharField(verbose_name='学科', max_length=256)
	def __str__(self):
		return self.name
		
class TypeTag(models.Model):
	"""種別タグモデル"""
	name = models.CharField(verbose_name='種別', max_length=256)
	def __str__(self):
		return self.name

class Post(models.Model):
	"""掲示物モデル"""
	board = models.ForeignKey(Board, verbose_name='掲示板名', on_delete=models.PROTECT)
	post_title = models.CharField(verbose_name='タイトル', max_length=256)
	post_overview = models.TextField(verbose_name='概要', null=True)
	started_at = models.DateTimeField(verbose_name='掲載開始', auto_now_add=True)
	ended_at = models.DateTimeField(verbose_name='掲載終了')
	post_photo = models.ImageField(verbose_name='写真', null=True, blank=True)
	post_upload = models.FileField(verbose_name='ファイル', upload_to='file/%y/%m/%d', null=True, blank=True)
	gradetags = models.ManyToManyField(GradeTag, verbose_name='学年')
	departmenttags = models.ManyToManyField(DepartmentTag, verbose_name='学科')
	typetags = models.ManyToManyField(TypeTag, verbose_name='種別')
	user_name = models.ForeignKey(CustomUser, verbose_name='投稿者', on_delete=models.CASCADE)
	def __str__(self):
		return self.post_title
		
	def file_name(self):
		return os.path.basename(self.post_upload.name)

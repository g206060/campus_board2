from django import forms
from django.utils import timezone

from .models import Post, GradeTag, DepartmentTag, TypeTag

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('board', 'post_title', 'post_overview', 'ended_at', 'post_photo', 'post_upload', 'gradetags', 'departmenttags', 'typetags', 'user_name')


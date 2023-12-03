from django.contrib import admin

from .models import Board, Post, GradeTag, DepartmentTag, TypeTag

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(GradeTag)
admin.site.register(DepartmentTag)
admin.site.register(TypeTag)

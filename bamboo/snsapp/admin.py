from django.contrib import admin
from .models import Post, Comment, FreePost, FreeComment

# 관리자 페이지에서 보기 위해서 등록해줘야함
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)
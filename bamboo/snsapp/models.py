from django.db import models

# 게시글 모델 만들기
class Post(models.Model):
    # 제목, 작성자, 날짜, 링크 누를경우 내용 보일예정
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
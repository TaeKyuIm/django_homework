from django.db import models
from django.contrib.auth.models import User

# 게시글 모델 만들기
class Post(models.Model):
    # 제목, 작성자, 날짜, 링크 누를경우 내용 보일예정
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 객체 추가시 그 당시의 시간을 데이터에 넣어줄 수 있음
    
    def __str__(self):
        return self.title
    
class Comment(models.Model): # ORM
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE) # 어느 게시글에 있는 댓글인지 중요하므로 models.ForeignKey를 이용하여 연결
    
    def __str__(self):
        return self.comment
    
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE) # 어느 게시글에 있는 댓글인지 중요하므로 models.ForeignKey를 이용하여 연결
    
    def __str__(self):
        return self.comment
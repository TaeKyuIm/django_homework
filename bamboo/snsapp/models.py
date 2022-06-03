from django.db import models

# 게시글 모델 만들기
class Post(models.Model):
    # 제목, 작성자, 날짜, 링크 누를경우 내용 보일예정
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 자동으로 객체 추가시 그 당시의 시간을 데이터에 넣어줄 수 있음
    
    def __str__(self):
        return self.title
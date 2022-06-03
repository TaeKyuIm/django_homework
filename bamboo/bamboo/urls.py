from django.contrib import admin
from django.urls import path
from snsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'), # detail/1 이런식으로 구현 할거임. 그때 id를 post_id라는 인자로 넘겨줄거임
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment')
]

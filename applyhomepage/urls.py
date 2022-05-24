from django.contrib import admin
from django.urls import path
from appliance import views

urlpatterns=[
	path('admin/', admin.site.urls),
	path('', views.home, name="home"),
	path('apply/', views.apply, name="apply"),
	path('create/', views.create, name="create"),
]
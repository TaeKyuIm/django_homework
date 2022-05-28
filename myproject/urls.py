from django.contrib import admin
from django.urls import path,include
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.home,name="home"), 
    path('accounts/', include('accounts.urls')),
]

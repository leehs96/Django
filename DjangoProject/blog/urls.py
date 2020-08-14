from django.urls import path
from django.contrib import admin
import blog.views

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('',blog.views.home,name="home"),
    path('<int:post_id>/', blog.views.detail, name = "detail"),
    path('new/', blog.views.new, name = "new"),
    path('create/', blog.views.create,name='create'),
]

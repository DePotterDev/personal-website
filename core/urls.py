from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [ 
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<language>', views.blog_language, name='language'),
    path('blog/post/<slug>', views.blog_post, name='posts'),
]
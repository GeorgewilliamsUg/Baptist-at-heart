from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('contact/', views.contact, name='contact'),
      path('category/<str:category_name>/', views.category, name='category'),
      path('single_post/<int:post_id>/', views.single_post, name='single_post'),
      path('about-the-book/', views.about_the_book, name='about-the-book'),
      path('articles/', views.articles, name='articles'),
              
]
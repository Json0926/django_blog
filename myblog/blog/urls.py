from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:article_id>/', views.article_page, name='article_page'),
    path('edit/<int:article_id>/', views.edit_page, name='edit_page'),
    path('edit/action', views.edit_page, name='edit_action'),
]
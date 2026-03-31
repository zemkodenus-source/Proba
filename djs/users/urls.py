from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.users_hub , name='users_hub'),
    path('users_register', views.users_register, name='users_registers'),
    path('add_comment' , views.add_comment , name = 'add_comment') ,
    path('<int:pk>' , views.commentDetailView.as_view() ,name ='comment-view') ,
    path('<int:pk>/update', views.commentUpdateView.as_view(), name='comment-update'),
    path('<int:pk>/delete', views.commentDeleteView.as_view(), name='comment-delete'),
    path('users_list', views.users_list, name='users_list'),
]
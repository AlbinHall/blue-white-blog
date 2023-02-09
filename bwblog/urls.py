from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('discussions/', views.discussion_list, name='discussion_list'),
    path('discussions/create/', views.discussion_create, name='discussion_create'),
    path('discussions/<int:pk>/', views.discussion_detail, name='discussion_detail'),
    path('discussion/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('discussions/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('discussion/<int:pk>/remove/', views.delete_discussion, name='delete_discussion'),
    path('discussions/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('discussions/<int:pk>/dislike/', views.toggle_dislike, name='toggle_dislike'),
    path('send_email/', views.send_email, name='send_email'),
    path('delete_comment/<int:pk>/<slug:slug>/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('edit_comment/<int:pk>/<slug:slug>/', views.UpdateCommentView.as_view(), name='edit_comment'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
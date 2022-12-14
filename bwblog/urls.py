from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('send_email/', views.send_email, name='send_email'),
    path('delete_comment/<int:pk>/<slug:slug>/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('edit_comment/<int:pk>/<slug:slug>/', views.UpdateCommentView.as_view(), name='edit_comment'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
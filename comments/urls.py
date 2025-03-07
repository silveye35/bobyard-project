from django.urls import path
from .views import CommentListCreateView, CommentRetrieveUpdateDeleteView

urlpatterns = [
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment-detail'),
]

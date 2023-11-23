from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('kyoumu/', views.KyoumuView.as_view(), name="board_kyoumu"),
    path('arubaito/', views.ArubaitoView.as_view(), name="board_arubaito"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post-create/', views.PostCreateView.as_view(), name="post_create"),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
]
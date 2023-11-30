from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('kyoumu/', views.KyoumuView.as_view(), name="board_kyoumu"),
    path('gakusei/', views.GakuseiView.as_view(), name="board_gakusei"),
    path('shien/', views.ShienView.as_view(), name="board_shien"),
    path('arubaito/', views.ArubaitoView.as_view(), name="board_arubaito"),
    path('gakuyu/', views.GakuyuView.as_view(), name="board_gakuyu"),
    path('job/', views.JobView.as_view(), name="board_job"),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post-create/', views.PostCreateView.as_view(), name="post_create"),
    path('post-update/<int:pk>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post-delete/<int:pk>/', views.PostDeleteView.as_view(), name="post_delete"),
]
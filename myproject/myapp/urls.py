from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Пути для работы с HTML-шаблонами
    path('create/', views.create_post, name='create_post'),
    path('', views.list_posts, name='list_posts'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),

    # Пути для работы с API
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/posts/', views.BlogPostListCreate.as_view(), name='api_posts'),
    path('api/posts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='api_post_detail'),
]

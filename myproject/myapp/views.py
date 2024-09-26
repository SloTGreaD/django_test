from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Представление для создания статьи
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        BlogPost.objects.create(title=title, content=content)
        return redirect('list_posts')  # Перенаправляем на список статей после создания
    return render(request, 'myapp/create_post.html')

# Представление для отображения всех статей
def list_posts(request):
    posts = BlogPost.objects.all()
    return render(request, 'myapp/list_posts.html', {'posts': posts})

# Представление для обновления статьи
def update_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return render(request, 'myapp/success.html', {'post': post})
    return render(request, 'myapp/update_post.html', {'post': post})

# Представление для удаления статьи
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return render(request, 'myapp/success_delete.html')
    return render(request, 'myapp/confirm_delete.html', {'post': post})

# Представление для добавления комментария
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(blog_post=post, content=content)
        return render(request, 'myapp/success.html', {'post': post})
    return render(request, 'myapp/add_comment.html', {'post': post})

# Представление для списка и создания статей с аутентификацией
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Представление для работы с одной статьей
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
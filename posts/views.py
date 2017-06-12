from django.shortcuts import render
from posts.models import Post

def home(request):

  posts = Post.objects.order_by('-pub_date')


  return render(request, 'posts/home.html', {
      'posts' : posts,
    })

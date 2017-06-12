from django.shortcuts import render
from posts.models import Post

def home(request):

  posts = Post.objects.order_by('-pub_date')


  return render(request, 'posts/home.html', {
      'posts' : posts,
    })


def single_post(request, post_pk):
  """
  describes single post page
  """
  return render(request, 'posts/single_post.html', {
    'post_pk':post_pk,
    })

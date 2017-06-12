from django.shortcuts import render, get_object_or_404
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
  post = get_object_or_404(Post, pk = post_pk)

  return render(request, 'posts/single_post.html', {
    'post':post,
    })

from django.shortcuts import render, get_object_or_404
from inner_pages.models import Page



def about(request):

  page = get_object_or_404(Page, page_slug = 'about')

  return render(request, 'inner_pages/inner_page.html', {
    'page':page,
    })




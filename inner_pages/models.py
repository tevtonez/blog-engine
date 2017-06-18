from django.db import models


class Page(models.Model):

  page_title = models.CharField(max_length = 250)
  page_slug = models.CharField(max_length = 20, default = 'page-', unique = True)
  page_body = models.TextField()

  def __str__(self):
    return self.page_title

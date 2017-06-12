from django.db import models



class Post(models.Model):
  title = models.CharField(max_length = 250)
  pub_date = models.DateTimeField()
  body = models.TextField()
  image = models.ImageField(upload_to = 'media/')

  def __str__(self):
    return self.title

  def pub_date_huminize(self):
    return self.pub_date.strftime('%b %e %Y')

  def trimify_content(self):
    if len(str(self.body)) > 100:
      return self.body[:100] + "..."
    else:
      return self.body

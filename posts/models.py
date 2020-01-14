from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(status='published')



class Post(models.Model):
	STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	body = models.TextField()

	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	objects = models.Manager()
	published = PublishedManager()
	
	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title + ", " + str(self.publish)


	def get_absolute_url(self):
		return reverse('posts:post_detail', args=[self.pk, self.slug])
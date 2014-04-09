from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length = 50, unique = True)

	class Meta:
		verbose_name = 'tag'
		verbose_name_plural = 'tags'
		ordering = ['name']

	def __unicode__(self):
		return self.name

		
class Bookmark(models.Model):
	title = models.CharField(max_length = 100)
	url = models.URLField()
	owner = models.ForeignKey(User, verbose_name = 'owner', related_name = 'bookmarks')
	tags = models.ManyToManyField(Tag, blank = True) 
	date_created = models.DateTimeField('Date Created')
	date_updated = models.DateTimeField('Date Updated')

	class Meta:
		verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['title']

   	def __unicode__(self):
   		return self.title
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
		self.date_updated = now()
		super(Bookmark, self).save(*args, **kwargs)


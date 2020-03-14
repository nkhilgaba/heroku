from django.db import models
from datetime import datetime
from tinymce import HTMLField
from filebrowser.fields import FileBrowseField

class Post(models.Model):
	title=models.CharField(max_length=140)
	summary=models.CharField(max_length=250,null=True)
	#content = HTMLField('Content') 
	content=models.TextField()
	date=models.DateTimeField('published on',default=datetime.now())
	thumb=models.ImageField(blank=True,null=True) # gives choose-file option
	
	def __str__(self):
		return self.title




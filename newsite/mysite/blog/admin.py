
from django.contrib import admin
from blog.models import Post
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	'''fields=['title',
						'published',
						'content'
				]'''
	fieldsets=[
	('Title/date',{'fields':['title','date']}),
	('Summary',{'fields':['summary']}),
	('Content',{'fields':['content']}),
	('Images',{'fields':['thumb']}),
	]
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()},
    	}


admin.site.register(Post,BlogAdmin)

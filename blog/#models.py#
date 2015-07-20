import datetime

from django.db import models
from django import forms

from tinymce.models import HTMLField

from wand.image import Image

# Create your models here.

class TimeStampedModel(models.Model):

    ''' For adding timestapes to models '''
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        get_latest_by = 'modified'
        ordering = ('-modified', '-created')
    
class Post(TimeStampedModel):
    titel = models.CharField(max_length=40)
    text = HTMLField()

# class Comment(TimeStampedModel):
#     post = models.ForeignKey(Post)
#     name = models.CharField(max_length=30)
#     email = models.CharField(max_length=40)
#     message = models.TextField(max_length=300)

# class Album(TimeStampedModel):
#     title = models.CharField(max_length=250)
#     description = models.TextField(blank=True, null=True)
#     cover_photo = models.ForeignKey('Photo', related_name='+', blank=True, null=True)
#     is_public = models.BooleanField(default=True)
#     date_added = models.DateField(null=True, blank=True)
#     order = models.PositiveIntegerField(default=999)

# def uploadPhotoTo(instance, filename):
#     return 'uploads/photo/%s-%s' % (str(datetime.datetime.now().strftime('%Y%m%d')), filename.replace(' ', '_'))

# class Photo(TimeStampedModel):
#     album = models.ForeignKey(Album)
#     img = models.ImageField(upload_to=uploadPhotoTo)
#     description = models.TextField(blank=True, null=True)
#     is_public = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         super(Photo, self).save(*args, **kwargs)
#         if self.img:
#             with Image(filename=self.img.path) as img:
#                 img.save(filename=self.img.path+'.ORGINAL')
#                 img.transform(resize='x700')
#                 img.compression_quality = 90
#                 img.save(filename=self.img.path)

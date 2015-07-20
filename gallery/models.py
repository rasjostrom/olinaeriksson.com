from django.db import models

from blog.models import TimeStampedModel

from wand.image import Image

# Create your models here.

def uploadPhotoTo(instance, filename):
    return '%s' % (filename.replace(' ', '_'))


class Photo(TimeStampedModel):
    img = models.ImageField(upload_to=uploadPhotoTo)
    text = models.TextField(default='', blank=True)
    published = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        if self.img:
            with Image(filename=self.img.path) as img:
                img.save(filename=self.img.path+'.ORGINAL')
                img.transform(resize='800x')
                img.compression_quality = 90
                img.save(filename=self.img.path)

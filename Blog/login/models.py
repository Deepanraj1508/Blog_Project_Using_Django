# models.py
from django.db import models
from django.core.exceptions import ValidationError
import uuid
from django.utils import timezone

def validate_image_size(file):
    max_size_kb = 5120  # 5 MB
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Image file size should be less than 5 MB")

def validate_video_size(file):
    max_size_kb = 10240  # 10 MB
    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Video file size should be less than 10 MB")

class Extensions(models.Model):
    """ Best practice for lookup field url instead pk or slug """

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now, db_index=True)
    modified = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class BlogPost(Extensions):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', validators=[validate_image_size])
    email = models.EmailField(unique= True,default= True)
    video = models.FileField(upload_to='blog_videos/', null=True, blank=True, validators=[validate_video_size])
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

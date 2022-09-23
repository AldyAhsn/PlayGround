from django.db import models

# Create your models here.
# streamblocks/models.py

# one object
class RichText(models.Model):
    text = models.TextField(blank=True, null=True)   

    class Meta:
        # This will use as name of block in admin
        verbose_name="Text"

# list of objects
class ImageWithText(models.Model):
    image = models.ImageField(upload_to="folder/")
    text = models.TextField(null=True, blank=True)
    
    # StreamField option for list of objects
    as_list = True

    class Meta:
        verbose_name="Image with text"
        verbose_name_plural="Images with text"

# Register blocks for StreamField as list of models
STREAMBLOCKS_MODELS = [
    RichText,
    ImageWithText
]
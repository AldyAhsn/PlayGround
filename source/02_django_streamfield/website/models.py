from django.db import models

# Create your models here.
from streamfield.fields import StreamField
from streamblocks.models import RichText, ImageWithText

class Page(models.Model):
    stream = StreamField(
        model_list=[ 
            RichText,
            ImageWithText
        ],
        verbose_name="Page blocks"
        )
from django.contrib import admin

# Register your models here.
from streamfield.fields import StreamFieldWidget
from streamblocks.models import RichText
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.id == 1:
            form.base_fields['stream'].widget = StreamFieldWidget(attrs={
                'model_list': [ RichText ]
                })
        return form
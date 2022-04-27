from django.contrib import admin

from .models import FileUpload, TestMode

# Register your models here.
admin.site.register(TestMode)
admin.site.register(FileUpload)

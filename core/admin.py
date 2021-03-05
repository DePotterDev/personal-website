from django.contrib import admin
from .models import Blog


admin.site.register(Blog)
class QuillPostAdmin(admin.ModelAdmin):
    pass
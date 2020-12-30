from django.contrib import admin

from .models import Story

admin.site.site_header = 'XSTORIES'

admin.site.register(Story)
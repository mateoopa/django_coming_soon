from django.contrib import admin
from .models import Section, Content


class SectionAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'description']


class ContentAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'tittle', 'description']


admin.site.register(Section, SectionAdmin)
admin.site.register(Content, ContentAdmin)

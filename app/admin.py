from django.contrib import admin
from .models import Post, Savollar, OurWorks
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'context']
    search_fields = ['title', 'context']

admin.site.register(Post, PostAdmin)


class SavollarAdmin(admin.ModelAdmin):
    list_display = ['savol', 'javob']
    search_fields = ['savol', 'javob']

admin.site.register(Savollar, SavollarAdmin)

class OurWorksAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(OurWorks, OurWorksAdmin)
from imagekit.admin import AdminThumbnail
from django.contrib import admin
from Boroughs.models import Borough

class BoroughsAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author',
                    'created', 'modified')
    admin_thumbnail = AdminThumbnail(image_field='main_img')
    list_filter = ['title', 'created', 'author']
    search_fields = ['title', 'author']


admin.site.register(Borough, BoroughsAdmin)

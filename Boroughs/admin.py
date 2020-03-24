from imagekit.admin import AdminThumbnail
from django.contrib import admin
from Boroughs.models import Borough, Photo

class photoInline(admin.TabularInline):
    model = Photo
    extra = 0


class BoroughsAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    search_fields = ['title']
    list_filter = ['title', 'created']

    list_display = ('title', 'slug',
                    'created', 'modified')

    admin_thumbnail = AdminThumbnail(image_field='main_img')
    inlines = [photoInline]

admin.site.register(Borough, BoroughsAdmin)


class PhotoAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['borough']}),
    #     # ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    # ]

    list_display = ('content', 'image', 'borough', 'approved', 'was_published_recently', 'votes',
                    'first_name', 'last_name', 'email', 'created')
    list_filter = ['borough', 'created', 'email', 'votes']
    search_fields = ['borough', 'content']

admin.site.register(Photo, PhotoAdmin)

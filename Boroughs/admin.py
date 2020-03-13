from imagekit.admin import AdminThumbnail
from embed_video.admin import AdminVideoMixin
from django.contrib import admin
from Boroughs.models import Borough, Photo, Video

class photoInline(admin.TabularInline):
    model = Photo
    extra = 0


class BoroughsAdmin(AdminVideoMixin, admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    search_fields = ['title', 'author']
    list_filter = ['title', 'created', 'author']

    list_display = ('title', 'slug', 'author',
                    'created', 'modified')

    admin_thumbnail = AdminThumbnail(image_field='main_img')
    inlines = [photoInline]

admin.site.register(Borough, BoroughsAdmin)


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, VideoAdmin)


class PhotoAdmin(AdminVideoMixin, admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['borough']}),
    #     # ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    # ]

    list_display = ('content', 'image', 'borough', 'approved', 'was_published_recently', 'votes',
                    'first_name', 'last_name', 'email', 'created')
    list_filter = ['borough', 'created', 'email', 'votes']
    search_fields = ['borough', 'content']

admin.site.register(Photo, PhotoAdmin)

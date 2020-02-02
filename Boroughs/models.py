import datetime

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Borough(models.Model):
    """ Represents a single Borough. """
    objects = models.Manager()
    slug = models.CharField(max_length=settings.BOROUGH_TITLE_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this borough's page. Generated by the system.")
    created = models.DateTimeField(
        auto_now_add=True, help_text="The date and time this page was created. Automatically generated when the model saves.")
    modified = models.DateTimeField(
        auto_now=True, help_text="The date and time this page was updated. Automatically generated when the model updates.")
    title = models.CharField(max_length=settings.BOROUGH_TITLE_MAX_LENGTH,
                             unique=True, default="Title of your page.")
    # author = models.ForeignKey(User, on_delete=models.PROTECT, help_text="The user that posted this article.")
    borough_Main_Img = models.ImageField(upload_to='images/')
    content = models.TextField(default="Write the content of your page here.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/my-new-page). """
        path_components = {'slug': self.slug}
        return reverse('borough-detail-page', kwargs=path_components)

    def save(self, *args, **kwargs):
        """ Creates a URL safe slug automatically when a new a page is created. """
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Borough, self).save(*args, **kwargs)

from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail import blocks
# Create your models here.

class ReleasesPage(Page):
    subtitle = models.CharField(max_length=200, null=True, blank=True)

    content = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = ReleasePage.objects.live().public()
        return context

class ReleasePage(Page):
    template = "releases/releases_listing_page.html"

    subtitle = models.CharField(max_length=200, null=True, blank=True)
    custom_subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    featured = models.BooleanField(blank=True, null=True)
    release_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content =  RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("custom_subtitle"),
        FieldPanel("release_image"),
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("featured")
    ]

from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from streams import blocks


class HomePage(Page):
    body = RichTextField(blank=True)

    carousel = StreamField([
        ('carousel', blocks.Carousel())
    ], use_json_field=True, null=True, blank=True )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('carousel')
    ]

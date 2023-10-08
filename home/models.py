from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from streams import blocks

from releases import models as releases_models

class HomePage(Page):
    body = RichTextField(blank=True)

    carousel = StreamField([
        ('carousel', blocks.Carousel())
    ], use_json_field=True, null=True, blank=True )

    def get_context(self, request):
        context = super().get_context(request)

        featured_post_pages = releases_models.ReleasePage.objects.live().filter(featured=True)

        featured_pages = sorted(
            featured_post_pages,
            key=lambda page: page.first_published_at, reverse=True)

        context['featured_pages'] = featured_pages

        return context

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('carousel')
    ]

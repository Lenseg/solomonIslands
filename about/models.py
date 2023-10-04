from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from streams import blocks

# Create your models here.

class AboutPage(Page):
        """About Page class"""

        subtitle = models.CharField(max_length=200, null=True, blank=True)

        questions_and_answers = StreamField([
            ('question_and_answer', blocks.Dropdown())
        ], use_json_field=True, null=True, blank=True )

        body = RichTextField(blank=True, null=True)
        side_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            blank=False,
            on_delete=models.SET_NULL,
            related_name="+"
        )
        content_panels=Page.content_panels + [
            FieldPanel("subtitle"),
            FieldPanel("body"),
            FieldPanel("questions_and_answers"),
            FieldPanel("side_image")
        ]

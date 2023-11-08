from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from streams import blocks
from wagtail import blocks as wblocks


from releases import models as releases_models

class SuperPage(Page):
    header = RichTextField(blank=True)

    content = StreamField([
        ('subheader', blocks.Subheader(reqired=False, help_text="Subheader")),
        ('section_text_and_image', blocks.TextAndImageBLock(help_text="Text and image")),
        ('section_text', wblocks.RichTextBlock(blank=True, null=True, help_text="Section text")),
        ('section_carousel', blocks.Carousel(help_text="Section slider")),
        ('section_dropdown', blocks.Dropdown(help_text="Section dropdown")),
        ('section_two_columns', blocks.TwoColumnsBlock(help_text="Section two columns"))
    ], use_json_field=True, null=True, blank=True )

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('content')
    ]

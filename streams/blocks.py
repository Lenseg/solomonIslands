from wagtail import blocks
from django.db import models

from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page

class Dropdown(blocks.StructBlock):
    header = blocks.CharBlock(reqired=True, help_text="Dropdown header")
    contnent = blocks.RichTextBlock(blank=True, null=True, help_text="Dropdown content")

    class Meta:
        template = 'dropdown.html'

class Carousel(blocks.StructBlock):
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ('slide_image', ImageChooserBlock(
                'wagtailimages.Image',
                null=True,
                blank=False,
                on_delete=models.SET_NULL,
                related_name="+"
            ))
        ])
    )
    slide_text = blocks.CharBlock(max_length=100,required=False, blank=True, null=True)
    button_text = blocks.CharBlock(max_length=100,required=False, blank=True, null=True)
    button_link = blocks.URLBlock(max_length=200,required=False, null=True, blank=True)

    class Meta:
        template = 'carousel.html'

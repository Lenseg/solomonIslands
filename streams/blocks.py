from wagtail import blocks
from django.db import models

from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


class TextAndImageBLock(blocks.StructBlock):
    image = ImageChooserBlock(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    text = blocks.RichTextBlock(blank=True, null=True, help_text="Section text")
    button_text = blocks.CharBlock(blank=True, null=True, required=False, help_text="Button text")
    button_link = blocks.URLBlock(blank=True, null=True, required=False, help_text="Button link")

    class Meta:
        template = 'textandimage.html'

class Dropdown(blocks.StructBlock):
    dropdown = blocks.ListBlock(
            blocks.StructBlock([
                ('label', blocks.CharBlock(reqired=True, help_text="Dropdown header")),
                ('content', blocks.RichTextBlock(blank=True, null=True, help_text="Dropdown content"))
            ])
        )
    class Meta:
        template = 'dropdown.html'

class Subheader(blocks.StructBlock):
    text = blocks.RichTextBlock(blank=True, null=True, help_text="Subheader text")

    class Meta:
        template = 'subheader.html'

class Carousel(blocks.StructBlock):
    slides = blocks.ListBlock(
        blocks.StructBlock([
            ('slide_image', ImageChooserBlock(
                'wagtailimages.Image',
                null=True,
                blank=False,
                on_delete=models.SET_NULL,
                related_name="+"
            )),
            ('slide_text', blocks.CharBlock(max_length=100,required=False, blank=True, null=True)),
            ('button_text', blocks.CharBlock(max_length=100,required=False, blank=True, null=True)),
            ('button_link', blocks.URLBlock(max_length=200,required=False, null=True, blank=True))
        ])
    )
    use_root_text = blocks.BooleanBlock(default=True, required=False)
    slide_text = blocks.CharBlock(max_length=100,required=False, blank=True, null=True)
    button_text = blocks.CharBlock(max_length=100,required=False, blank=True, null=True)
    button_link = blocks.URLBlock(max_length=200,required=False, null=True, blank=True)

    class Meta:
        template = 'carousel.html'


class TwoColumnsBlock(blocks.StructBlock):
    leftBlock = blocks.StreamBlock([
        ('section_text', blocks.RichTextBlock(blank=True, null=True, help_text="Section text")),
        ('section_carousel', Carousel(help_text="Section slider")),
        ('section_dropdown', Dropdown(help_text="Section dropdown"))
    ], use_json_field=True, null=True, blank=True )

    rightBlock = blocks.StreamBlock([
        ('section_text', blocks.RichTextBlock(blank=True, null=True, help_text="Section text")),
        ('section_carousel', Carousel(help_text="Section slider")),
        ('section_dropdown', Dropdown(help_text="Section dropdown"))
    ], use_json_field=True, null=True, blank=True )

    class Meta:
        template = 'two_columns.html'

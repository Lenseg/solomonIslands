from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

# Create your models here.
@register_setting
class GlobalSiteSettings(BaseSiteSetting):

    logo =  models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    facebook = models.URLField(blank=True, null=True, help_text="Facebook Url")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter Url")
    youtube = models.URLField(blank=True, null=True, help_text="Youtube Url")

    phone = models.CharField(blank=True, max_length=100, null=True, help_text="Contact phone")
    email = models.CharField(blank=True, max_length=100, null=True, help_text="Contact email")
    address = models.CharField(blank=True, max_length=200, null=True, help_text="Contact address")

    links = StreamField([
        ('link', blocks.StructBlock([
            ('link_text', blocks.CharBlock(max_length=100,required=True, blank=True, null=True)),
            ('link_url', blocks.URLBlock(max_length=300,required=True, blank=True, null=True)),
        ]))
    ], use_json_field=True, null=True, blank=True )

    panels = [
        FieldPanel("logo"),
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube")
        ], heading = 'Social Media Settings'),
        MultiFieldPanel([
            FieldPanel("phone"),
            FieldPanel("email"),
            FieldPanel("address")
        ], heading = 'Contacts Settings'),
        MultiFieldPanel([
            FieldPanel("links"),
        ], heading = 'Footer Links')
    ]

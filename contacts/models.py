from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtailmenus.models import MenuPageMixin
from wagtailmenus.panels import menupage_settings_panels

from wagtail import blocks
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm

# Create your models here.

class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactsPage',
        on_delete=models.CASCADE,
        related_name='form_fields'
    )

class ContactsPage(AbstractEmailForm, MenuPageMixin):

    subtitle = models.CharField(max_length=200, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    thank_you_text = RichTextField(blank=True, null=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        InlinePanel('form_fields', heading = "Form Fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6")
            ]),
            FieldPanel('subject')
        ], heading = "Email settings")
    ]
    settings_panels = menupage_settings_panels

# class ContactsPage(Page):
#
#         subtitle = models.CharField(max_length=200, null=True, blank=True)
#
#         body = RichTextField(blank=True, null=True)
#
#         offices = StreamField([
#             ('office', blocks.ListBlock(
#                 blocks.StructBlock([
#                     ('office_name',
#                         blocks.CharBlock(max_length=200,required=True, blank=True, null=True)
#                     ),
#                     ('office_type',
#                         blocks.CharBlock(max_length=200,required=True, blank=True, null=True)
#                     )
#                 ])
#             ))
#         ], use_json_field=True, null=True, blank=True)
#
#         content_panels=Page.content_panels + [
#             FieldPanel("subtitle"),
#             FieldPanel("body"),
#             FieldPanel("offices")
#         ]

# Generated by Django 4.2.5 on 2023-10-12 22:48

from django.db import migrations
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('superpage', '0005_alter_superpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superpage',
            name='content',
            field=wagtail.fields.StreamField([('subheader', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(blank=True, help_text='Subheader text', null=True))], help_text='Subheader', reqired=False)), ('section_text_and_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock('wagtailimages.Image', blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')), ('text', wagtail.blocks.RichTextBlock(blank=True, help_text='Section text', null=True)), ('button_text', wagtail.blocks.CharBlock(blank=True, help_text='Button text', null=True, reqired=False)), ('button_link', wagtail.blocks.URLBlock(blank=True, help_text='Button link', null=True, reqired=False))], help_text='Text and image')), ('section_text', wagtail.blocks.RichTextBlock(blank=True, help_text='Section text', null=True)), ('section_carousel', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(help_text='Dropdown header', reqired=True)), ('contnent', wagtail.blocks.RichTextBlock(blank=True, help_text='Dropdown content', null=True))], help_text='Section dropdown'))], blank=True, null=True, use_json_field=True),
        ),
    ]

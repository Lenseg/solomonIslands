# Generated by Django 4.2.5 on 2023-09-26 15:10

from django.db import migrations
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_homepage_banner_cta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='carousel',
            field=wagtail.fields.StreamField([('carousel', wagtail.blocks.StructBlock([('slides', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('slide_image', wagtail.images.blocks.ImageChooserBlock('wagtailimages.Image', blank=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+')), ('slide_text', wagtail.blocks.CharBlock(blank=True, max_length=100, null=True)), ('button_text', wagtail.blocks.CharBlock(blank=True, max_length=100, null=True)), ('button_link', wagtail.blocks.URLBlock(blank=True, max_length=200, null=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]

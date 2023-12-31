# Generated by Django 4.2.5 on 2023-09-27 22:17

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_globalsitesettings_delete_socialmediasettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsitesettings',
            name='links',
            field=wagtail.fields.StreamField([('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(blank=True, max_length=100, null=True, required=True)), ('link_url', wagtail.blocks.URLBlock(blank=True, max_length=300, null=True, required=True))]))], blank=True, null=True, use_json_field=True),
        ),
    ]

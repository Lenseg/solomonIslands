# Generated by Django 4.2.5 on 2023-10-15 14:24

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contactspage_repeat_in_subnav_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactspage',
            name='offices',
            field=wagtail.fields.StreamField([('office', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('office_name', wagtail.blocks.CharBlock(blank=True, max_length=200, null=True, required=True)), ('office_phone', wagtail.blocks.CharBlock(blank=True, max_length=200, null=True, required=False)), ('office_adress', wagtail.blocks.CharBlock(blank=True, max_length=200, null=True, required=False)), ('lat', wagtail.blocks.CharBlock(blank=True, max_length=200, null=True, required=True)), ('lng', wagtail.blocks.CharBlock(blank=True, max_length=200, null=True, required=True))])))], blank=True, null=True, use_json_field=True),
        ),
    ]
# Generated by Django 4.2.5 on 2023-10-17 18:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_alter_aboutpage_questions_and_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='questions_and_answers',
            field=wagtail.fields.StreamField([('questions_and_answers', wagtail.blocks.StructBlock([('dropdown', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(help_text='Dropdown header', reqired=True)), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='Dropdown content', null=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]

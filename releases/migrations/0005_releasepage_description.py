# Generated by Django 4.2.5 on 2023-10-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0004_alter_releasepage_content_alter_releasespage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='releasepage',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

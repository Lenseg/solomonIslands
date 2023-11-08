from django.db import models

from wagtail.models import Page
from wagtail.search import index

from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail import blocks

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your models here.

class ReleasesPage(RoutablePageMixin, Page):


    subtitle = models.CharField(max_length=200, null=True, blank=True)

    content = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("content")
    ]
    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = ReleasePage.objects.child_of(self).live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 9)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context

class ReleasePage(Page, index.Indexed):
    template = "releases/releases_listing_page.html"

    subtitle = models.CharField(max_length=200, null=True, blank=True)
    custom_subtitle = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    date = models.DateField("Event date", null=True, blank=True)
    featured = models.BooleanField(blank=True, null=True)
    release_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content =  RichTextField(null=True, blank=True)

    search_fields = Page.search_fields + [ # Inherit search_fields from Page
        index.SearchField('description'),
        index.SearchField('content'),
        index.SearchField('subtitle'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel("custom_subtitle"),
        FieldPanel("release_image"),
        FieldPanel("description"),
        FieldPanel("content"),
        FieldPanel("date"),
        FieldPanel("featured")
    ]

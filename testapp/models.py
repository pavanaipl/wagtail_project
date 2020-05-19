from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
# Create your models here.

class UsersDetails(Page):

    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile_number = models.CharField(max_length=11, null=True, blank=True)
    age = models.IntegerField(default=0)
    dob = models.DateField(null=True, blank=True)
    user_image = models.ForeignKey("wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('name'),
        FieldPanel('email'),
        FieldPanel('mobile_number'),
        FieldPanel('age'),
        ImageChooserPanel('user_image'),

    ]
    def __str__(self):
        return self.name

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]



# Create your models here.

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.core.fields import StreamField
from streams import blocks

class FlexPage(Page):


    template = 'flex/flex_page.html'
    max_count = 1

    content = StreamField([
        ("title_and_text", blocks.TitleAndTextBlock()),

    ],
        null=True, blank=True
    )

    subtitle = models.CharField(max_length=150, null=True, blank=True)


    content_panels = Page.content_panels + [

        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

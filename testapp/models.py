from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from django.shortcuts import render

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


class EmployeeDetails(models.Model):

    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    designation = RichTextField(blank=True)
    number = models.IntegerField()


from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractForm.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),

    ]


class FlavourSuggestionPage(Page):
    intro = RichTextField(blank=True)
    thankyou_page_title = models.CharField(
        max_length=255, help_text="Title text to use for the 'thank you' page")


    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('thankyou_page_title'),
    ]

    def serve(self, request):
        from testapp.forms import EmployeeForm

        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                flavour = form.save()
                return render(request, 'testapp/thankyou.html', {
                    'page': self,
                    'flavour': flavour,
                })
        else:
            form = EmployeeForm()

        return render(request, 'testapp/suggest.html', {
            'page': self,
            'form': form,
        })
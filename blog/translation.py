from .models import BlogIndexPage, BlogPage

from wagtail_modeltranslation.translation import TranslationOptions
from modeltranslation.decorators import register

@register(BlogIndexPage)
class BlogIndexPageTR(TranslationOptions):
    fields = (
    )


@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = (
        'body',
    )

from .models import BlogIndexPage, BlogPage

@register(BlogIndexPage)
class BlogIndexPageTR(TranslationOptions):
    fields = (
    )


@register(BlogPage)
class BlogPageTR(TranslationOptions):
    fields = (
        'body',
    )

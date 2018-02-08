from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, BlogTag
from common.translation import CommonPostTranslationOptions


class BlogTranslationOptions(CommonPostTranslationOptions):
	fields = ('title', 'author', 'text', 'seo_title', 'seo_keywords', 'seo_description',)

class BlogTagTranslationOptions(TranslationOptions):
    	fields = ('tag','seo_title', 'seo_keywords', 'seo_description',)

translator.register(Blog, BlogTranslationOptions)
translator.register(BlogTag, BlogTagTranslationOptions)

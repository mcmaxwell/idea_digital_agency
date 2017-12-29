from modeltranslation.translator import translator, TranslationOptions
from .models import Blog, BlogTag
from common.translation import CommonPostTranslationOptions


class BlogTranslationOptions(CommonPostTranslationOptions):
	fields = ('title', 'author', 'text')

class BlogTagTranslationOptions(TranslationOptions):
    	fields = ('tag',)

translator.register(Blog, BlogTranslationOptions)
translator.register(BlogTag, BlogTagTranslationOptions)
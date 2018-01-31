from modeltranslation.translator import translator, TranslationOptions
from .models import Info
from common.translation import CommonPostTranslationOptions



class InfoTranslationOptions(TranslationOptions):
	fields = ('adress_footer','seo_title_blog', 'seo_keywords_blog', 'seo_description_blog')

translator.register(Info, InfoTranslationOptions)

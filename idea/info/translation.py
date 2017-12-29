from modeltranslation.translator import translator, TranslationOptions
from .models import Info
from common.translation import CommonPostTranslationOptions



class InfoTranslationOptions(TranslationOptions):
	fields = ('adress_footer',)

translator.register(Info, InfoTranslationOptions)

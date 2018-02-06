from modeltranslation.translator import translator, TranslationOptions
from .models import Case, CaseService
from common.translation import CommonPostTranslationOptions


class CaseTranslationOptions(TranslationOptions):
	fields = ('activity_title', 'title', 'client', 'project','case_site', 'text', 'seo_title', 'seo_keywords', 'seo_description',)

class CaseServiceTranslationOptions(TranslationOptions):
    	fields = ('title',)

translator.register(Case, CaseTranslationOptions)
translator.register(CaseService, CaseServiceTranslationOptions)

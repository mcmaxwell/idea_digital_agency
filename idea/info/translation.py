from modeltranslation.translator import translator, TranslationOptions
from .models import Info, TeamMember
from common.translation import CommonPostTranslationOptions



class InfoTranslationOptions(TranslationOptions):
	fields = ('adress_footer','seo_title_blog', 'seo_keywords_blog', 'seo_description_blog')

class TeamMemberTranslationOptions(TranslationOptions):
	fields = ('name','position',)

translator.register(Info, InfoTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)

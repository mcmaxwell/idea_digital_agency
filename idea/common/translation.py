from modeltranslation.translator import translator, TranslationOptions


class CommonPostTranslationOptions(TranslationOptions):
    fields = ('title','author','text')

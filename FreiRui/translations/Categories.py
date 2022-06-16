from modeltranslation.translator import TranslationOptions


class CategoriesTranslationOptions(TranslationOptions):
    fields = ('name', 'short_name', 'title', 'video_url', 'published')

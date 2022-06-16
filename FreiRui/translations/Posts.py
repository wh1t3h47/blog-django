from modeltranslation.translator import TranslationOptions


class PostsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'is_deleted')

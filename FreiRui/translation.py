from modeltranslation.translator import translator
from FreiRui.models.Posts import Posts
from FreiRui.models.Categories import Categories
from FreiRui.translations.Posts import PostsTranslationOptions
from FreiRui.translations.Categories import CategoriesTranslationOptions

translator.register(Posts, PostsTranslationOptions)
translator.register(Categories, CategoriesTranslationOptions)

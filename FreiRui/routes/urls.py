from typing import List
from django.urls import URLPattern, path

from FreiRui import routes

'''
importa todos os arquivos de rotas do diretório routes e concatena na
urlpatterns
'''

urlpatterns: List[URLPattern] = []

for route in routes.__all__:
    route = __import__(f'FreiRui.routes.{route}', fromlist=['urlpatterns'])
    urlpatterns += route.urlpatterns

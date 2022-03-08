from django.urls import path
from .views_api import *
from .marvel_api_views import *

urlpatterns = [
    #vistas de prueba
    path('saludo/', saludo),
    path('query/', queryset),
    path('total/', total),
    #vistas de la api de ejemplos de clase
    path('get-comics/', get_comics),
    path('purchase-item/', purchased_item),
    
]

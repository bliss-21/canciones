from django.urls import path
from .views import home, listado,cancion, biblia

urlpatterns = [
    path('', home, name="home"),
    path('listado/', listado, name="listado"),
    path('listado/<id>/', listado, name="listado"),
    path('cancion/<id>/', cancion, name="cancion"),
    path('biblia', biblia, name="biblia"),
]
from django.urls import path
from .views import home, accesorios, contacto, comida, listar_contactos

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('accesorios/', accesorios, name="accesorios"),
    path('comida/', comida, name="comida"),
    path('listar/', listar_contactos, name="listar"),

]
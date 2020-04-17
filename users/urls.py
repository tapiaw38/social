from django.urls import path
from users import views


urlpatterns = [
    path('ingresar/',views.sign_in, name='sign_in'),
    path('salir/',views.log_out, name='log_out'),
]
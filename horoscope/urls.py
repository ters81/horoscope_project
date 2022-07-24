from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type', views.types_list),
    path('type/<str:type_zodiac>', views.type_zodiac, name='type-name'),
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),
]
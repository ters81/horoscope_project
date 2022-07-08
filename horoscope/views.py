from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': "Знак зодиака - Овен",
    'taurus': "Знак зодиака - Телец",
    'gemini': "Знак зодиака - Близнецы",
    'cancer': "Знак зодиака - Рак",
    'leo': "Знак зодиака - Лев",
    'virgo': "Знак зодиака - Дева",
    'libra': "Знак зодиака - Весы",
    'scorpio': "Знак зодиака - Скорпион",
    'sagittarius': "Знак зодиака - Стрелец",
    'capricorn': "Знак зодиака - Козерог",
    'aquarius': "Знак зодиака - Водолей",
    'pisces': "Знак зодиака - Рыбы"
}


def get_info_about_sign_zodiac(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac > len(zodiac_dict) or sign_zodiac == 0:
        return HttpResponse(f"Неправильный значание номера знака Зодиака - {sign_zodiac}")
    else:
        zodiac_name = list(zodiac_dict)[sign_zodiac - 1]
        redirect_url = reverse('horoscope-name', args=(zodiac_name,))
        return HttpResponseRedirect(redirect_url)


def index(request):
    li_elements = ''
    for sign in zodiac_dict:
        redirect_path = reverse('horoscope-name', args=(sign,))
        li_elements += f"<li> <a href='{redirect_path}'> {sign.capitalize()} </a> </li>"
    response = f'<ul>{li_elements}</ul>'
    return HttpResponse(response)

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    'aries': ("Знак зодиака - Овен", 'fire'),
    'taurus': ("Знак зодиака - Телец", 'earth'),
    'gemini': ("Знак зодиака - Близнецы", 'air'),
    'cancer': ("Знак зодиака - Рак", 'water'),
    'leo': ("Знак зодиака - Лев", 'fire'),
    'virgo': ("Знак зодиака - Дева", 'earth'),
    'libra': ("Знак зодиака - Весы", 'air'),
    'scorpio': ("Знак зодиака - Скорпион",'water'),
    'sagittarius': ("Знак зодиака - Стрелец", 'fire'),
    'capricorn': ("Знак зодиака - Козерог", 'earth'),
    'aquarius': ("Знак зодиака - Водолей", 'air'),
    'pisces': ("Знак зодиака - Рыбы",'water'),
}


def get_info_about_sign_zodiac(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description[0]}</h2>')
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


def types_list(request):
    types_of_signes = set()
    for sign in zodiac_dict.values():
        types_of_signes.add(sign[1])

    li_elements = ''
    for sign in types_of_signes:
        redirect_path = reverse('type-name', args=(sign,))
        li_elements += f"<li> <a href='{redirect_path}'> {sign.capitalize()} </a> </li>"
    response = f'<ul>{li_elements}</ul>'
    return HttpResponse(response)


def type_zodiac(request, sign_type):
    redirect_url = reverse('type/type-name', args=(sign_type,))


    return HttpResponseRedirect(redirect_url)
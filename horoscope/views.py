from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def aries(request):
    return HttpResponse("Знак зодиака - Овен")


def taurus(request):
    return HttpResponse("Знак зодиака - Телец")


def gemini(request):
    return HttpResponse("Знак зодиака - Близнецы")


def cancer(request):
    return HttpResponse("Знак зодиака - Рак")


def leo(request):
    return HttpResponse("Знак зодиака - Лев")


def virgo(request):
    return HttpResponse("Знак зодиака - Дева")


def libra(request):
    return HttpResponse("Знак зодиака - Весы")


def scorpio(request):
    return HttpResponse("Знак зодиака - Скорпион")


def sagittarius(request):
    return HttpResponse("Знак зодиака - Стрелец")


def capricorn(request):
    return HttpResponse("Знак зодиака - Козерог")


def aquarius(request):
    return HttpResponse("Знак зодиака - Водолей")


def pisces(request):
    return HttpResponse("Знак зодиака - Рыбы")

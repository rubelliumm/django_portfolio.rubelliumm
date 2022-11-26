from django.shortcuts import render
from django.http import JsonResponse


def fifawcpredictorhome(request):
    return render(request, 'fifawcpredictor/fifa_home.html')


def test(request):
    print(request)
    return JsonResponse({'name': "rubelliumm"})

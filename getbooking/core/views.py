from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def view_week(request, year, month, day):
    return render(request, 'core/view_week.html')

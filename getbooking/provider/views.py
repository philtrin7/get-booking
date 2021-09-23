from django.shortcuts import render


def view_week(request, year, month, day):
    return render(request, 'provider/view_week.html')

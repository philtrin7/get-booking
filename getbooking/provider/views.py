from django.shortcuts import render


def view_week(request, year, month, day):
    return render(request, 'core/view_week.html')

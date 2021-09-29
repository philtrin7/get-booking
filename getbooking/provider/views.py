import requests
import pytz
import datetime as dt

from django.http import Http404
from django.shortcuts import render

from getbooking.settings import CRONOFY_CLIENT_ID, CRONOFY_CLIENT_SECRET, CRONOFY_REFRESH_TOKEN, TIME_ZONE

LOCALTZ = pytz.timezone(TIME_ZONE)


def request_cronofy_access_token():
    client_id = CRONOFY_CLIENT_ID
    client_secret = CRONOFY_CLIENT_SECRET
    refresh_token = CRONOFY_REFRESH_TOKEN

    base_url = "https://api.cronofy.com/oauth/token?client_id=%s&client_secret=%s&grant_type=refresh_token&refresh_token=%s" % (
        client_id, client_secret, refresh_token)

    try:
        request = requests.post(base_url)
    except requests.exceptions.ConnectionError as err:
        print(err)
    except requests.exceptions.RequestException as err:
        print(err)

    return request.json()


def view_week(request, year, month, day):
    try:
        date = LOCALTZ.localize(dt.datetime(
            int(year), int(month), int(day), hour=9))
    except ValueError:
        raise Http404("Date does not exist")

    print(date)
    # access_token = request_cronofy_access_token()
    # print(access_token)
    return render(request, 'provider/view_week.html')

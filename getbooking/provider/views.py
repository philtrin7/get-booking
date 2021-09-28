import requests
from django.shortcuts import render


def request_cronofy_access_token():
    client_id = ""
    client_secret = ""
    grant_type = ""
    refresh_token = ""

    base_url = "https://api.cronofy.com/oauth/token?client_id=%s&client_secret=%s&grant_type=%s&refresh_token=%s" % (
        client_id, client_secret, grant_type, refresh_token)

    try:
        request = requests.post(base_url)
    except requests.exceptions.ConnectionError as err:
        print(err)
    except requests.exceptions.RequestException as err:
        print(err)

    return request.json()


def view_week(request, year, month, day):
    return render(request, 'provider/view_week.html')

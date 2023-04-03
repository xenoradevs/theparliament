# flask app
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():

    current_date = datetime.date.today()

    formatted_date = current_date.strftime('%A, %d %B %Y').replace(
        '{0}', str(current_date.day) + suffix(current_date.day))

    # get number of followers on facebook
    followers = get_followers()
    data = {
        'name': 'Daily News Strem',
        'date': formatted_date,
        'slogan': 'The best news in the world',
        'trending': ['2024 AFCON', '2022 World Cup', '2022 Olympics', '2022 FIFA World Cup'],
        'followers': {
            'facebook': followers,
            'twitter': '120',
            'instagram': '780',
            'linkedin': '1420',
        },
        'rubrics': {
            'sport': 'Sport',
            'politics': 'Politics',
            'economic': 'Economic',
            'culture': 'Culture',
            'science': 'Science',
            'technology': 'Technology',
            'education': 'Education',

        }



    }
    return render_template('index.html', content=data)


def get_followers():
    access_token = 'EABUxSCgZCq5YBAD9IEYhsyNC7fPatYrOqybmqciwHJ5V4tc8B6ULuAoRH9DE2dIUbcnAjEBIvSpmFhr9lYV2MMhkQzXLHLXB9LVfivCjgBw4KdhR5qyGeeHEcnLkI1lFxq8129cbJmiZA1YZCq0blutpF6Ht0NSLP5NyUlRZCnerOt3CSSyZBl91uhmb5yf1sZAuylKJgfottPtDsFl4Yk'

    page_id = "bravetechsolutions"
    url = f"https://graph.facebook.com/v13.0/{page_id}?fields=fan_count&access_token={access_token}"

    response = requests.get(url)
    data = response.json()

    followers = data["fan_count"]
    return followers
    print(f"Number of followers of the page {page_id}: {followers}")


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

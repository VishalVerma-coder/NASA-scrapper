from datetime import date, timedelta
import requests
start_date = date(2010, 1, 1)
end_date = date(2020, 1, 1)
delta = timedelta(days=1)

while start_date <= end_date:
    import os
    import urllib.request
    print (start_date.strftime('%Y-%m-%d'))

    key = "mg7TL8NkoSbmUKd41ddhjfeoNLYZrcUNcJsIhgqj"
    params = {'date': start_date.strftime('%Y-%m-%d'),
          'hd': True,
          'api_key': key}

    # Get request
    r = requests.get("https://api.nasa.gov/planetary/apod",params=params)
    r = r.json()

    urllib.request.urlretrieve(r['hdurl'], r['date']+'.jpg')
    start_date += delta

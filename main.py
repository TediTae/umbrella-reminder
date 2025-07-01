import requests
import smtplib

latitude = 41.008240 # This latitude is for Istanbul you should get your own latitude from latlong website.
longitude = 28.978359 # This longitude is for Istanbul you should get your own longitude from latlong website.
api_key = "Your own api key" # you should sign in and get your own api key for that to work.
USER = "your mail address here"
PASSWORD = "your app password"

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= weather_params)
response.raise_for_status()
data = response.json()

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")  # if using gmail
    connection.starttls()
    connection.login(USER, PASSWORD)
    connection.sendmail(
        from_addr=USER,
        to_addrs=USER,
        msg="Subject:Reminder\n\nDont forget to get your umbrella today."
    )

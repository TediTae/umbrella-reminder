# Umbrella Reminder ☔

A simple Python script that checks the upcoming weather forecast using the OpenWeatherMap API and sends an email reminder if rain is expected.

## 🌦️ Features

- Fetches weather forecast based on your coordinates.
- Checks for rain conditions in the next few hours.
- Sends an automatic email reminding you to take an umbrella.
- Uses OpenWeatherMap API and SMTP (Gmail supported).

## 📦 Requirements

- Python 3.x
- `requests` library
- An OpenWeatherMap API key
- A Gmail account with an app password

## 🔧 Installation
1. **Clone the repository**
2. pip install requests.
3. Set up your environment variables
  - fill your credentials directly in the script:
  - api_key = "YOUR_OPENWEATHERMAP_API_KEY"
  - USER = "your_email@gmail.com"
  - PASSWORD = "your_app_password"
4. Run the script : main.py

## 📌 Notes
- Weather condition codes below 700 usually indicate rain or similar precipitation.
- Use a scheduler (like cron or Windows Task Scheduler) to automate this script daily.

## 🔒 Security Tip
- Never share your email password or API key. Use environment variables or .env files, and add .env to your .gitignore if pushing to GitHub.

##📄 License
- MIT License

## Contact
- tolgayilmaz1377@gmail.com

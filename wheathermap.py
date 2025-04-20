import requests
import matplotlib.pyplot as plt
import datetime

API_KEY = "45ae5e4f3925286a8f881965635b679f"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Check if 'list' exists
if "list" in data:
    dates = []
    temperatures = []

    for item in data['list']:
        dt = datetime.datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']

        dates.append(dt)
        temperatures.append(temp)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f"5-Day Weather Forecast for {CITY}", fontsize=16)
    plt.xlabel("Date and Time", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("Error fetching weather data:", data.get("message", "Unknown error"))

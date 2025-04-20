# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PANKAJ KUMAR

*INTERN ID*: CT04DA498

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

**Task Description:**

The objective of this task is to develop a Python-based application that fetches real-time data from a public API, such as OpenWeatherMap, and creates insightful visualizations using Matplotlib. This project combines skills in API integration, data processing, and data visualization, providing a practical foundation for handling real-world datasets and presenting them effectively.

**1. Introduction to API Integration:**

An Application Programming Interface (API) allows different software systems to communicate with each other. Public APIs like OpenWeatherMap offer valuable real-time data such as weather conditions, temperature, humidity, and more. In this task, we will utilize the OpenWeatherMap API to fetch weather data for a specified location. Accessing the API requires an API key, which is provided upon registering at the OpenWeatherMap website.

**2. Fetching Data Using Python:**

Python’s `requests` library will be used to send HTTP GET requests to the API endpoint. The endpoint typically includes the API key and query parameters like city name and units (metric or imperial). The API responds with data in JSON format, which can easily be parsed using Python's built-in `json` module or by handling the response object directly.

Example snippet:
```python
import requests

api_key = "your_api_key"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()
```
The fetched data includes information like temperature, weather conditions, humidity, wind speed, and atmospheric pressure.

**3. Processing the Data:**

After fetching the data, the next step is to process it for visualization. Important data points like current temperature, minimum and maximum temperatures, weather description, and humidity can be extracted from the JSON response. Data can be organized into lists or dictionaries, especially if collecting data for multiple cities or over different timestamps.

Example:
```python
temperature = data['main']['temp']
humidity = data['main']['humidity']
description = data['weather'][0]['description']
```

**4. Creating Visualizations Using Matplotlib:**

Matplotlib is a powerful plotting library in Python used for creating static, animated, and interactive visualizations. Using the extracted weather data, various types of plots can be created:

- **Bar Charts:** Compare temperatures across different cities.
- **Line Graphs:** Show temperature changes over time if data is collected at intervals.
- **Pie Charts:** Display proportions of different weather conditions in a dataset.
- **Scatter Plots:** Analyze relationships between temperature and humidity.

Example of a simple bar chart:
```python
import matplotlib.pyplot as plt

cities = ['London', 'New York', 'Tokyo']
temperatures = [15, 10, 20]

plt.bar(cities, temperatures, color='skyblue')
plt.title('Temperature Comparison')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.show()
```

**5. Conclusion:**

This task emphasizes the full workflow from data retrieval to data visualization. Students or developers will learn how to connect with external data sources using APIs, extract and organize JSON data, and create professional-quality visualizations. Mastering these skills is essential for roles in data science, software development, and data analysis, where making data understandable through visualization is critical. Additionally, handling APIs introduces learners to important concepts like authentication, error handling, and working with real-time dynamic data.

#OUTPUT

![Screenshot (1484)](https://github.com/user-attachments/assets/5b870546-3bfd-46cc-b5c8-ce03cb08b3e7)


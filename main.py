import requests
import os
from tkinter import Tk, Label, Entry, Button


def get_weather():
  city = city_entry.get()
  print(f"Fetching weather for city: {city}")  # Debugging line
  # Get API key from environment variable for security
  api_key = os.getenv("OPENWEATHER_API_KEY")
  if not api_key:
      raise ValueError("API key not found. Set the OPENWEATHER_API_KEY environment variable.")
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  try:
    response = requests.get(url)
    data = response.json()
    print(data)  # Debugging line to see the full response
    if data["cod"] == 200:
      temp = data["main"]["temp"]
      humidity = data["main"]["humidity"]
      description = data["weather"][0]["description"]
      result_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nDescription: {description}")
    else:
      result_label.config(text="City not found.")
  except:
    result_label.config(text="Error fetching data.")


#GUI setup
root = Tk()
root.title("Weather App")
root.geometry("300x200")

city_entry = Entry(root, width=30)
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")


get_button = Button(root, text="Get Weather", command=get_weather)
get_button.pack(pady=5) 

result_label = Label(root, text="")
result_label.pack(pady=10)

font = ("Helvetica", 12)
root.mainloop()
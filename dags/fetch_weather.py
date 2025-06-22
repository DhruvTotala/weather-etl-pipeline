import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_weather(city="Mumbai"):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise Exception("❌ API key not found. Please check your .env file.")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"❌ Error fetching weather data: {data.get('message')}")

    weather_info = {
        "city": city,
        "timestamp": datetime.utcnow(),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

    df = pd.DataFrame([weather_info])
    os.makedirs("data", exist_ok=True)
    output_file = f"data/{city}_weather.csv"
    df.to_csv(output_file, index=False)

    print(f"✅ Weather data for {city} saved to {output_file}")

# 👇 This line ensures it runs when the script is executed directly
if __name__ == "__main__":
    fetch_weather()

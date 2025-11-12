import requests

def get_weather(city_name):
    API_KEY = "bc2f0da777333de8516c33aab9817422"  # Replace with your own API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        print("\n🌍 Weather Report for:", data['name'])
        print("🌡 Temperature:", data['main']['temp'], "°C")
        print("💧 Humidity:", data['main']['humidity'], "%")
        print("🌥 Condition:", data['weather'][0]['description'].title())
        print("🌬 Wind Speed:", data['wind']['speed'], "m/s")

    except requests.exceptions.HTTPError:
        print("❌ City not found. Please check the name and try again.")
    except Exception as e:
        print("⚠️ Error:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)

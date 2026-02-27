# Copyright by Emilio

import requests
import json
import time
from datetime import datetime

capitals_list = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]

weather_description = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight showers",
    81: "Moderate showers",
    82: "Heavy showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail"
}


def get_weather(lat, lon):
    print("deubg - API Anfrage laeuft...")
    api_url = "https://api.open-meteo.com/v1/forecast"
    today = datetime.now().strftime("%Y-%m-%d")

    query_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation_probability,weathercode",
        "temperature_unit": "celsius",
        "windspeed_unit": "kmh",
        "timezone": "auto",
        "start_date": today,
        "end_date": today
    }

    try:
        response = requests.get(api_url, params=query_params, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result

    except requests.exceptions.Timeout:
        print(f"  [ERROR] Timeout for coordinates ({lat}, {lon})")
        return None

    except requests.exceptions.ConnectionError:
        print(f"  [ERROR] No connection for ({lat}, {lon})")
        return None

    except requests.exceptions.HTTPError as e:
        print(f"  [ERROR] HTTP error: {e}")
        return None

    except Exception as e:
        print(f"  [ERROR] Something went wrong: {e}")
        return None


def parse_response(raw_data, city_name, country_name):
    if raw_data is None:
        return None

    try:
        cw = raw_data["current_weather"]
        code = cw.get("weathercode")

        current = {
            "temperature": cw.get("temperature"),
            "windspeed": cw.get("windspeed"),
            "weathercode": code,
            "condition": weather_description.get(code, "Unknown"),
            "time": cw.get("time")
        }

        hourly_data = raw_data.get("hourly", {})
        hours = []

        times = hourly_data.get("time", [])
        temps = hourly_data.get("temperature_2m", [])
        precip = hourly_data.get("precipitation_probability", [])
        codes = hourly_data.get("weathercode", [])

        for i in range(len(times)):
            hour_entry = {
                "time": times[i],
                "temperature": temps[i],
                "precipitation_probability": precip[i],
                "weathercode": codes[i],
                "condition": weather_description.get(codes[i], "Unknown")
            }
            hours.append(hour_entry)

        city_data = {
            "country": country_name,
            "coordinates": {
                "latitude": raw_data.get("latitude"),
                "longitude": raw_data.get("longitude")
            },
            "current_weather": current,
            "hourly_forecast": hours
        }

        return city_data

    except KeyError as e:
        print(f"  [ERROR] Missing key for {city_name}: {e}")
        return None
    except Exception as e:
        print(f"  [ERROR] Could not process data for {city_name}: {e}")
        return None


def save_json(data, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n[OK] Saved to {filename} ({len(data)} cities)")

    except IOError as e:
        print(f"[ERROR] Could not write file: {e}")


def main():
    print("=" * 45)
    print("  EU CAPITALS WEATHER DATA COLLECTOR")
    print("  by Emilio :)")
    print("=" * 45)
    print("Loading weather data, this takes a moment...")

    all_weather = {}
    total = len(capitals_list)

    for i, capital in enumerate(capitals_list):
        city = capital["city"]
        country = capital["country"]
        lat = capital["lat"]
        lon = capital["lon"]

        print(f"[{i+1}/{total}] Loading {city}, {country}...")

        raw = get_weather(lat, lon)
        parsed = parse_response(raw, city, country)

        if parsed is not None:
            all_weather[city] = parsed
            print(f"  [OK] Data received for {city}")
        else:
            print(f"  [SKIPPED] No data for {city}")

        if i < total - 1:
            time.sleep(1)

    output_filename = "eu_weather_data.json"
    save_json(all_weather, output_filename)

    if len(all_weather) == 0:
        print("\n[!] No data collected. Check internet connection.")
        return

    print("\n--- Quick Summary ---")
    print(f"Cities collected: {len(all_weather)} / {total}")

    hottest_city = None
    coldest_city = None
    hottest_temp = None
    coldest_temp = None
    temp_sum = 0
    temp_count = 0

    for city_name, city_info in all_weather.items():
        temp = city_info["current_weather"]["temperature"]

        if temp is None:
            continue

        temp_sum += temp
        temp_count += 1

        if hottest_temp is None or temp > hottest_temp:
            hottest_temp = temp
            hottest_city = city_name

        if coldest_temp is None or temp < coldest_temp:
            coldest_temp = temp
            coldest_city = city_name

    if temp_count > 0:
        avg_temp = temp_sum / temp_count
        print(f"Average temperature: {avg_temp:.1f}°C")
        print(f"Hottest city: {hottest_city} with {hottest_temp}°C")
        print(f"Coldest city: {coldest_city} with {coldest_temp}°C")
    print("Fertig!")


if __name__ == "__main__":
    main()

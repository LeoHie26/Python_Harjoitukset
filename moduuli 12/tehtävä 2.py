import requests

api_key = "40fa5d5805c022f4b88e88e0e506b769"

try:

    search_city = input("Enter municipality name: ")

    search = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={search_city},FI&appid={api_key}")

    if search.status_code == 200:
        j = search.json()
        city = j[0]
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={city['lat']}&lon={city['lon']}&units=metric&appid={api_key}")
        weather = weather.json()
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        print(f"Weather: {desc}")
        print(f"Temperature: {temp}")

    else:
        print(f"Error: status code {search.status_code}")

except requests.exceptions.RequestException as e:
    print("can not proceed with search.")



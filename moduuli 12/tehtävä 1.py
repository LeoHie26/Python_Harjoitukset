import requests


search = "https://api.chucknorris.io/jokes/random"
try:
    answer = requests.get(search)
    if answer.status_code==200:
        j = answer.json()
        print(j["value"])

    else:
        print(f"Error: status code {answer.status_code}")
        
except requests.exceptions.RequestException as e:
    print("can not proceed with search.")

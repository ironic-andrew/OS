import requests
import time

url = "https://www.chnu.edu.ua/"

start_time = time.time()
try:
    response = requests.get(url)
    end_time = time.time()
    if response.status_code == 200:
        print(f"Сайт доступний, час відповіді: {round((end_time - start_time)*1000)} мс")
    else:
        print(f"Сайт недоступний, код відповіді: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Помилка при підключенні: {e}")

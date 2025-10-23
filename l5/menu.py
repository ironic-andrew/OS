import requests
import time
import psutil

while True:
    print("\nМеню:")
    print("1. Переглянути процеси")
    print("2. Пінгувати сайт(https://www.chnu.edu.ua/)")
    print("3. Вийти")

    choice = input("Виберіть дію: ")

    match choice:
        case "1":

            for proc in psutil.process_iter(['pid', 'name', 'username']):
                try:
                    print(proc.info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

        case "2":

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

        case "3":

            print("Удачи!")
            break

        case _:
            print("Невірний вібір")










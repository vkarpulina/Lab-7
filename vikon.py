print('ЗАДАНИЕ 1')
import requests
API_KEY = "a7eaca8c0ec28ce1aaf6da6e93694202"
city_name = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ru"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_desc = data["weather"][0]["description"]
    print(f"Город: {city}, {country}")
    print(f"Температура: {temperature}°C (ощущается как {feels_like}°C)")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Погода: {weather_desc.capitalize()}")
else:
    print("Ошибка! Проверьте API-ключ или название города.")

print('ЗАДАНИЕ 2')
import requests
import json


def get_hh_vacancies(search_query, area=1, per_page=5):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": search_query,
        "area": area,
        "per_page": per_page
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        vacancies = data.get("items", [])
        for vacancy in vacancies:
            title = vacancy.get("name", "Нет названия")
            employer = vacancy.get("employer", {}).get("name", "Неизвестный работодатель")
            salary = vacancy.get("salary", {})
            salary_from = salary.get("from", "Не указано")
            salary_to = salary.get("to", "Не указано")
            salary_currency = salary.get("currency", "")
            url = vacancy.get("alternate_url", "Нет ссылки")

            print("==========================")
            print(f"Вакансия: {title}")
            print(f"Компания: {employer}")
            print(f"Зарплата: {salary_from} - {salary_to} {salary_currency}")
            print(f"Ссылка: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    SEARCH_QUERY = "Python разработчик"
    AREA = 1
    get_hh_vacancies(SEARCH_QUERY, AREA)

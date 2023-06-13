import requests
from secrets import kinopoisk_api


def movie_search(film_name):
    # Параметры запроса
    params = {
        "name": f"{film_name}"
    }

    # Заголовки запроса
    headers = {
        "accept": "application/json",
        "X-API-KEY": kinopoisk_api
    }

    # Выполнение GET-запроса
    response = requests.get("https://api.kinopoisk.dev/v1.3/movie?page=1&limit=10&", params=params, headers=headers)

    # Проверка успешности запроса и получение данных
    if response.status_code == 200:
        data = response.json()
        # Обработка полученных данных
        id = data['docs'][0].get('id')
        link = 'https://kinopoisk-watch-dsze5.ondigitalocean.app/player/?id=' + str(id)
        return link
    else:
        print("Ошибка при выполнении запроса:", response.status_code)

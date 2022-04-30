import requests
import yadisk
import datetime
import json


def photo():

                        # Работа с вк APi
    URL = "https://api.vk.com/method/photos.get"
    params = {
        "user_ids": "1",
        "access_token": token,
        "v": "5.131",
        "owner_id": id_profile,
        "album_id": "wall",
        "count": col_photo,
        "extended": "1"
    }

    res = requests.get(URL, params=params).json()
    res1 = res['response']['items']

        # Словари для записи Имен, Ссылки и Размера фото
    name = []
    url_photo = []
    size = []


    name.append([str(photo["likes"]['count']) for photo in res1]) # из всего списка берём количество лайков с фото

    size.append([str(url["sizes"][-1]["type"]) for url in res1]) # из всего списка берём максимальный размер

    url_photo.append([str(url["sizes"][-1]["url"]) for url in res1]) # из всего списка берём URL фото



                            # Работа с YaDisk
    y = yadisk.YaDisk(token=TOKEN_YA)

    name_folder = datetime.datetime.now().strftime("%d-%m-%Y \n%H.%M.%S")  # Имя для папки сегодняшняя дата
    y.mkdir(name_folder)  # Создание папки


                          # Открытие json файла
    def write(data, filename):
        data = json.dumps(data)
        data = json.loads(str(data))
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    jsFile = []

                            # Загрузка всех фото
    i = 0
    while i < len(name[0]):
        print(f"\n\nЗАГРУЖЕНО ФОТО {i+1}/{len(name[0])}\nИмя фотографии: {name[0][i]} \nРазмер фотографии: {size[0][i]} \nСсылка на фото: {url_photo[0][i]}")
        y.upload_url({url_photo[0][i]}, f"{name_folder}/{name[0][i]}.jpg")  # Загрузка фото

                    # Сохранение информации загруженных фото в json файле
        n_data = [{
            "file_name": f"{name[-1][i]}.jpg",
            "size": f"{size[-1][i]}"
        }]
        jsFile.append(n_data)


        i += 1

                        # Запись в json файл
    write(jsFile, "data.json")


                        # Запуск программы
if __name__ == "__main__":

    token = ""  # Token приложения вк
    id_profile = input("Введите Id пользователя: ")
    TOKEN_YA = input("Введите токен вашего YaDisk: ")
    col_photo = int(input("Введите количество фото которое нужно сохранить: "))
    photo()



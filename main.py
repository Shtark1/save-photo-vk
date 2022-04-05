import requests
import yadisk
import datetime


def photo():

                        # Работа с вк APi
    URL = "https://api.vk.com/method/photos.get"
    params = {
        "user_ids": "1",
        "access_token": token,
        "v": "5.131",
        "owner_id": id_profile,
        "album_id": "wall",
        "count": "5",
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


                            # Загрузка всех фото
    i = 0
    while i < len(name[0]):
        print(f"\n\nИмя фотографии: {name[0][i]} \nРазмер фотографии: {size[0][i]} \nСсылка на фото: {url_photo[0][i]}")
        y.upload_url({url_photo[0][i]}, f"{name_folder}/{name[0][i]}.jpg")  # Загрузка фото

        i += 1




if __name__ == "__main__":

    token = ""  # Token приложения вк
    id_profile = input("Введите Id пользователя: ")
    TOKEN_YA = input("Введите токен вашего YaDisk: ")
    photo()

from pprint import pprint

import requests

from reddit import Reddit
from ya_disk import YandexDisk
from SuperHero import SuperHero

TOKEN = "AQAAAAA_-a3uAADLW0DvyJL2LEq4m0o58yrwTcY"
SH = ['Captain America','Thanos','Hulk']
test_dict = {'key1':'hello', 'key2':'bay'}
URL = 'https://cloud-api.yandex.net/v1/disk/resources'

# def test_request():
    # url = "https://bootssizes/get"
    # url = "https://www.httpbin.org/get"

    # params = {"model": "nike123","model1": "nike2222"}
    # headers = {"Authorization": "secret - token - 123"}
    # response = requests.get(url, params=params, headers=headers, timeout=5)
    # response = requests.get(url)
    # pprint(response.json())


if __name__ == '__main__':
    # test_request()
    # reddit = Reddit()
    # pprint(reddit.get_popular_videos())
    # ya = YandexDisk(token=TOKEN)
    dict_hero = {}

    sh = SuperHero()
    for hero in SH:
         dict_hero[hero] = sh.get_files_list(hero)

    intelligence = 0
    for i,j in dict_hero.items():
        if intelligence < int(j['results'][0]['powerstats']['intelligence']):
            intelligence = int(j['results'][0]['powerstats']['intelligence'])
            super_hero = i
        print(i)
        print(j['results'][0]['powerstats']['intelligence'])
    print ('Наибольший интеллект=',intelligence, ' у героя:',super_hero)

    # dic = {'count': 157748,
    #        'items': [
    #            {'id': 1094057, 'title': '1 Александровка', 'area': 'Уваровский район', 'region': 'Тамбовская область'},
    #            {'id': 1112583, 'title': '1 Военный', 'area': 'Карабаш город', 'region': 'Челябинская область'},
    #            {'id': 1086151, 'title': '1 Городок', 'area': 'Хвалынский район', 'region': 'Саратовская область'}]}
    #
    # lst = [it['title'] for it in dic['items']]
    # lst

    # for sh_pw_key in dict_hero.items():
    #     print(sh_pw_key)





    # просмотр спсика файлов на диске
    # pprint(sh.get_files_list())


    # создаем каталог
    # ya.create_folder('netology_1')
    # пишем файл в каталог
    # sh.upload_file_to_disk('netology_1/test.txt','C:\Work\development\Python\Lecture\Lecture_requests\\test.txt')
    # sh.upload_file_to_disk('netology_1/img_0036.jpg','C:\\Work\\foto\\Крым 2020\\img_0036.jpg')

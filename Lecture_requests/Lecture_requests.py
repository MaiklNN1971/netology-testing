from pprint import pprint

import requests

from reddit import Reddit
from ya_disk import YandexDisk

TOKEN = "AQAAAAA_-a3uAADLW0DvyJL2LEq4m0o58yrwTcY"
URL = 'https://cloud-api.yandex.net/v1/disk/resources'

def test_request():
    # url = "https://bootssizes/get"
    url = "https://www.httpbin.org/get"

    # params = {"model": "nike123","model1": "nike2222"}
    # headers = {"Authorization": "secret - token - 123"}
    # response = requests.get(url, params=params, headers=headers, timeout=5)
    response = requests.get(url)
    pprint(response.json())


if __name__ == '__main__':
    # test_request()
    # reddit = Reddit()
    # pprint(reddit.get_popular_videos())
    ya = YandexDisk(token=TOKEN)
    # просмотр спсика файлов на диске
    # pprint(ya.get_files_list())
    # создаем каталог
    ya.create_folder('netology_1')
    # пишем файл в каталог
    ya.upload_file_to_disk('netology_1/test.txt','C:\Work\development\Python\Lecture\Lecture_requests\\test.txt')
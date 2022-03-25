from pprint import pprint

import requests


class SuperHero:
    # def __init__(self, hero):
    #     self.SuperHero = hero

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self, hero):
        # files_url = 'https://superheroapi.com/api/2619421814940190/149/powerstats'
        files_url = 'https://superheroapi.com/api/2619421814940190/search/'+hero
        response = requests.get(files_url)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.text)
        pprint(response.json())
        return response.json()

    def create_folder(self,path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        """Создание папки. \n path: Путь к создаваемой папке."""
        requests.put(f'{upload_url}?path={path}', headers=headers)

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json["href"]
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
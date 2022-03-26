import requests
import os

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_upload_link(self, file_path):
        """Функция для получения ссылки для загрузки файла"""
        upload_link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_path, 'overwrite': 'true'}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        response = requests.get(upload_link, params=params, headers=headers)
        return response.json()

    def upload_file(self, file_path):
        """Функция для загрузки файла"""
        for file in file_path:
            href_json = self.get_upload_link(file)
            href = href_json['href']
            response = requests.put(href, data=open(FILES_DIR + file, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("File uploaded successfully!")


if __name__ == '__main__':

    token = input('Please, enter TOKEN: ')

    BASE_DIR = os.getcwd()
    FILES_DIR = 'files/'
    files_path = os.path.join(BASE_DIR, FILES_DIR)
    file_list = os.listdir(files_path)

    uploader = YandexDisk(token)
    uploader.upload_file(file_list)
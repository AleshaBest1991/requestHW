from pprint import pprint

import requests

TOKEN = 'y0_AgAAAABbDBNyAADLWwAAAADSgnSGn1nbYkrpSbWMgl5AG7Wx8-2kow4'
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path)
        url = href.get('href', '')
        response = requests.put(url, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
        disk_file_path = 'netology/test.txt'
        token = 'y0_AgAAAABbDBNyAADLWwAAAADSgnSGn1nbYkrpSbWMgl5AG7Wx8-2kow4'
        uploader = YaUploader(token=TOKEN)
        uploader.upload(disk_file_path=disk_file_path, filename='test.txt')

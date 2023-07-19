import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {"Authorization": self.token}
        file_name = file_path.split('\\')[-1]
        params = {"path": file_name}
        response = requests.get(url, headers=headers, params=params).json()
        url = response.get("href", "")
        with open(file_path, 'rb') as f:
            response = requests.put(url, files={"file": f}, headers=headers, params=params)
            return(response.status_code)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:\\Users\\pushk\\Desktop\\buduku.jpg"
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)


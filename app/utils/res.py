import requests


class Res():
    def __init__(self):
        super().__init__()

    def data_raw(self, keyword):
        img = requests.get('http://127.0.0.1:8088/api/v1/get_image?url=https://www.tiket.com/hotel/indonesia/aston-mojokerto-hotel-conference-center-511001669349429617?room=1&adult=1&checkin=2024-04-05&checkout=2024-04-06&referrer=https%3A%2F%2Fwww.tiket.com%2Fhotel%2Fsearch%3Froom%3D1%26adult%3D1%26id%3Deast-java-108001534490276152%26type%3DREGION%26q%3DJawa%2520Timur%26checkin%3D2024-03-22%26checkout%3D2024-03-23&utm_page=searchResultPage').json()
        return img
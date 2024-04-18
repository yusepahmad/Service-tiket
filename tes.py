import requests


class Res():
    def __init__(self):
        super().__init__()

    def get_link(self, start, end):
        headers = {
            'accept': 'application/json',
        }

        params = {
            'url': 'https://www.tiket.com/hotel/search?room=1&adult=1&id=east-java-108001534490276152&type=REGION&q=Jawa%20Timur',
            'check_in': '2024-03-22',
            'check_out': '2024-03-22',
            'start': start,
            'end': end,
        }

        response = requests.get('http://127.0.0.1:8098/api/v1/get_link_range', params=params, headers=headers).json()
        return response

    def image(self, url):
        headers = {
            'accept': 'application/json',
        }

        params = {
            'url': url,
        }
        try:
            response = requests.get('http://127.0.0.1:8098/api/v1/get_image', params=params, headers=headers).json()
        except:
            response = {}
        return response

    def information(self, link):
        headers = {
            'accept': 'application/json',
        }

        params = {
            'url': f'https://www.tiket.com{link}',
        }
        try:
            response = requests.get('http://127.0.0.1:8098/api/v1/get_info', params=params, headers=headers).json()
        except:
            response = {}

        return response

    def review(self, id):
        headers = {
            'accept': 'application/json',
        }

        params = {
            'id': id,
        }

        try:
            response = requests.get('http://127.0.0.1:8098/api/v1/get_review', params=params, headers=headers).json()
        except:
            response = {}

        return response



# response = Res().get_link('0','1')
#
# for data in response:
#     link = data.get('link')
#     id = data.get('id_hotel')
#
#     print(id)

    # img = Res().image(f'https://www.tiket.com{link}')
    # info = Res().information(link)
    # reviews = Res().review(id)

    # info.update({'review':reviews, 'img_link':img})



    # print(info)
    # print()
    # print(reviews)
    # print()
    # print(img)


# print(Res().review('aston-mojokerto-hotel-conference-center-511001669349429617'))

response = requests.get('http://127.0.0.1:8098/api/v1/get_review?id=monoloog-hotel-surabaya-609001695617428336').json()
print(response)
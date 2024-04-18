
from .parser import Parsing

class Helper(Parsing):
    def __init__(self):
        super().__init__()

    def mapping_hotel(self, name=None, rating=None, price=None, addres=None, popular=None, other=None, check_in=None, check_out=None, policy=None, about=None, room=None):
        data = {
        "link": 'https://www.tiket.com',
        "domain": 'tiket.com',
        "tag": [
            'tiket',
            'hotel',
            'review'
        ],
            'name_hotel' :name,
            'rating_hotel' :rating,
            'price' :price,
            'address' :addres,
            'popular _facilities': popular,
            'other_facilities' :other,
            'check_in' :check_in,
            'check_out' :check_out,
            'policy' :policy,
            'about' :about,
            'room' :room,
        },

        return data

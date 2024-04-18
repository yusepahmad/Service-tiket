
from .hardcode import HardCode

class SoftCode(HardCode):
    def __init__(self):
        super().__init__()


    async def get_id_soft(self, keyword):
        response = await self.get_id_hard(keyword)
        return response

    async def get_link_soft(self, url, index):
        response = await self.get_link_hard(url, index)
        return response

    async def get_image_soft(self, url):
        response = await self.get_image_hard(url)
        return response

    async def get_info_soft(self, url):
        response = await self.get_info_hard(url)
        return response

    async def get_review_soft(self, id):
        response = await self.review(id)
        return response

    async def get_all_content(self):
        response = await self.data_raw('jawa')
        return response


    async def get_link_range_soft(self, url, start, end):
        response = await self.get_link_range_hard(url, start, end)
        return response
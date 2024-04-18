import asyncio
from fastapi import APIRouter, Query
from typing import Optional

from ..utils.softcode import SoftCode

router = APIRouter()


@router.get("/get_image")
async def get_image(
        url : str = Query(
            example='https://www.tiket.com/hotel/indonesia/aston-mojokerto-hotel-conference-center-511001669349429617?room=1&adult=1&checkin=2024-04-05&checkout=2024-04-06&referrer=https%3A%2F%2Fwww.tiket.com%2Fhotel%2Fsearch%3Froom%3D1%26adult%3D1%26id%3Deast-java-108001534490276152%26type%3DREGION%26q%3DJawa%2520Timur%26checkin%3D2024-03-22%26checkout%3D2024-03-23&utm_page=searchResultPage',
            description='Link page hotel content'
        )
):
    response = await SoftCode().get_image_soft(url)
    return response

@router.get("/get_info")
async def get_info(
        url : str = Query(
            example='https://www.tiket.com/hotel/indonesia/aston-mojokerto-hotel-conference-center-511001669349429617?room=1&adult=1&checkin=2024-04-05&checkout=2024-04-06&referrer=https%3A%2F%2Fwww.tiket.com%2Fhotel%2Fsearch%3Froom%3D1%26adult%3D1%26id%3Deast-java-108001534490276152%26type%3DREGION%26q%3DJawa%2520Timur%26checkin%3D2024-03-22%26checkout%3D2024-03-23&utm_page=searchResultPage',
            description='Link page hotel content'
        )
):
    response = await SoftCode().get_info_soft(url)
    return response

@router.get("/get_review")
async def get_link_review(
        id : str = Query(
            example='aston-mojokerto-hotel-conference-center-511001669349429617',
            description='id hotel'
        )
):
    response = await SoftCode().get_review_soft(id)
    return response

@router.get("/get_data_raw")
async def data_raw():
    response = await SoftCode().get_all_content()
    return response
import asyncio
from fastapi import APIRouter, Query
from typing import Optional

from ..utils.softcode import SoftCode

router = APIRouter()

@router.get("/get_id")
async def get_id(
        keyword: str = Query(
            example='Jawa Timur',
            description='Keyword by province'
        )
):
    response = await SoftCode().get_id_soft(keyword)
    return response


@router.get("/get_link")
async def get_link(
        url: str = Query(
            example='https://www.tiket.com/hotel/search?room=1&adult=1&id=east-java-108001534490276152&type=REGION&q=Jawa%20Timur',
            description="Link page hotel list"
        ),
        check_in : str = Query(
            example='2024-03-22',
            description='Date Check-In'
        ),
        check_out : str = Query(
            example='2024-03-22',
            description='Date Check-Out'
        ),
        index: str = Query(
            example='0',
            description='index hotel'
        )
):
    url = f'{url}&checkin={check_in}&checkout{check_out}'
    response = await SoftCode().get_link_soft(url, index)
    return response


@router.get("/get_link_range")
async def get_link_range(
        url: str = Query(
            example='https://www.tiket.com/hotel/search?room=1&adult=1&id=east-java-108001534490276152&type=REGION&q=Jawa%20Timur',
            description="Link page hotel list"
        ),
        check_in : str = Query(
            example='2024-03-22',
            description='Date Check-In'
        ),
        check_out : str = Query(
            example='2024-03-22',
            description='Date Check-Out'
        ),
        start: int = Query(
            example='0',
            description='index start'
        ),
        end: int = Query(
            example='0',
            description='index end'
        )
):
    url = f'{url}&checkin={check_in}&checkout{check_out}'
    response = await SoftCode().get_link_range_soft(url, start, end)
    return response

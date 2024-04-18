from fastapi import APIRouter
from ..service.service_code import router as information
from ..service.service_crawl import router as crawl_data


router = APIRouter()

router.include_router(information, tags=["Automation Data information"], prefix="/api/v1")
router.include_router(crawl_data, tags=["Automation Crawl Content"], prefix="/api/v1")

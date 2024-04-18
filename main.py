from fastapi import FastAPI
from app.routes.route import router

app = FastAPI(title='Service Tiket.com', description="Crawl Data information Hotel by keyword", version='1.0.1 Beta')
app.include_router(router)
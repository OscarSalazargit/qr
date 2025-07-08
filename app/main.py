from fastapi import FastAPI
from app.routes import qr

app = FastAPI(title="QR Code Generator API")

app.include_router(qr.router, prefix="/api/qr", tags=["QR Codes"])

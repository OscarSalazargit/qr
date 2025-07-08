from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from app.services.qr_generator import generate_qr_code

router = APIRouter()

@router.get("/generate")
def generate_qr(data: str = Query(..., description="Texto o URL para generar el código QR")):
    filepath, filename = generate_qr_code(data)
    return FileResponse(filepath, media_type="image/png", filename=filename)

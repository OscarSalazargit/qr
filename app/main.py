from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import qr

app = FastAPI(title="QR Code Generator API")

# Rutas de la API
app.include_router(qr.router, prefix="/api/qr", tags=["QR Codes"])

# Servir contenido estático
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")

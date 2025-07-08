import qrcode
import uuid
import os

QR_DIR = "app/static/qrcodes"

def generate_qr_code(data: str):
    # Crear carpeta si no existe
    os.makedirs(QR_DIR, exist_ok=True)

    # Crear código QR genera un objeto imagen con el código QR basado en el contenido data.
    qr = qrcode.make(data)

    #Esto genera el nombre unico para el archivo
    filename = f"{uuid.uuid4()}.png"
    filepath = os.path.join(QR_DIR, filename)
    qr.save(filepath) #guarda el QR como imagen PNG en disco

    return filepath, filename

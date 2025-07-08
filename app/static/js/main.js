async function generateQR() {
    const text = document.getElementById("qr-text").value;
    if (!text) {
        alert("Introduce un texto o URL.");
        return;
    }

    // Petición a la API
    const response = await fetch(`/api/qr/generate?data=${encodeURIComponent(text)}`);
    if (!response.ok) {
        alert("Error generando el QR");
        return;
    }

    // Crear blob e imagen
    const blob = await response.blob();
    const imageUrl = URL.createObjectURL(blob);

    // Mostrar imagen
    const img = document.getElementById("qr-image");
    img.src = imageUrl;
    img.style.display = "block";

    // Mostrar botón de descarga
    const link = document.getElementById("download-link");
    link.href = imageUrl;
    link.download = "qr_code.png";
    link.style.display = "inline";
    link.textContent = "Descargar QR";
}
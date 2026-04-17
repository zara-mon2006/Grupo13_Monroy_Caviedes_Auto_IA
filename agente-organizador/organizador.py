"""
Agente Organizador de Archivos con IA (Claude).
Escanea una carpeta, clasifica archivos con Claude y los organiza automáticamente.
"""
import os
import json
import shutil
from pathlib import Path
import anthropic

def escanear_carpeta(ruta_carpeta: str) -> list[str]:
    """
    Escanea una carpeta y retorna la lista de archivos (no carpetas).
    """
    carpeta = Path(ruta_carpeta)
    
    if not carpeta.exists():
        print(f"❌ Error: La carpeta '{ruta_carpeta}' no existe.")
        return []
    
    if not carpeta.is_dir():
        print(f"❌ Error: '{ruta_carpeta}' no es una carpeta.")
        return []
    
    archivos = [f.name for f in carpeta.iterdir() if f.is_file()]
    
    if not archivos:
        print(f"⚠️ La carpeta '{ruta_carpeta}' está vacía.")
        return []
    
    print(f"📂 Se encontraron {len(archivos)} archivos en '{ruta_carpeta}':")
    for archivo in sorted(archivos):
        print(f"   📄 {archivo}")
    
    return archivos

def clasificar_con_claude(archivos: list[str]) -> dict:
    """
    Envía la lista de archivos a Claude para que los clasifique por categoría.
    """
    client = anthropic.Anthropic(
        api_key=open(".env").read().split("=")[1].strip()
    )
    
    lista_archivos = "\n".join(f"- {archivo}" for archivo in archivos)
    
    prompt = f"""Eres un asistente que clasifica archivos en categorías.
Analiza los siguientes nombres de archivos y clasifica CADA UNO en exactamente 
UNA de estas categorías:
- documentos (PDF, Word, texto, presentaciones)
- imagenes (fotos, capturas, diagramas)
- codigo (scripts, páginas web, estilos)
- audio_video (música, podcasts, videos, grabaciones)
- datos (hojas de cálculo, CSV, JSON, bases de datos)
- comprimidos (ZIP, RAR, TAR, 7Z)
- otros (archivos que no encajen en ninguna categoría anterior)

IMPORTANTE: Clasifica basándote en el NOMBRE y la EXTENSIÓN del archivo.
Si un archivo no tiene extensión, intenta deducir su tipo por el nombre.

Archivos a clasificar:
{lista_archivos}

Responde ÚNICAMENTE con un JSON válido con esta estructura exacta:
{{
    "nombre_archivo.ext": "categoria",
    "otro_archivo.ext": "categoria"
}}
No incluyas explicaciones, solo el JSON."""

    print("\n🤖 Enviando archivos a Claude para clasificación...")
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    respuesta = message.content[0].text
    respuesta_limpia = respuesta.strip()
    if respuesta_limpia.startswith("```"):
        lineas = respuesta_limpia.split("\n")
        lineas = [l for l in lineas if not l.strip().startswith("```")]
        respuesta_limpia = "\n".join(lineas)
    
    try:
        clasificacion = json.loads(respuesta_limpia)
        print(f"✅ Claude clasificó {len(clasificacion)} archivos:")
        for archivo, categoria in sorted(clasificacion.items()):
            print(f"   📄 {archivo} → 📁 {categoria}")
        return clasificacion
    except json.JSONDecodeError as e:
        print(f"❌ Error al parsear respuesta: {e}")
        return {}

# --- Prueba rápida ---
if __name__ == "__main__":
    archivos = escanear_carpeta("desordenada")
    if archivos:
        clasificacion = clasificar_con_claude(archivos)
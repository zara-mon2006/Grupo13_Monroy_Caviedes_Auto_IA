"""
Agente Organizador de Archivos con IA (Claude).
Escanea una carpeta, clasifica archivos con Claude y los organiza automáticamente.
"""
import os
import json
import shutil
from pathlib import Path
import anthropic
from datetime import datetime

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

def mover_archivos(ruta_carpeta: str, clasificacion: dict) -> dict:
    """
    Mueve los archivos a subcarpetas según la clasificación de Claude.
    """
    carpeta = Path(ruta_carpeta)
    estadisticas = {}
    errores = []
    
    for archivo, categoria in clasificacion.items():
        origen = carpeta / archivo
        destino_carpeta = carpeta / categoria
        destino = destino_carpeta / archivo
        
        if not origen.exists():
            errores.append(f"No encontrado: {archivo}")
            continue
        
        destino_carpeta.mkdir(exist_ok=True)
        
        try:
            shutil.move(str(origen), str(destino))
            estadisticas[categoria] = estadisticas.get(categoria, 0) + 1
        except Exception as e:
            errores.append(f"Error moviendo {archivo}: {e}")
    
    print("\n📊 Resumen de organización:")
    print("-" * 40)
    for categoria, cantidad in sorted(estadisticas.items()):
        print(f"   📁 {categoria}: {cantidad} archivo(s)")
    print("-" * 40)
    total = sum(estadisticas.values())
    print(f"   ✅ Total movidos: {total}")
    
    if errores:
        print(f"\n⚠️ Errores ({len(errores)}):")
        for error in errores:
            print(f"   ❌ {error}")
    
    return estadisticas, errores

def mostrar_plan(clasificacion: dict) -> None:
    """Muestra el plan de organización antes de ejecutar."""
    categorias = {}
    for archivo, categoria in clasificacion.items():
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(archivo)
    
    print("\n" + "=" * 55)
    print("📋 PLAN DE ORGANIZACIÓN")
    print("=" * 55)
    for categoria, archivos in sorted(categorias.items()):
        print(f"\n📁 {categoria}/ ({len(archivos)} archivos)")
        for archivo in sorted(archivos):
            print(f"   └── {archivo}")
    print("\n" + "=" * 55)

def guardar_log(ruta_carpeta: str, estadisticas: dict, errores: list) -> None:
    """Guarda un registro de la organización en log_organizacion.txt"""
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log_organizacion.txt", "a", encoding="utf-8") as log:
        log.write("\n" + "=" * 55 + "\n")
        log.write(f"📅 Fecha y hora: {ahora}\n")
        log.write(f"📂 Carpeta organizada: {ruta_carpeta}\n")
        log.write("-" * 55 + "\n")
        
        log.write("Archivos movidos:\n")
        for categoria, cantidad in sorted(estadisticas.items()):
            log.write(f"   📁 {categoria}: {cantidad} archivo(s)\n")
        
        total = sum(estadisticas.values())
        log.write(f"   ✅ Total: {total} archivos\n")
        
        if errores:
            log.write("\nErrores:\n")
            for error in errores:
                log.write(f"   ❌ {error}\n")
        
        log.write("=" * 55 + "\n")
    
    print(f"\n📝 Log guardado en 'log_organizacion.txt'")

def main():
    """Función principal del agente organizador."""
    print("=" * 55)
    print("🐍 AGENTE ORGANIZADOR DE ARCHIVOS CON IA")
    print("   Powered by Claude (Anthropic)")
    print("=" * 55)
    
    ruta = input("\n📂 Ingresa la ruta de la carpeta a organizar: ").strip()
    
    if not ruta:
        ruta = "desordenada"
        print(f"   Usando carpeta por defecto: '{ruta}'")
    
    print("\n" + "-" * 55)
    print("PASO 1: Escaneando carpeta...")
    print("-" * 55)
    archivos = escanear_carpeta(ruta)
    
    if not archivos:
        print("\n🛑 No hay archivos para organizar. Finalizando.")
        return
    
    print("\n" + "-" * 55)
    print("PASO 2: Clasificando con Claude...")
    print("-" * 55)
    clasificacion = clasificar_con_claude(archivos)
    
    if not clasificacion:
        print("\n🛑 No se pudo clasificar. Finalizando.")
        return
    
    mostrar_plan(clasificacion)
    
    respuesta = input("\n¿Deseas ejecutar este plan? (s/n): ").strip().lower()
    
    if respuesta != "s":
        print("\n🚫 Operación cancelada por el usuario.")
        return
    
    print("\n" + "-" * 55)
    print("PASO 3: Moviendo archivos...")
    print("-" * 55)
    estadisticas, errores = mover_archivos(ruta, clasificacion)
    guardar_log(ruta, estadisticas, errores)
    
    print("\n" + "=" * 55)
    print("🎉 ¡ORGANIZACIÓN COMPLETADA!")
    print("=" * 55)
    print(f"Revisa la carpeta '{ruta}' para ver el resultado.")

if __name__ == "__main__":
    main()
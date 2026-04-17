"""
Script para crear archivos de prueba en una carpeta 'desordenada'.
"""
import os

CARPETA = "desordenada"

ARCHIVOS = [
    "informe_final_proyecto.pdf",
    "tarea_matematicas_semana4.docx",
    "notas_de_clase_fisica.txt",
    "presentacion_grupo.pptx",
    "curriculum_vitae_2026.pdf",
    "foto_vacaciones_playa.jpg",
    "screenshot_error_codigo.png",
    "diagrama_circuito_motor.png",
    "selfie_graduacion.jpeg",
    "mi_primer_script.py",
    "utilidades_matematicas.py",
    "pagina_portafolio.html",
    "estilos_web.css",
    "podcast_tecnologia_ep5.mp3",
    "tutorial_python_basico.mp4",
    "grabacion_clase_virtual.wav",
    "datos_ventas_marzo.csv",
    "respuestas_encuesta.xlsx",
    "configuracion_servidor.json",
    "backup_proyecto_final.zip",
    "recursos_diseno.rar",
    "readme_instrucciones",
    "notas_rapidas",
]

def crear_archivos():
    os.makedirs(CARPETA, exist_ok=True)
    for archivo in ARCHIVOS:
        ruta = os.path.join(CARPETA, archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(f"Archivo de prueba: {archivo}\n")
    print(f"✅ Se crearon {len(ARCHIVOS)} archivos en '{CARPETA}/'")
    for archivo in sorted(ARCHIVOS):
        print(f"   📄 {archivo}")

if __name__ == "__main__":
    crear_archivos()
    
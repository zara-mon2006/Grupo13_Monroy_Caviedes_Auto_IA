**Proyecto 2 — Grupo 13 | Software de Automatización | Segundo Corte**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![Claude](https://img.shields.io/badge/Anthropic-Claude_API-purple?style=flat-square)
![VS Code](https://img.shields.io/badge/Editor-VS_Code-007ACC?style=flat-square)
![Agente IA](https://img.shields.io/badge/Agente-IA-green?style=flat-square)

---

## 📌 Descripción

Agente de **Inteligencia Artificial** desarrollado en Python que escanea una carpeta desordenada, utiliza la API de Claude (Anthropic) para clasificar cada archivo por categoría y los organiza automáticamente en subcarpetas. Todo el proceso se ejecuta desde Visual Studio Code.

---

## 🏗️ Arquitectura del Agente

| Capa | Función | Tecnología |
|---|---|---|
| **Percepción** | Escanea el directorio y lista los archivos | `os`, `pathlib` |
| **Razonamiento** | Claude decide la categoría de cada archivo | Anthropic API |
| **Acción** | Crea subcarpetas y mueve los archivos | `shutil`, `os` |

---

## 📁 Categorías de Organización

| Categoría | Tipos de archivo |
|---|---|
| `documentos/` | .pdf, .docx, .txt, .pptx |
| `imagenes/` | .jpg, .png, .jpeg |
| `codigo/` | .py, .html, .css |
| `audio_video/` | .mp3, .mp4, .wav |
| `datos/` | .csv, .xlsx, .json |
| `comprimidos/` | .zip, .rar |
| `otros/` | Archivos sin categoría definida |

---

## 🗂️ Estructura del Proyecto

```
proyecto2_agente_organizador/
├── organizador.py           # Agente principal
├── crear_archivos_prueba.py # Genera archivos de prueba
├── test_api.py              # Verifica conexión con la API
├── log_organizacion.txt     # Log automático de ejecuciones
├── .env                     # API Key (no subir a git)
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.11
- Cuenta activa en [Anthropic](https://console.anthropic.com/) con API Key
- Visual Studio Code

---

## 🚀 Instalación y Uso

### 1. Clonar el repositorio y entrar a la carpeta

```bash
cd proyecto2_agente_organizador
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
```

Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install anthropic
```

### 4. Configurar la API Key

Crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
```

### 5. Crear archivos de prueba (opcional)

```bash
python crear_archivos_prueba.py
```

Esto genera 23 archivos de distintos tipos en la carpeta `desordenada/`.

### 6. Ejecutar el agente

```bash
python organizador.py
```

El agente pedirá la ruta de la carpeta a organizar, mostrará el plan y solicitará confirmación antes de mover los archivos.

---

## 📋 Ejemplo de Salida

```
=======================================================
🐍 AGENTE ORGANIZADOR DE ARCHIVOS CON IA
   Powered by Claude (Anthropic)
=======================================================

📂 Ingresa la ruta de la carpeta a organizar: desordenada

PASO 1: Escaneando carpeta...
📂 Se encontraron 23 archivos en 'desordenada'

PASO 2: Clasificando con Claude...
🤖 Enviando archivos a Claude para clasificación...
✅ Claude clasificó 23 archivos

📋 PLAN DE ORGANIZACIÓN
=======================================================
📁 audio_video/ (3 archivos)
📁 codigo/ (4 archivos)
📁 comprimidos/ (2 archivos)
📁 datos/ (3 archivos)
📁 documentos/ (7 archivos)
📁 imagenes/ (4 archivos)
=======================================================

¿Deseas ejecutar este plan? (s/n): s

PASO 3: Moviendo archivos...
✅ Total movidos: 23

🎉 ¡ORGANIZACIÓN COMPLETADA!
📝 Log guardado en 'log_organizacion.txt'
```

---

## 👥 Integrantes

| Nombre | Rol |
|---|---|
| **Zara Melisa Monroy Vera** | Desarrolladora |
| **Juan David Caviedes Cortes** | Desarrollador |

---

## 🎓 Información Académica

**Programa:** Ingeniería Mecatrónica  
**Asignatura:** Software de Automatización — 2026A  
**Institución:** Corporación Universitaria del Huila — CORHUILA

---

> Proyecto académico desarrollado para la asignatura de Software de Automatización — Ingeniería Mecatrónica, 2026A.

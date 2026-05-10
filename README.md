# Grupo13_Monroy_Caviedes
**Grupo 13 — Software de Automatización | Segundo y Tercer Corte**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![n8n](https://img.shields.io/badge/n8n-Automatización-coral?style=flat-square)
![Claude](https://img.shields.io/badge/Anthropic-Claude_API-purple?style=flat-square)
![Agente IA](https://img.shields.io/badge/Agente-IA-green?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agente-orange?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square)

---

## 📌 Descripción del Proyecto

Este repositorio contiene el desarrollo del **Segundo y Tercer Corte** del proyecto de Software de Automatización, orientado a la integración de **Inteligencia Artificial con flujos de automatización** mediante la API de Anthropic (Claude) y la plataforma n8n, conforme a los lineamientos académicos del programa de Ingeniería Mecatrónica.

---

## 🎯 Alcance del Segundo Corte

### 🤖 Proyecto 1 — Sistema de Soporte Inteligente con IA (n8n + Claude)

Automatización robusta de **10 nodos** que recibe tickets de soporte a través de un webhook y utiliza la API de Claude (Anthropic) para:

- **Clasificar** el tipo de solicitud automáticamente
- **Analizar el sentimiento** del ticket (positivo / neutral / negativo)
- **Generar respuestas personalizadas** adaptadas al contexto del usuario
- **Notificar por Gmail** con la respuesta generada
- **Registrar en Google Sheets** cada ticket procesado con su clasificación

**Tecnologías:** n8n · Claude API (Anthropic) · Gmail API · Google Sheets API · Webhooks

---

### 🐍 Proyecto 2 — Agente Organizador de Archivos con Python y Claude

Desarrollo de un **agente de Inteligencia Artificial** construido en Python que escanea una carpeta desordenada, utiliza la API de Claude (Anthropic) para clasificar los archivos por categoría y los organiza automáticamente en subcarpetas.

El agente implementa una arquitectura de tres capas:

- **Percepción** — escanea el directorio y lista todos los archivos encontrados
- **Razonamiento** — envía los nombres a Claude, que decide la categoría de cada archivo usando lenguaje natural
- **Acción** — crea las subcarpetas y mueve cada archivo a su destino correspondiente

Funcionalidades adicionales:
- Muestra un **plan de organización** con confirmación del usuario antes de actuar
- Genera un **log automático** (`log_organizacion.txt`) con fecha, hora y resumen de cada ejecución
- Manejo de errores y archivos sin extensión

**Tecnologías:** Python 3.11 · Anthropic Claude API · VS Code · `pathlib` · `shutil` · `json`

---

## 🎯 Alcance del Tercer Corte

### 🎯 Proyecto 3 — Generador de Propuestas de Marketing con Multi-Agentes IA

Desarrollo de una **aplicación web multi-agente** construida en Python que orquesta 4 agentes de Inteligencia Artificial especializados usando **LangGraph** y **Claude de Anthropic** para generar propuestas comerciales de marketing profesionales, exportables en PDF y Markdown, visualizado en tiempo real con **Streamlit**.

El sistema implementa un pipeline de 4 agentes en cadena que comparten un estado común (`MarketingProposalState`):

- 🔍 **Agente 1: Analista** — Analiza el mercado usando el framework PEST + Pain-Gain-Fear
- 🏛️ **Agente 2: Estratega** — Define posicionamiento y mensajes clave con el Messaging Hierarchy Canvas
- ✍️ **Agente 3: Redactor** — Redacta la propuesta completa (11 secciones, +850 palabras) con el framework StoryBrand
- ✅ **Agente 4: Editor** — Revisa y pule el documento aplicando el PACT Rubric (Personalización, Acción, Claridad, Tono)

Funcionalidades adicionales:
- Interfaz web interactiva con **barra de progreso en tiempo real** por cada agente
- **Exportación en Markdown y PDF** con estilos corporativos (ReportLab)
- API Key cargada de forma segura desde archivo `.env`
- Visualización formateada, texto plano editable y descarga directa

**Tecnologías:** Python 3.11 · LangGraph · LangChain · Claude Haiku (Anthropic) · Streamlit · ReportLab · python-dotenv

---

## 👥 Integrantes

| Nombre | Rol |
|---|---|
| **Zara Melisa Monroy Vera** | Desarrolladora |
| **Juan David Caviedes Cortes** | Desarrollador |

---

## 🎓 Programa Académico

**Ingeniería Mecatrónica**  
Asignatura: Software de Automatización — 2026A

---

## 🗂️ Estructura del Repositorio

```
Grupo13_Monroy_Caviedes/
├── proyecto1_soporte_ia/
│   ├── workflow_n8n.json        # Flujo exportado de n8n (10 nodos)
│   └── README.md
├── proyecto2_agente_organizador/
│   ├── organizador.py           # Agente principal
│   ├── crear_archivos_prueba.py # Script de archivos de prueba
│   ├── test_api.py              # Verificación de conexión API
│   ├── .env                     # API Key (no incluir en git)
│   └── README.md
├── proyecto3_agente_marketing/
│   ├── app.py                   # Aplicación principal (agentes + grafo + UI)
│   ├── requirements.txt         # Dependencias Python
│   ├── .env                     # API Key (no incluir en git)
│   └── README.md
└── README.md
```

---

## ⚙️ Requisitos

- [n8n](https://n8n.io/) (self-hosted o cloud)
- Cuenta en [Anthropic](https://console.anthropic.com/) con API Key activa
- Python 3.11 con entorno virtual (`venv`)
- Credenciales de Gmail y Google Sheets (para Proyecto 1)

---

## 🚀 Instrucciones de Uso

### Proyecto 1
1. Importar `workflow_n8n.json` en tu instancia de n8n
2. Configurar las credenciales de Gmail, Google Sheets y la API Key de Claude
3. Activar el workflow y enviar un ticket de prueba al webhook

### Proyecto 2
1. Crear y activar el entorno virtual:
   ```
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Instalar dependencias:
   ```
   pip install anthropic
   ```
3. Configurar la API Key en el archivo `.env`:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```
4. Crear archivos de prueba:
   ```
   python crear_archivos_prueba.py
   ```
5. Ejecutar el agente:
   ```
   python organizador.py
   ```
6. Ingresar la ruta de la carpeta a organizar y confirmar el plan

### Proyecto 3
1. Crear y activar el entorno virtual:
   ```
   python -m venv venv
   .\venv\Scripts\activate.bat
   ```
2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Configurar la API Key en el archivo `.env`:
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```
4. Ejecutar la aplicación:
   ```
   streamlit run app.py
   ```
5. Completar el formulario con los datos del cliente y hacer clic en **Generar Propuesta**

---

> Proyecto académico desarrollado para la asignatura de Software de Automatización — Ingeniería Mecatrónica, 2026A.

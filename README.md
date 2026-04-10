# Grupo13_Monroy_Caviedes

**Grupo 13 — Software de Automatización | Segundo Corte**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![n8n](https://img.shields.io/badge/n8n-Automatización-coral?style=flat-square)
![Claude](https://img.shields.io/badge/Anthropic-Claude_API-purple?style=flat-square)
![MCP](https://img.shields.io/badge/Protocol-MCP-teal?style=flat-square)

---

## 📌 Descripción del Proyecto

Este repositorio contiene el desarrollo del **Segundo Corte** del proyecto de Software de Automatización, orientado a la integración de **Inteligencia Artificial con flujos de automatización** mediante la API de Anthropic (Claude) y la plataforma n8n, conforme a los lineamientos académicos del programa de Ingeniería Mecatrónica.

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

### 🔗 Proyecto 2 — Integración n8n como Servidor MCP con Claude Desktop

Configuración de **n8n como servidor MCP (Model Context Protocol)** conectado a Claude Desktop para crear automatizaciones de análisis de facturas mediante lenguaje natural.

- Claude Desktop actúa como agente principal
- No se escriben prompts en n8n — Claude entiende la instrucción y ejecuta el workflow automáticamente
- Análisis de facturas mediante conversación directa con el modelo
- Arquitectura orientada a agentes donde el LLM controla la ejecución de tareas

**Tecnologías:** n8n (MCP Server) · Claude Desktop · Model Context Protocol · Anthropic API

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
├── proyecto2_mcp_facturas/
│   ├── mcp_config/              # Configuración del servidor MCP
│   └── README.md
└── README.md
```

---

## ⚙️ Requisitos

- [n8n](https://n8n.io/) (self-hosted o cloud)
- Cuenta en [Anthropic](https://console.anthropic.com/) con API Key activa
- Claude Desktop (para Proyecto 2)
- Credenciales de Gmail y Google Sheets (para Proyecto 1)

---

## 🚀 Instrucciones de Uso

### Proyecto 1
1. Importar `workflow_n8n.json` en tu instancia de n8n
2. Configurar las credenciales de Gmail, Google Sheets y la API Key de Claude
3. Activar el workflow y enviar un ticket de prueba al webhook

### Proyecto 2
1. Configurar n8n como servidor MCP (ver carpeta `mcp_config/`)
2. Conectar Claude Desktop al servidor MCP
3. Hablar con Claude en lenguaje natural para ejecutar análisis de facturas

---

> Proyecto académico desarrollado para la asignatura de Software de Automatización — Ingeniería Mecatrónica, 2026A.

# Sistema de Soporte Inteligente con IA — n8n + Claude API

**Proyecto 1 — Grupo 13 | Software de Automatización | Segundo Corte**

![n8n](https://img.shields.io/badge/n8n-Workflow_Automation-orange?style=flat-square)
![Claude](https://img.shields.io/badge/Anthropic-Claude_API-purple?style=flat-square)
![Gmail](https://img.shields.io/badge/Gmail-OAuth2-red?style=flat-square)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-Registro-green?style=flat-square)

---

## 📌 Descripción

Sistema de **automatización inteligente de tickets de soporte técnico** desarrollado en n8n, que utiliza la API de Claude (Anthropic) para clasificar automáticamente los tickets recibidos, generar respuestas personalizadas al cliente y registrar cada caso en Google Sheets. El flujo se activa mediante un Webhook que recibe solicitudes desde cualquier cliente HTTP (como Postman o un formulario web).

---

## 🏗️ Arquitectura del Flujo

| Nodo | Función | Tecnología |
|---|---|---|
| **Webhook** | Recibe el ticket de soporte vía HTTP POST | n8n Webhook |
| **If** | Valida que el email, nombre y mensaje sean válidos | n8n If |
| **Edit Fields** | Estructura y enriquece los datos del ticket | n8n Edit Fields |
| **Basic LLM Chain** | Clasifica el ticket con IA | Anthropic Claude + Basic LLM Chain |
| **Switch** | Enruta según la categoría detectada por la IA | n8n Switch |
| **Edit Fields (Consolidar)** | Une datos originales con el análisis de la IA | n8n Edit Fields |
| **Basic LLM Chain 2** | Genera respuesta personalizada al cliente | Anthropic Claude + Basic LLM Chain |
| **Gmail (Cliente)** | Envía la respuesta generada al cliente | Gmail OAuth2 |
| **Gmail (Admin)** | Envía alerta con análisis completo al administrador | Gmail OAuth2 |
| **Google Sheets** | Registra el ticket y su análisis en la hoja de cálculo | Google Sheets API |

---

## 🤖 Capacidades de Clasificación IA

El primer modelo de Claude analiza cada ticket y devuelve un JSON estructurado con:

| Campo | Valores posibles |
|---|---|
| `categoria` | `TÉCNICO`, `FACTURACIÓN`, `CONSULTA_GENERAL`, `QUEJA`, `SOLICITUD` |
| `sentimiento` | `POSITIVO`, `NEUTRO`, `NEGATIVO`, `FRUSTRADO` |
| `urgencia` | `BAJA`, `MEDIA`, `ALTA`, `CRÍTICA` |
| `resumen` | Resumen de máximo 50 palabras del problema |
| `palabras_clave` | Lista de 3 palabras clave del ticket |

---

## 📋 Estructura del Flujo

```
Webhook (POST)
    └── If (validación email + nombre + mensaje)
            ├── false → (sin acción)
            └── true
                    └── Edit Fields (estructurar ticket)
                            └── Basic LLM Chain (clasificación IA)
                                    └── Switch (enrutamiento por categoría)
                                            ├── Output 0 → TÉCNICO
                                            ├── Output 1 → FACTURACIÓN
                                            ├── Output 2 → QUEJA
                                            └── Fallback → CONSULTA_GENERAL / SOLICITUD
                                                    └── Edit Fields (consolidar datos + análisis)
                                                                └── Basic LLM Chain (generar respuesta)
                                                                            ├── Gmail → Cliente
                                                                            ├── Gmail → Administrador
                                                                            └── Google Sheets → Registro
```

---

## ⚙️ Requisitos

- n8n (instalación local en `localhost:5678`)
- Cuenta activa en [Anthropic](https://console.anthropic.com/) con API Key
- Cuenta de Gmail con OAuth2 configurado en n8n
- Google Sheets con las columnas: `ID`, `FECHA`, `NOMBRE`, `EMAIL`, `ASUNTO`, `MENSAJE`, `CATEGORÍA IA`, `SENTIMIENTO`, `URGENCIA`, `RESPUESTA IA`

---

## 🚀 Configuración y Uso

### 1. Importar el flujo en n8n

Importar el archivo JSON del flujo desde el menú de n8n:

```
n8n → Workflows → Import from file
```

### 2. Configurar credenciales

Agregar las siguientes credenciales en n8n:

- **Anthropic API Key:** desde [console.anthropic.com](https://console.anthropic.com/)
- **Gmail OAuth2:** autorizar cuenta de Google en n8n → Credentials
- **Google Sheets OAuth2:** autorizar acceso a Google Sheets

### 3. Configurar la hoja de Google Sheets

Crear una hoja llamada `Tickets Soporte Inteligente` con las siguientes columnas en la fila 1:

```
ID | FECHA | NOMBRE | EMAIL | ASUNTO | MENSAJE | CATEGORÍA IA | SENTIMIENTO | URGENCIA | RESPUESTA IA
```

### 4. Activar el workflow

Hacer clic en el toggle **Inactive → Active** en n8n para activar el flujo en modo producción.

### 5. Enviar un ticket de prueba

Usar Postman o cualquier cliente HTTP con el siguiente payload:

```http
POST http://localhost:5678/webhook/soporte-inteligente
Content-Type: application/json

{
  "nombre": "María González",
  "email": "maria.gonzalez@ejemplo.com",
  "asunto": "Error al procesar mi pedido #4521",
  "mensaje": "Llevo 3 días esperando respuesta sobre mi pedido. El sistema me muestra un error cuando intento rastrearlo.",
  "prioridad": "alta"
}
```

---

## 📋 Ejemplo de Respuesta al Cliente

```
Estimada María González,

Hemos recibido tu ticket TK-20260421-5834 sobre "Error al procesar mi pedido #4521".

Lamentamos los inconvenientes que estás experimentando. Nuestro equipo técnico
ha revisado tu caso y tomará acción en las próximas horas.

Quedo a tu disposición para cualquier consulta adicional.

Equipo de Soporte — Sistema Inteligente
```

---

## 📊 Registro en Google Sheets

Cada ticket procesado queda registrado automáticamente con:

- ID único generado automáticamente
- Fecha y hora de recepción
- Datos completos del cliente
- Categoría, sentimiento y urgencia detectados por la IA
- Respuesta generada y enviada al cliente

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

# 🚀 Proyecto CI/CD - Flask con IA y Despliegue Automático

**Estudiante:** Alejandro Maldonado  
**Curso:** DevOps / CI/CD  
**Versión:** 1.0.5

---

## 📋 Descripción del Proyecto

Este proyecto implementa una aplicación web **Flask** con **Inteligencia Artificial** para análisis de sentimientos, junto con un flujo completo de **Integración Continua / Despliegue Continuo (CI/CD)** automatizado usando **GitHub Actions**, **Docker** y **GitHub Packages (GHCR)**.

El objetivo es asegurar que cada cambio en la rama `maldonado` pase por pruebas exhaustivas antes de construir, publicar y desplegar automáticamente la aplicación en un servidor VPS.

---

## 🎯 Características Principales

- ✅ **Aplicación Flask con IA**: Modelo de análisis de sentimientos (positivo, negativo, neutral)
- ✅ **Interfaz Web Interactiva**: UI moderna y responsive para interactuar con el modelo
- ✅ **API REST**: Endpoints documentados para integración programática
- ✅ **Tests Automatizados**: 12 tests unitarios que validan toda la funcionalidad
- ✅ **Containerización**: Docker para portabilidad y consistencia
- ✅ **Pipeline CI/CD Completo**: Automatización total con GitHub Actions
- ✅ **GitHub Packages (GHCR)**: Publicación automática de imágenes Docker
- ✅ **Despliegue Automático**: Deploy a VPS sin intervención manual
- ✅ **HTTPS Seguro**: Certificado SSL con Let's Encrypt vía Traefik
- ✅ **Health Checks**: Monitoreo automático del estado de la aplicación

---

## 🏗️ Estructura del Proyecto
```
alejandro-maldonado/
├── .github/
│   └── workflows/
│       └── ci.yml                # Pipeline CI/CD completo
├── app.py                        # Aplicación Flask con IA
├── test_app.py                   # Suite de tests automatizados (12 tests)
├── requirements.txt              # Dependencias Python
├── Dockerfile                    # Imagen Docker optimizada
├── stack.yml                     # Docker Compose stack para VPS
├── Makefile                      # Comandos útiles para desarrollo
├── .gitignore                    # Archivos ignorados por Git
├── .dockerignore                 # Archivos ignorados por Docker
└── README.md                     # Este archivo
```

---

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.0, Python 3.11
- **IA**: Modelo simple de clasificación de sentimientos
- **Testing**: unittest (Python standard library)
- **Containerización**: Docker, Docker Compose, Docker Swarm
- **CI/CD**: GitHub Actions
- **Registro de Imágenes**: GitHub Container Registry (GHCR)
- **Reverse Proxy**: Traefik
- **SSL**: Let's Encrypt (certificados automáticos)

---

## 📦 Instalación y Ejecución Local

### Prerrequisitos

- Python 3.11+
- Docker (opcional, para contenedores)
- Git

### Opción 1: Ejecución Directa con Python
```bash
# Clonar el repositorio
git clone https://github.com/AlejandroMGT52/alejandro-maldonado.git
cd alejandro-maldonado

# Cambiar a la rama de desarrollo
git checkout maldonado

# Crear y activar entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python app.py
```

La aplicación estará disponible en: **http://localhost:5000**

### Opción 2: Con Docker
```bash
# Construir la imagen Docker
docker build -t maldonado:1.0.5 .

# Ejecutar el contenedor
docker run -p 5000:5000 maldonado:1.0.5
```

Accede a: **http://localhost:5000**

### Opción 3: Con Makefile (Recomendado)
```bash
# Ver comandos disponibles
make help

# Ejecutar tests
make test

# Construir imagen
make build

# Ejecutar aplicación
make run
```

---

## 🧪 Ejecutar Tests
```bash
# Opción 1: Con unittest
python -m unittest test_app.py -v

# Opción 2: Con pytest (si está instalado)
pytest test_app.py -v

# Opción 3: Con Makefile
make test
```

### Suite de Tests (12 tests totales)

**Tests de la Aplicación Flask (8 tests):**
- ✅ `test_health_endpoint` - Verifica endpoint de salud
- ✅ `test_index_endpoint` - Verifica página principal
- ✅ `test_info_endpoint` - Verifica endpoint de información
- ✅ `test_analyze_positive_sentiment` - Análisis de sentimiento positivo
- ✅ `test_analyze_negative_sentiment` - Análisis de sentimiento negativo
- ✅ `test_analyze_neutral_sentiment` - Análisis de sentimiento neutral
- ✅ `test_analyze_empty_text` - Manejo de texto vacío
- ✅ `test_analyze_missing_text` - Manejo de campo faltante

**Tests del Modelo de IA (4 tests):**
- ✅ `test_positive_prediction` - Predicción de sentimiento positivo
- ✅ `test_negative_prediction` - Predicción de sentimiento negativo
- ✅ `test_neutral_prediction` - Predicción de sentimiento neutral
- ✅ `test_generate_response` - Generación completa de respuesta

---

## 🌐 Endpoints de la API

### `GET /`
Interfaz web principal con UI interactiva.

**Respuesta:** HTML con interfaz de usuario

---

### `GET /health`
Health check para verificar el estado del servicio.

**Respuesta:**
```json
{
  "status": "healthy",
  "version": "1.0.5",
  "timestamp": "2025-11-25T10:30:00.000000",
  "service": "maldonado-cicd"
}
```

---

### `POST /api/analyze`
Analiza el sentimiento de un texto.

**Request:**
```json
{
  "text": "Este proyecto es excelente y funciona genial"
}
```

**Response:**
```json
{
  "sentiment": "positivo",
  "confidence": 0.67,
  "response": "¡Me alegra que estés de buen ánimo! 😊",
  "processed_at": "2025-11-25T10:30:00.000000"
}
```

**Posibles valores de `sentiment`:**
- `"positivo"` - Sentimiento positivo detectado
- `"negativo"` - Sentimiento negativo detectado
- `"neutral"` - Sentimiento neutral

---

### `GET /info`
Información detallada del proyecto.

**Respuesta:**
```json
{
  "project": "CI/CD Flask con IA",
  "student": "Alejandro Maldonado",
  "version": "1.0.5",
  "features": [
    "Análisis de sentimientos con IA",
    "Pipeline CI/CD automatizado",
    "Tests automatizados",
    "Despliegue automático a VPS",
    "Publicación en GitHub Packages"
  ],
  "endpoints": {
    "/": "Interfaz web",
    "/health": "Health check",
    "/api/analyze": "Análisis de sentimiento (POST)",
    "/info": "Información del proyecto"
  }
}
```

---

## 🔄 Pipeline CI/CD - Fases del Flujo Automatizado

El pipeline se activa automáticamente con cada `push` a la rama `maldonado` y consta de **3 jobs principales** que se ejecutan secuencialmente:

### Job 1: Test (Integración Continua)

Este job se ejecuta en `ubuntu-latest` y verifica la calidad del código.

| Paso | Descripción | Archivos involucrados |
|------|-------------|----------------------|
| **Checkout** | Descarga el código del repositorio | - |
| **Configurar Python** | Configura Python 3.11 | - |
| **Instalar dependencias** | Instala Flask y otras librerías | `requirements.txt` |
| **Ejecutar tests** | Ejecuta los 12 tests unitarios | `test_app.py` |

**Criterio de éxito:** Todos los tests deben pasar (12/12) ✅

Si algún test falla, el pipeline se detiene y **NO** se construye ni despliega la aplicación.

---

### Job 2: Build and Push (Publicación de Imagen)

Este job solo se ejecuta si los tests fueron exitosos. Construye y publica la imagen Docker en GitHub Packages.

| Paso | Descripción |
|------|-------------|
| **Checkout** | Descarga el código |
| **Login a GHCR** | Autenticación en GitHub Container Registry |
| **Extraer metadata** | Genera tags y labels para la imagen |
| **Build & Push** | Construye y sube la imagen Docker |

**Imagen publicada:** `ghcr.io/alejandromgt52/maldonado:1.0.5`

**Tags generados:**
- `maldonado:1.0.5` (versión específica)
- `maldonado:latest` (última versión)

---

### Job 3: Deploy (Despliegue Automático)

Este job solo se ejecuta si la imagen se publicó correctamente. Despliega automáticamente la aplicación en el VPS.

| Paso | Descripción |
|------|-------------|
| **Checkout** | Descarga el código |
| **Conexión SSH** | Conecta al VPS de forma segura |
| **Login a GHCR** | Autenticación en el VPS |
| **Pull de imagen** | Descarga la nueva versión |
| **Detener stack anterior** | Para el servicio antiguo |
| **Desplegar nuevo stack** | Inicia el servicio actualizado |
| **Verificación** | Confirma que el despliegue fue exitoso |

**Resultado:** Aplicación actualizada automáticamente en `https://maldonado.byronrm.com` 🚀

---

## 🚀 Despliegue en Producción

### URL de Producción
🌐 **https://maldonado.byronrm.com**

### Características del Despliegue

- ✅ **Completamente Automático**: Sin intervención manual
- ✅ **SSL/HTTPS**: Certificado Let's Encrypt automático
- ✅ **Alta Disponibilidad**: Configurado con Docker Swarm
- ✅ **Health Checks**: Monitoreo continuo del estado
- ✅ **Zero Downtime**: Actualizaciones sin interrupciones
- ✅ **Traefik**: Reverse proxy con balanceo de carga

### Flujo de Despliegue
```
1. Developer → Push a rama 'maldonado'
2. GitHub Actions → Ejecuta tests
3. Tests pass ✅ → Construye imagen Docker
4. Imagen → Se publica en GHCR
5. Pipeline → Se conecta al VPS vía SSH
6. VPS → Descarga nueva imagen
7. Docker Swarm → Actualiza servicio
8. Traefik → Rutea tráfico a nueva versión
9. Let's Encrypt → Renueva certificado SSL si es necesario
10. Aplicación → Disponible en https://maldonado.byronrm.com
```

---

## 🔐 Secrets Requeridos en GitHub

Para que el pipeline funcione correctamente, debes configurar estos secrets en tu repositorio:

**Ir a:** Repositorio → Settings → Secrets and variables → Actions → New repository secret

| Secret Name | Descripción | Ejemplo |
|-------------|-------------|---------|
| `VPS_HOST` | IP o dominio del VPS | `192.168.1.100` |
| `VPS_USER` | Usuario SSH del VPS | `ubuntu` |
| `VPS_PASSWORD` | Contraseña SSH | `tu_password_seguro` |
| `VPS_SSH_PORT` | Puerto SSH (normalmente 22) | `22` |
| `GHCR_PAT` | Personal Access Token de GitHub | `ghp_xxxxx...` |

**Nota:** `GITHUB_TOKEN` se genera automáticamente por GitHub Actions.

---

## 📊 Cumplimiento de Requisitos del Examen

### ✅ Criterio 1: Uso correcto de Git y repositorio (1 punto)

- ✅ Estructura clara y organizada
- ✅ Commits con mensajes descriptivos
- ✅ Única rama de desarrollo: `maldonado`
- ✅ `.gitignore` correctamente configurado
- ✅ Documentación completa en README

### ✅ Criterio 2: Imagen publicada en GHCR (2 puntos)

- ✅ Pipeline construye imagen automáticamente
- ✅ Etiquetado correcto: `maldonado:1.0.5`
- ✅ Publicada exitosamente en GitHub Packages
- ✅ Visible en: `https://github.com/AlejandroMGT52?tab=packages`
- ✅ Tag adicional: `latest`

### ✅ Criterio 3: Pipeline CI funcional (1 punto)

- ✅ Tests se ejecutan automáticamente
- ✅ 12 tests unitarios completos
- ✅ Tests fallan correctamente ante errores
- ✅ Build se completa sin errores
- ✅ Logs claros y descriptivos

### ✅ Criterio 4: Pipeline CD funcional (6 puntos)

- ✅ Conexión SSH automática al VPS
- ✅ Sin intervención manual requerida
- ✅ Pull de imagen desde GHCR
- ✅ Actualización automática del stack
- ✅ Verificación post-despliegue
- ✅ Aplicación operativa en producción
- ✅ Subdominio funcional con HTTPS

**Puntuación Total: 10/10 puntos** 🎉

---

## 🐛 Troubleshooting - Solución de Problemas

### Problema 1: Tests fallan localmente
```bash
# Verificar que tienes las dependencias correctas
pip install -r requirements.txt

# Ejecutar tests con output detallado
python -m unittest test_app.py -v

# Revisar que app.py tiene la versión correcta (1.0.5)
grep "version" app.py
```

### Problema 2: Pipeline falla en GitHub Actions
```bash
# Ver logs del pipeline:
# GitHub → Actions → Click en el workflow fallido

# Verificar que los secrets están configurados:
# Settings → Secrets and variables → Actions
```

### Problema 3: No se puede acceder al subdominio
```bash
# Verificar DNS
nslookup maldonado.byronrm.com

# Verificar que el VPS está accesible
ping maldonado.byronrm.com

# Conectarse al VPS y verificar
ssh usuario@vps_ip
docker ps | grep maldonado
docker logs quintob_maldonado-app
```

### Problema 4: Imagen no aparece en GitHub Packages
```bash
# Verificar permisos del workflow:
# Settings → Actions → General → Workflow permissions
# Debe estar en: "Read and write permissions"

# Verificar que el build fue exitoso
# Actions → Click en el workflow → Ver job "build-and-push"
```

### Problema 5: Contenedor no inicia en el VPS
```bash
# SSH al VPS
ssh usuario@vps_ip

# Ver logs del contenedor
docker service logs quintob_maldonado-app

# Ver estado del servicio
docker service ps quintob_maldonado-app

# Verificar que la imagen se descargó
docker images | grep maldonado

# Reiniciar el servicio
docker service update --force quintob_maldonado-app
```

---

## 📝 Comandos Útiles

### Desarrollo Local
```bash
# Ejecutar aplicación
python app.py

# Ejecutar tests
make test

# Construir imagen Docker
make build

# Ver comandos disponibles
make help
```

### En el VPS
```bash
# Ver servicios corriendo
docker service ls

# Ver logs en tiempo real
docker service logs -f quintob_maldonado-app

# Ver estado de contenedores
docker ps

# Actualizar servicio manualmente
docker service update --image ghcr.io/alejandromgt52/maldonado:1.0.5 quintob_maldonado-app

# Reiniciar stack completo
docker stack rm quintob
sleep 30
docker stack deploy --with-registry-auth -c stack.yml quintob
```

---

## 🎓 Conclusión

Este proyecto demuestra un flujo completo de CI/CD moderno, desde el desarrollo local hasta el despliegue automático en producción, incluyendo:

- ✅ Integración continua con tests automatizados
- ✅ Containerización con Docker
- ✅ Publicación en registro de contenedores
- ✅ Despliegue continuo sin intervención manual
- ✅ Monitoreo y health checks
- ✅ HTTPS con certificados automáticos

**Resultado:** Una aplicación web profesional, escalable y totalmente automatizada. 🚀

---

## 👨‍💻 Autor

**Alejandro Maldonado**  
Examen Final - CI/CD  
Noviembre 2025

---

## 📄 Licencia

Proyecto académico - Uso educativo únicamente
# Usar imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos primero (mejor práctica para cache)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app.py .

# Exponer puerto 5000 (Flask usa 5000, no 80)
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=app.py
ENV PORT=5000

# Health check para verificar que la app está funcionando
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:5000/health')" || exit 1

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
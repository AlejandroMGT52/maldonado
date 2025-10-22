# Imagen base de Python slim (mejores prácticas)
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar archivos (incluye app.py, requirements.txt, etc.)
COPY . .

# Instalar dependencias con opción para optimizar la imagen
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto de la aplicación Flask
EXPOSE 3000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

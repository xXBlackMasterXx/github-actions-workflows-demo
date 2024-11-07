FROM python:3.12-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

EXPOSE 8000

# Ejecutar la aplicación
CMD ["fastapi", "run", "main.py"]
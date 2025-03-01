FROM python:3.11-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias del sistema
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Copiar el archivo de requisitos
COPY requirements.txt /requirements.txt

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r /requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . /app

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar cuando se inicie el contenedor
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

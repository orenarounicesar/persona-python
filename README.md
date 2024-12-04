# Backend Python con FastAPI

Este es un backend desarrollado con **FastAPI** para gestionar una base de datos PostgreSQL. Está diseñado para ejecutarse dentro de un contenedor Docker.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuración del Proyecto

### Variables de Entorno

El proyecto utiliza variables de entorno para la configuración de la base de datos.
Puedes configurarlas de dos maneras:

1. **Usando un archivo `.env`** (recomendado):
   
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```env
   DB_HOST=postgresql  #nombre del host o direccion ip
   DB_PORT=5432     #puerto en el que PostgreSQL escucha conexiones
   DB_USER=root     #nombre de usuario que se utilizará para autenticar la conexión
   DB_PASSWORD=root    #contraseña del usuario especificado en DB_USER
   DB_NAME=personas    #nombre de la base de datos a la que tu aplicación se conectará
   ```
   
   En el archivo de docker-compose debe estar principalmente esta manera
   Recuerda que aqui debes tener tambien tu base de datos
    ```
    service:
      python-backend:
      build:
        context: ./persona-python/api
        dockerfile: dockerfile
      container_name: python
      environment:
        - DB_HOST=${DB_HOST}
        - DB_PORT=${DB_PORT}
        - DB_USER=${DB_USER}
        - DB_PASSWORD=${DB_PASSWORD}
        - DB_NAME=${DB_NAME}
      ports:
        - "8001:8001"
      networks:
      - nombre_de_tu_red
      depends_on:
      - postgresql
      ```
    Ejecuta el siguiente comando para construir y levantar los contenedores:
    ```
    docker-compose up --build

  2. **Pasándolas directamente al contenedor**
     
     Para este paso es importante que tengas tus base de datos creada previamente y esten en una misma red
     
     Debes estar primero ubicado en la carpeta ../persona-python/api y construir la imagen
     ```
     docker build -t python .
     ```
     Y ya puedes pasar las variables al contenedor con el comando docker run:
     ```
     docker run --name python-backend --network nombre_de_tu_red -p 8001:8001 \
      -e DB_HOST=postgresql \
      -e DB_PORT=5432 \
      -e DB_USER=root \
      -e DB_PASSWORD=root \
      -e DB_NAME=personas \
      python

   3. **Verificacion**
      
      Puedes verificar las apis del backend de python
      
          localhost:8001/docs

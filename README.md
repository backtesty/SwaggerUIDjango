# SwaggerUI Django
Vamos agregar Swagger UI o documentación automática a las APIs de Django Rest Framework.

<!-- ABOUT THE PROJECT -->
## Acerca del proyecto

Este proyecto que implementa la generación de documentación automática de las APIs de Django Rest Framework, utilizando Swagger UI. Swagger UI es una herramienta que permite visualizar y probar las APIs de una forma sencilla y amigable.

## Tutorial
* Vídeo tutorial de Youtube <a href="https://youtu.be/uSo-7zt9L5w">https://youtu.be/uSo-7zt9L5w</a>
 
<!-- GETTING STARTED -->
## Tecnologías

* Python
* Django
* Django Rest Framework
* Swagger UI

### Prerequisitos

Debe tener instalado Python en su computadora. Puede descargarlo desde el siguiente enlace: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>

* Clonar el repositorio
  ```sh
  git clone https://github.com/backtesty/SwaggerUIDjango.git
  ```

* Crear el entorno virtual
  ```sh
  python -m venv env
  ```
* Activar entorno virtual (windows):
  ```sh
  env\Scripts\activate
  ```
* Instalar las dependencias del proyecto:
  ```sh
  pip install -r requirements.txt
  ```
* Migrar la base de datos:
  ```sh
  python manage.py migrate
  ```
* Crear un superusuario:
  ```sh
  python manage.py createsuperuser
  ```
* Ejecutar el servidor:
  ```sh
  python manage.py runserver 5000
  ```
## Acceder a la documentación
Ingresa en el navegador a la siguiente dirección: <a href="http://localhost:5000/docs/">http://localhost:5000/docs/</a>

## Finalmente

Agradezco tu visita, no olvides seguirme y darle me gusta si te sirvió el vídeo, más información en mi canal de <a href="https://www.youtube.com/channel/UCxGqlLmQXjFjkrnSRLa7B7g">YouTube</a>.
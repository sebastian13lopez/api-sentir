# API REST de SENTIR

Proyecto de API REST construido con **FastAPI** y **PostgreSQL** para la gestión de reportes de emergencias, administración de personas y sus ubicaciones.

## Tecnologías Utilizadas
* Python 3
* FastAPI
* PostgreSQL
* psycopg2
* Uvicorn

## Endpoints Principales
* **Personas:** `GET, POST, PUT, DELETE /personas`
* **Emergencias:** `GET, POST, PUT, DELETE /emergencias`
* **Ubicaciones:** `GET, POST, PUT, DELETE /ubicaciones`
* **Integración:** 
  * `GET /emergencias/{id}/ubicacion`
  * `GET /emergencias/{id}/detalle` 

  
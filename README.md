# Docker Projects

Este repositorio contiene mis **proyectos y experimentos con Docker**. 
Cada carpeta representa un proyecto independiente con su propio 
`Dockerfile`, `docker-compose.yml` y demás archivos relacionados.

---

## Contenido

- `Proyecto1/` – Descripción breve del primer proyecto
- `Proyecto2/` – Descripción breve del segundo proyecto
- `ProyectoX/` – Otros experimentos con Docker

> Cada proyecto tiene instrucciones propias para levantar contenedores y 
probar la aplicación.

---

## Recomendaciones

1. **Instalar Docker**: Asegúrate de tener Docker instalado en tu máquina.  
   [Docker Installation](https://docs.docker.com/get-docker/)

2. **Docker Compose**: Algunos proyectos usan Docker Compose para levantar 
múltiples contenedores.  
   [Docker Compose Installation](https://docs.docker.com/compose/install/)

3. **Variables de entorno**: Cada proyecto puede tener un archivo `.env` 
que no está en el repositorio por seguridad.  
   Crea tu propio `.env` siguiendo el ejemplo `.env.example` si existe.

---

## Cómo usar

```bash
# Entrar a la carpeta de un proyecto
cd Proyecto1

# Construir la imagen
docker build -t proyecto1 .

# Levantar con Docker Compose (si aplica)
docker-compose up -d

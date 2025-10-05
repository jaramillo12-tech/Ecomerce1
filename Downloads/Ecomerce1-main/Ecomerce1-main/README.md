# TechStore (Reflex)

Proyecto de e-commerce construido con Reflex (Python). Este README incluye pasos para desarrollo local y despliegue en GitHub Pages.

## Requisitos

- Python 3.11
- Node.js 18
- `pip` y `reflex` (incluido en `requirements.txt`)

## Desarrollo

1. Instala dependencias:
   - `pip install -r requirements.txt`
2. Ejecuta en local:
   - `reflex run`

## Despliegue en GitHub Pages

Este proyecto puede exportar un frontend estático ideal para GitHub Pages.

Pasos:
- Crea un repositorio en GitHub y sube este proyecto (rama `main`).
- En Ajustes del repositorio → Secrets and variables → Actions, agrega el secreto `BACKEND_API_URL` si necesitas que el frontend se conecte a un backend público en producción. Si es solo demo estática, puedes omitirlo.
- El workflow incluido en `.github/workflows/deploy-pages.yml` hará lo siguiente:
  - Instalará Python y Node.
  - Construirá el frontend con `reflex export`.
  - Descomprimirá `frontend.zip` a `dist/` y añadirá `.nojekyll`.
  - Publicará `dist/` en GitHub Pages.

Configuración de GitHub Pages:
- En Settings → Pages, establece `Source: GitHub Actions`.
- Tras ejecutar el workflow, tu sitio estará disponible en `https://<usuario>.github.io/<repo>/`.

Notas importantes:
- Rutas bajo subpath: si no tienes dominio personalizado, GitHub Pages publica bajo `/<repo>`. Evita rutas absolutas con `/` para assets si notas que no cargan. En este proyecto se enlaza `/animations.css`; en Pages normalmente funciona desde la raíz del repo. Si no, cambia a `animations.css` (ruta relativa) o usa CDN.
- API_URL: para hosting estático, el frontend llamará a la URL definida por `API_URL`. Ajusta el secreto `BACKEND_API_URL` para que apunte a una URL pública accesible.
- Backend: `reflex export` también genera `backend.zip`. GitHub Pages solo sirve el frontend; si necesitas backend, despliega `backend.zip` en un servidor (Railway, Render, Fly.io, etc.) y usa su URL como `API_URL`.

## Exportación manual

- Ejecuta `reflex export`.
- Sube el contenido de `frontend.zip` (descomprimido) a cualquier hosting estático.
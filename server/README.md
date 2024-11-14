# RAG-LANGCHAIN Server

## Requisitos 
- Python 3.x: Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- pip: El gestor de paquetes de Python. Generalmente se instala automáticamente con Python 3.

## Configuración del Entorno Virtual

Se recomienda usar entornos virtuales para evitar conflictos entre las dependencias de diferentes proyectos. Sigue estos pasos para crear y activar un entorno virtual:

```bash
# Instalar la herramienta virtualenv si no está instalada
pip install virtualenv

# Crear un nuevo entorno virtual
virtualenv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate
# o (Linux/macOS)
source venv/bin/activate
```

## Instalación de Dependencias
Para instalar las librerías necesarias, ejecuta el siguiente comando después de activar tu entorno virtual:
```bash
pip install -r requirements.txt
```

## Setea las variables de entorno
```bash
cp .env.example .env
```

En el archivo .env agrega el modelo a usar y el nombre del archivo.


## Agrega un archivo pdf en la carpeta docs

Deberá ser un archivo pdf con el texto que se desea analizar en el proyecto

## Correr el servidor

Ejecute el siguiente comando para levantar el servidor:
```bash
uvicorn main:app --reload
```

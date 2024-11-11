# Pasos para el inicio del proyecto

## 1. Clonar el repositorio
```bash
git clone https://github.com/devyan18/RAG-LANGCHAIN.git
```

## 2. Iniciar docker compose
```bash
docker-compose up -d
```

## 3. Crear entorno virtual
```bash
python -m venv venv
```
o
```bash
python3 -m venv venv
```

## 4. Activar entorno virtual
```bash
source venv/bin/activate
```

## 5. Instalar dependencias
```bash
pip install langchain langchain_chroma langchain_core langchain_ollama langchain_community langchain_text_splitters python-dotenv chromadb PyPDF2
```

## 6. Setear variables de entorno
```bash
cp .env.example .env
```
Luego editar el archivo .env con las credenciales de la base de datos

## 7. Agregar el archivo file.pdf en la carpeta docs

Deberá ser un archivo pdf con el texto que se desea analizar en el proyecto

## 8. Correr el servidor
```bash
python main.py
```

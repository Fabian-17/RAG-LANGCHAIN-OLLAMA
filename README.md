# RAG-LANGCHAIN

RAG-LANGCHAIN es un proyecto diseñado para demostrar el uso de cadenas de lenguaje en aplicaciones de recuperación y generación de texto.

## Requisitos

- Node.js (v14 o superior)
- npm (v6 o superior)
- Python 3(3.0 en adelante)
- pip

## Instalación

Para instalar y configurar el proyecto, sigue estos pasos:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Fabian-17/RAG-LANGCHAIN-OLLAMA.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd RAG-LANGCHAIN-OLLAMA
    ```
3. Navega hasta la carpeta del cliente e instala las dependencias:
    ```bash
    cd client
        npm install
    ```
4. Navega hasta la carpeta del servidor e instala las dependencias:
    ```bash
    cd server
        pip install -r requirements.txt
    ```

## Uso

Para ejecutar el proyecto en modo desarrollo, utiliza el siguiente comando desde el cliente:
```bash
npm run dev
```

Para ejecutar el servidor:
```bash
uvicorn main:app --reload
```
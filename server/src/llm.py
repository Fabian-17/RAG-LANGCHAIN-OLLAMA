from src.config import env
from langchain_ollama import ChatOllama
from langchain_core.language_models import LLM

class LlmCreator:
    def __init__(self, model: str):
        self._model_instance = ChatOllama(model=model)

    @property
    def model(self) -> LLM:
        return self._model_instance

llm = LlmCreator(model=env.model).model

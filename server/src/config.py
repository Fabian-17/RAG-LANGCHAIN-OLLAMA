from dotenv import load_dotenv
import os

class Config:
    def __init__(self):
        load_dotenv()

    @property
    def model(self) -> str:
        return os.getenv('MODEL') or "llama3.2:1b"
    
    @property
    def file(self) -> str:
        return os.getenv('FILE') or "docs/file.pdf"
    
env = Config()
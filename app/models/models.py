from pydantic import BaseModel

class Text(BaseModel):
    text: str

class TextOut(BaseModel):
    original: str
    anonymized: str
    entities_found: list | None = None
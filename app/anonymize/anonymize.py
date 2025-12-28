from fastapi import APIRouter
from app.services.services import anonymize
from app.models.models import Text

router = APIRouter()

@router.post("/anonymize")
async def anonymize_text(text: Text, query: str):
    return await anonymize(text.text, query)

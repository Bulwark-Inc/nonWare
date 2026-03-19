from ninja import Schema, Router
from .models import ContactMessage, QuoteRequest

router = Router()


class ContactIn(Schema):
    name: str
    email: str
    message: str


class QuoteIn(Schema):
    name: str
    email: str
    project_type: str
    budget: str
    description: str


@router.post("/contact")
def contact(request, data: ContactIn):
    ContactMessage.objects.create(**data.dict())
    return {"success": True}


@router.post("/quote")
def quote(request, data: QuoteIn):
    QuoteRequest.objects.create(**data.dict())
    return {"success": True}
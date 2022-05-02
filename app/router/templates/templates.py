from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/templates", tags=["templates"])

templates = Jinja2Templates(directory="templates")


@router.get("product/{id}", response_class=HTMLResponse)
def get_product(id: str, request: Request):
    return templates.TemplateResponse(
        "product.html",
        {
            "request": request,
            "id": id,
        },
    )

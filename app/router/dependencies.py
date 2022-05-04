from fastapi import APIRouter, Request, Depends

router = APIRouter(prefix="/dependencies", tags=["dependencies"])


def convert_headers(request: Request, separator: str = "-+"):
    out_headers = []
    for key, value in request.headers.items():
        out_headers.append(f"{key} {separator} {value}")
    return out_headers


@router.get("/")
def get_items(separator: str = "--", headers=Depends(convert_headers)):
    return {"items": ["a", "b", "c"], "headers": headers}


@router.post("/")
def create_item(headers=Depends(convert_headers)):
    return {"result": "new item created", "headers": headers}


class Account:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


@router.post("/user")
def create_user(
    name: str, email: str, password: str, account: Account = Depends(Account)
):
    # account - perform wether account operations
    return {"name": account.name, "email": account.email}
    pass

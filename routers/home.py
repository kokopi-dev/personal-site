#!/usr/bin/env python3
from fastapi import APIRouter, Request
from utils import templates

router = APIRouter(
    tags=["home"]
)

@router.get("/")
async def home_home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("home.html", context=context)

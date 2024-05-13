#!/usr/bin/env python3
from typing import Annotated
from fastapi import APIRouter, Depends, Request
from utils import templates
from info import About, Experiences, Navbar, ThisWebsite, Profile
from info.profile import SocialEnum
from db.tables.blogs import BlogTable

router = APIRouter(
    tags=["home"]
)

def get_blog_table() -> BlogTable:
    return BlogTable()

BlogTableDep = Annotated[BlogTable, Depends(get_blog_table)]

@router.get("/")
async def home_home(request: Request, table: BlogTableDep):
    blog_meta = await table.get_random_blog_meta()
    context = {
        "request": request,
        "profile": Profile(),
        "navbar": Navbar(),
        "experiences": Experiences(),
        "blog_meta": blog_meta,
        "about": About(),
        "site": ThisWebsite(),
        "social_enums": SocialEnum
    }
    return templates.TemplateResponse("home.html", context=context)


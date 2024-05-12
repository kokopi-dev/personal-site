#!/usr/bin/env python3
from fastapi import APIRouter, Request
from utils import templates
from services.random_blog import get_random_coding_blog_meta
from info import About, Experiences, Navbar, ThisWebsite, Profile
from info.profile import SocialEnum

router = APIRouter(
    tags=["home"]
)

@router.get("/")
async def home_home(request: Request):
    blog_meta = await get_random_coding_blog_meta()
    context = {
        "request": request,
        "profile": Profile(),
        "navbar": Navbar(),
        "experiences": Experiences(),
        "random_blog": blog_meta,
        "about": About(),
        "site": ThisWebsite(),
        "social_enums": SocialEnum
    }
    return templates.TemplateResponse("home.html", context=context)

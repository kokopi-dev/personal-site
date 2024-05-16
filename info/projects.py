#!/usr/bin/env python3
from pydantic import BaseModel

class Project(BaseModel):
    name: str
    url: str
    description: str
    tech: list[str]
    github: bool

class Projects(BaseModel):
    items: list[Project] = [
        Project(
            name="derrickgee.dev",
            url="https://github.com/kokopi-dev/personal-site",
            description="Portfolio site.",
            tech=["Python", "FastAPI", "Tailwindcss"],
            github=True
        ),
        Project(
            name="Vim (Neovim) Config",
            url="https://github.com/kokopi-dev/dotfiles/tree/master/nvim",
            description="My personal neovim config along with my Linux dotfiles.",
            tech=["Lua"],
            github=True
        ),
        Project(
            name="kokopi.dev",
            url="https://kokopi.dev",
            description="Personal blog site.",
            tech=["Hugo", "Javascript", "Tailwindcss"],
            github=False
        ),
    ]

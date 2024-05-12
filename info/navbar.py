#!/usr/bin/env python3
from pydantic import BaseModel

class NavbarItem(BaseModel):
    name: str
    id: str

class Navbar(BaseModel):
    items: list[NavbarItem] = [
        NavbarItem(name="About", id="#about"),
        NavbarItem(name="Experience", id="#exp"),
        NavbarItem(name="Blog", id="#blog")
    ]

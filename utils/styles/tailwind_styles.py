#!/usr/bin/env python3
from pydantic import BaseModel

class Buttons(BaseModel):
    normal: str = "py-1.5 px-3 rounded-md bg-stone-950 font-medium text-indigo-400 hover:text-indigo-300 hover:outline outline-1 outline-slate-700 shadow"
    nav: str = "text-indigo-300 underline hover:no-underline hover:text-indigo-500 font-bold"

class Headers(BaseModel):
    """Delete if needed, this is for an example"""
    pass

class Nav(BaseModel):
    sidenav_button: str = "p-3 hover:bg-indigo-950 rounded-md [&.active]:bg-indigo-800/90"

class TailwindStylesBase:
    buttons: Buttons = Buttons()
    nav: Nav = Nav()

    def get_active_nav(self, current_url, nav_url) -> str:
        if f"{nav_url}" in f"{current_url}":
            return "active"
        return ""

TailwindStyles = TailwindStylesBase()

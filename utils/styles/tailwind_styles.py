#!/usr/bin/env python3
from pydantic import BaseModel

class Badges(BaseModel):
    regular: str = "block rounded-full dark:bg-c-primary/75 bg-c-primary-li/60 dark:text-c-base-200 text-c-base-200-li font-semibold px-3 py-1"

class Cards(BaseModel):
    info: str = "flex flex-col gap-1.5 dark:bg-c-base-200 bg-c-base-200-li p-4 rounded-md dark:shadow-black shadow-md"

class TailwindStylesBase:
    cards: Cards = Cards()
    badges: Badges = Badges()

    def get_active_nav(self, current_url, nav_url) -> str:
        if f"{nav_url}" in f"{current_url}":
            return "active"
        return ""

TailwindStyles = TailwindStylesBase()

#!/usr/bin/env python3
from pydantic import BaseModel

class ThisWebsite(BaseModel):
    github: str = "#"
    description: str = "This site was deployed on a VPS with DigitalOcean, built with:"
    tech: list[str] = ["Python", "FastAPI", "Tailwindcss", "Javascript"]

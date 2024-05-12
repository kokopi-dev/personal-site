#!/usr/bin/env python3
from pydantic import BaseModel

class ThisWebsite(BaseModel):
    github: str = "#"
    description: str = "This site was deployed on VPS with DigitalOcean."
    tech: list[str] = ["Python", "FastAPI", "Tailwindcss"]

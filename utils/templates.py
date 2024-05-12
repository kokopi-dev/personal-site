#!/usr/bin/env python3
from fastapi.templating import Jinja2Templates
from utils.styles.tailwind_styles import TailwindStyles
from utils import Env
from datetime import datetime
from datetime import UTC

def versioning(input):
    return f"{input}?v={int(datetime.now().timestamp())}"

def rel_static(static_filename: str):
    return f"/static/{static_filename}"

templates = Jinja2Templates(directory="templates")
custom_variables = {
    "rel_static": rel_static,
    "settings": Env,
    "styles": TailwindStyles,
    "now": datetime.now(UTC)
}
templates.env.globals.update(custom_variables)
templates.env.filters["version"] = versioning

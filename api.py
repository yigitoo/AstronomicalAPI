from typing import (
    List,
    Dict,
    Tuple,
    Any,
)
from fastapi import (
    FastAPI
)

from models import (
    Planet,
)

app = FastAPI()

@app.get('/')
def Root_Page():
    return {
        "desc": "API root url",
        "route": "/",
    }

@app.get('/planets/{planet_name}')
def Get_Spesific_Planet(planet_name: str, q: str | None = None):
    return {
        "planet_name": planet_name,
        "query": q if q is not None else "",
    }


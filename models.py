from pydantic import BaseModel
from typing import (
    Dict,
    Any,
    List,
)
import os

class Planet(BaseModel):
    planet_name: str
    planet_id: int
    planet_properties: Dict[str, Any]
    spesific_prop: str | None = None

class DBModel:
    query: str | None = None

    def __init__(self, query: str | None = None, connection_url: str | None = None):
        self.query = query
        self.connection_url = connection_url if connection_url is not None else os.getenv('DB_CONNECTION_URL')
        self.db: Any

    def execute(self, query: str | None = None) -> Any:
        if query is not None:
            self.query = query

        if self.is_connected:
            self.db.execute(self.query)
        else:
            print("First you must connect to the database. And it's not connected!")
            try:
                self.connect()
                self.execute()
            except:
                print("Cannot connect to the database.")

    def connect(self, connection_url: str | None = None):
        if connection_url is not None:
            self.connection_url = connection_url

        if self.connection_url is not None:
            self.db.connect(self.connection_url)

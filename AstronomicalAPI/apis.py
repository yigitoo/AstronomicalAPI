from typing import (
    Dict,
    List,
    Tuple,
    Any,
    Self
)

class API:
    def __init__(self, key: str | None = None):
        if key is not None:
            self.key = key


    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if exc_type is None and trace is None:
            return self.close()

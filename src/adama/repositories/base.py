from abc import ABC
import sqlite3
from typing import Generic, TypeVar

from adama.config import config

T = TypeVar("T")
class Repository(ABC, Generic[T]):
	def __init__(self) -> None:
		self.conn = sqlite3.connect(config.database.DB_PATH)

	def save(self, entity: T) -> bool: ...
	def load(self, id: int) -> T | None: ...
	def delete(self, id: int) -> bool: ...
	def all(self) -> list[T]: ...
	

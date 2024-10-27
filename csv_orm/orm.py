import csv
import os
from dataclasses import fields
from typing import Type, TypeVar

from csv_orm.operations import create, delete, get_all, get_one, update

T = TypeVar("T")


def orm_csv(file_path: str):
    def decorator(cls: Type[T]) -> Type[T]:
        cls._file_path = file_path

        if not os.path.exists(file_path):
            with open(file_path, mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=[f.name for f in fields(cls)])
                writer.writeheader()

        setattr(cls, "get_all", classmethod(get_all))
        setattr(cls, "create", classmethod(create))
        setattr(cls, "get_one", classmethod(get_one))
        setattr(cls, "update", classmethod(update))
        setattr(cls, "delete", classmethod(delete))

        return cls

    return decorator

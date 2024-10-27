from dataclasses import dataclass

from csv_orm.orm import orm_csv


@dataclass
@orm_csv("person.csv")
class Person:
    uid: int
    name: str

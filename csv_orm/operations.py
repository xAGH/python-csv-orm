import csv
from dataclasses import asdict, fields
from typing import List, Optional, Type, TypeVar

T = TypeVar("T")


def get_all(cls: Type[T]) -> List[T]:
    instances = []
    with open(cls._file_path, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            instances.append(cls(**row))
    return instances


def create(cls: Type[T], **kwargs) -> T:
    instance = cls(**kwargs)
    with open(cls._file_path, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[f.name for f in fields(cls)])
        writer.writerow(asdict(instance))
    return instance


def get_one(cls: Type[T], uid: int) -> Optional[T]:
    with open(cls._file_path, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["uid"]) == uid:
                return cls(**row)
    return None


def update(cls: Type[T], uid: int, **kwargs) -> bool:
    updated = False
    records = []
    with open(cls._file_path, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["uid"]) == uid:
                row.update(kwargs)
                updated = True
            records.append(row)

    if updated:
        with open(cls._file_path, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[f.name for f in fields(cls)])
            writer.writeheader()
            writer.writerows(records)

    return updated


def delete(cls: Type[T], uid: int) -> bool:
    deleted = False
    records = []
    with open(cls._file_path, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["uid"]) != uid:
                records.append(row)
            else:
                deleted = True

    if deleted:
        with open(cls._file_path, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[f.name for f in fields(cls)])
            writer.writeheader()
            writer.writerows(records)

    return deleted

from entities.person import Person

if __name__ == "__main__":
    person = Person.get_one(uid=1)
    print(person)
    all_records = Person.get_all()
    print(all_records)
    Person.update(uid=1, name="Alice Updated")
    person_updated = Person.get_one(uid=1)
    print(person_updated)
    Person.delete(uid=1)
    all_after_delete = Person.get_all()
    print(all_after_delete)
    person_created = Person.create(uid=10, name="Andrés")
    print(person_created)
    all_after_create = Person.get_all()
    print(all_after_create)

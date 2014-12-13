from model.person import Person

persons = []


class PersonNotFoundException(Exception):

    def __init__(self, msg):
        super().__init__(msg)


class PersonService(object):

    """docstring for PersonService"""

    def __init__(self, dc=None):
        self.dc = dc

    def save(self, name):
        persons.append(Person(name))

    def remove(self, name):
        person = None
        for p in persons:
            if p.name == name:
                person = p
        if person:
            persons.remove(person)

    def get(self, name):
        for p in persons:
            if p.name == name:
                return p
        raise PersonNotFoundException('cannot find Person with name:' + name)

    def getAll(self):
        for p in persons:
            print(p.name)


if __name__ == "__main__":
    personService = PersonService()
    personService.save('john')
    personService.save('alex')
    personService.save('smith')

    # personService.getAll()

    personService.remove('alex')
    personService.getAll()

    # john = personService.get('john')
    # print(john.name)

    # john_kell = personService.get('john kell')
    # print(john_kell.name)

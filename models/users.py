# описание свойств будущего объекта(ов)
class User:
    name: str
    age: int
    status: str
    itemt: list[str]

    # инициализация описанного класса
    def __init__(self, name, age, status, items):
        self.name = name
        self.age = age
        self.status = status
        self.itemt = items


# __name__ что это?
if __name__ == '__main__':
    vasia = User("Vas", 18, "worker", [])
    anna = User("Ana", 16, "student", [])
    print(anna)

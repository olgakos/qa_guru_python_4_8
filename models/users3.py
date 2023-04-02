from dataclasses import dataclass


# автоматчиески создаст конструктор (для всех атрибутов, описанных в свойствах убдущего класса)
@dataclass
# описание свойств будущего объекта(ов)
class User:
    name: str
    age: int
    status: str
    itemt: list[str]

    # встроенный метод датакаласса умеющий показывать на экрен сожержимое класса...
    # def __repr__(self):
    # встроенынй метод датакаласса умеющий сравнивать ОБЪЕКТЫ между собой... (типа пользователи равны если равны наприемр все их 4 атрибута)
def __eq__(self, other):

        '''
# инициализация описанного класса
    def __init__(self, name, age, status, items):
        self.name = name
        self.age = age
        self.status = status
        self.itemt = items
        '''



# __name__ что это?
if __name__ == '__main__':
    vasia = User("Vas", 18, "worker", [])
    anna = User("Ana", 16, "student", [])
    assert (vasia == anna) #сожержимое объектов не прано, чтд



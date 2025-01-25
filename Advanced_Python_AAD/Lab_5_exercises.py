class Animal():
    __name = ''
    __age = '0'
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_all(self, name, age):
        self.__name = name
        self.__age = age
    
    def __str__(self):
        return self.get_str()

class Dolphin(Animal):
    __type_of = 'Дельфин'
    def get_type_of(self):
        return self.__type_of
    def get_str(self):
        return " ".join([" Имя:", self.get_name(), "\n", "Возраст:", self.get_age(), "\n", "Тип животного:", self.get_type_of()])

class Zebra(Animal):
    __type_of = 'Зебра'
    def get_type_of(self):
        return self.__type_of
    def get_str(self):
        return " ".join([" Имя:", self.get_name(), "\n", "Возраст:", self.get_age(), "\n", "Тип животного:", self.get_type_of()])


class Mother():
    __name = 'M'
    def __str__(self):
        return " ".join(self.__name)


class Daughter(Mother):
    __name = 'D'
    __age = '12'
    def __str__(self):
        return " ".join([self.__name, ' ', self.__age])

class Shape:
    __hight = 0.0
    __width = 0.0

    def get_hight(self):
        return self.__hight

    def get_width(self):
        return self.__width

    def set_hight(self, hight):
        self.__hight = hight

    def set_width(self, width):
        self.__width = width


class Triangle(Shape):
    def area(self):
        return (tr.get_hight() * tr.get_width() * 0.5)

class Rectangle(Shape):
    def area(self):
        return (re.get_hight() * re.get_width())

if __name__ == "__main__":
    tr = Triangle()
    re = Rectangle()

    #print("Введите высоту и ширину треугольника: ")
    #print("Высота: ", end= '')
    #tr.set_hight(float(input()))
    #print("Ширина: ", end= '')
    #tr.set_width(float(input()))
    #print("Площадь треугольника: ", tr.area())

    #print("Введите высоту и ширину прямоугольника: ")
    #print("Высота: ", end= '')
    #re.set_hight(float(input()))
    #print("Ширина: ", end= '')
    #re.set_width(float(input()))
    #print("Площадь прямоугольника: ", re.area())
    
    #--------------------------------------------------------------------

    #a = Mother()
    #b = Daughter()
    #print(a)
    #print(b)

    #--------------------------------------------------------------------

    #an1 = Dolphin()
    #an2 = Zebra()
    #print("Введите имя и возраст дельфина: ", end= '')
    #an1.set_all(*list(map(str, input().split(','))))
    #print("Введите имя и возраст зебры: ", end= '')
    #an2.set_all(*list(map(str, input().split(','))))
    #print()
    #print("Информация о дельфине:")
    #print(an1)
    #print()
    #print("Информация о зебре:")
    #print(an2)

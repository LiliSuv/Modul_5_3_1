class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ("Такого этажа не существует")
        else:
            print (new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):

        return f'Название: {self.name},кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")

        return self.number_of_floors == other

    def __lt__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors < other

    def __le__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")

        return self.number_of_floors <= other

    def __gt__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors > other

    def __ge__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors >= other

    def __ne__(self, other):
        if not isinstance (other, (int, House)):
            raise ArithmeticError ("other должен быть  int или объектом House")
        return self.number_of_floors != other

    def __add__(self, valuo):
        self.number_of_floors = self.number_of_floors + valuo
        return self.number_of_floors

    def __radd__(self, valuo):
        self.number_of_floors = valuo + self.number_of_floors
        return self.number_of_floors

    def __iadd__(self, valuo):
        return self.number_of_floors


h1 = House ('ЖК Эльбрус', 10)
h2 = House ('ЖК Акация', 20)
print (h1)
print (h2)
print (h1 == h2)
h1.number_of_floors = h1 + 10
print (h1)
print (h1 == h2)
h1.number_of_floors += 10
print (h1)
h2.number_of_floors = 10 + h2
print (h2)
print (h1 > h2)
print (h1 >= h2)
print (h1 < h2)
print (h1 <= h2)
print (h1 != h2)

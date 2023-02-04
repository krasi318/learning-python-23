class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "cant print objects like this"

    def __iter__(self):
        return "this is ", self.name, self.age

    def get_older(self):
        years = int(input("enter years : "))
        self.age += years
        print(self.name, " aged ", years, " years and now is ", self.age, " years old.")


p1 = Person("krasi", 19, 192)
p2 = Person("robi", 20, 178)
p3 = Person("sashko", 19, 182)
p4 = Person("marti", 20, 167)


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        return "bullshit"

    def calc_yearly_salary(self):
        print(self.salary * 12)


w1 = Worker("georg", 39, 162, 2000)
w2 = Worker("mustafa", 43, 174, 3000)

# w2.get_older()
# w2.calc_yearly_salary()


class Programmer(Worker):
    def __init__(self, name, age, height, salary, programming_lang):
        super(Programmer, self).__init__(name, age, height, salary)
        self.programming_lang = programming_lang

    def __str__(self):
        return "this is {} age {} height {} salary {} fav programming lang {} ".format(self.name, self.age, self.height,
                                                                                       self.salary,
                                                                                       self.programming_lang)

    def __iter__(self):
        return "this is {} age {} height {} salary {} fav programming lang {} ".format(self.name, self.age, self.height,
                                                                                       self.salary,
                                                                                       self.programming_lang)


programer = Programmer("joro", 34, 120, 5000, "python")
programer1 = Programmer("koko", 44, 200, 10000, "web")
w3 = Worker("sinan", 43, 174, 3000)

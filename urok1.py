class Kis:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def voice(self):
        if self.species == "кіт":
            print(f"{self.name} каже: Мяу!")
        elif self.species == "собака":
            print(f"{self.name} каже: Гав!")
        else:
            print(f"{self.name} видає незнайомий звук")

    def play(self):
        print(f"{self.name} грається")

    def eat(self, food):
        print(f"{self.name} їсть {food}")

    def grow(self, delta=1):
        self.age += delta
        print(f"{self.name} став(ла) старшим(ою) на {delta} рік/роки! Тепер йому/їй {self.age} років.")

cat = Kis(name="Мурка", age=3, species="кіт")
dog = Kis(name="Бобик", age=5, species="собака")

cat.voice()
dog.voice()

cat.play()
dog.play()

cat.eat("рибу")
dog.eat("м'ясо")

cat.grow(2)
dog.grow(4)
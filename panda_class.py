class Panda:
    def __init__(self, name, age, weight, favorite_food):
        self.name = name
        self.age = age
        self.weight = weight
        self.favorite_food = favorite_food
    def wieght(self):
        print(f"this Panda his wieght is {self.weight}")
    def eat(self):
        print(f"{self.name} is eating {self.favorite_food}.")

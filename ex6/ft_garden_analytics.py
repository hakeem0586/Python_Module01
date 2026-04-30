#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ariandri <ariandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 14:50:14 by ariandri            #+#    #+#            #
#   Updated: 2026/04/30 15:59:49 by ariandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from os import name


class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int
            ) -> None:

        self.name = name
        self._height = height if height >= 0 else 0.0
        self._plant_age = plant_age if plant_age >= 0 else 0
    
    def get_name(self) -> str:
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float) -> None:
        if (new_height < 0):
            print(
                f"{self.name.capitalize()}: Error, "
                f"height can't be negative"
            )
            print("Height update rejected")
            return
        print(f"Height updated: {new_height}cm")
        self._height = float(new_height)

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, new_plant_age: int) -> None:
        if (new_plant_age < 0):
            print(
                f"{self.name.capitalize()}: Error, "
                f"age can't be negative"
            )
            print("Age update rejected\n")
            return
        print(f"Age updated: {new_plant_age} days\n")
        self._plant_age = new_plant_age

    @staticmethod
    def is_check_days(plant_age: int) -> str:
        if plant_age > 365:
            print (f"Is {plant_age} days more than a year? -> True")
        else:
            print (f"Is {plant_age} days more than a year? -> False")
    
    @classmethod
    def anonymous_plant(
        cls,
        name: str = "Unknown",
        height: float = 0.0,
        plant_age: int = 0
    ) -> "Plant":
        return cls(name, height, plant_age)
    
    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{round(self._height, 1)}cm, "
            f"{round(self._plant_age, 1)} days old"
        )


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int,
            color: str
            ) -> None:
        super().__init__(name, height, plant_age)
        self._color = color
        self._bloomed = False

    def get_color(self) -> str:
        return self._color

    def set_color(self, new_color: str) -> None:
        self._color = new_color

    def bloom(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self.name.capitalize()} has not bloomed yet.")
            self._bloomed = True
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")

class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int,
            color: str,
            number_of_seeds: int = 0
            ) -> None:
        super().__init__(name, height, plant_age, color)
        self._number_of_seeds = number_of_seeds
    
    def bloom(self) -> None:
        super().show()
        if self._number_of_seeds == 0:
            print(f" {self.name.capitalize()} has not bloomed yet.")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        print(f" Seeds: {self._number_of_seeds}")

    def grow_height_and_age(self, days: int) -> None:
        self._height += 1.5
        self._plant_age += days
        self._number_of_seeds = 42

class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, plant_age)
        self._trunk_diameter = trunk_diameter
        self.__produced_shade = False

    def produce_shade(self) -> None:
        if not self.__produced_shade:
            self.__produced_shade = True
        else:
            print(
                f"Tree {self.name.capitalize()} now produces a shade of "
                f"{round(self._height, 1)}cm long and "
                f"{self._trunk_diameter}cm wide."
            )
    
    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 plant_age: int,
                 harvest_saison: str,
                 nutritional_value: int
                 ) -> None:
        super().__init__(name, height, plant_age)
        self._harvest_saison = harvest_saison
        self._nutritional_value = 0

    def grow(self, days: int) -> None:
        self._height += 2.1

    def age(self, days: int) -> None:
        self._plant_age += days
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_saison}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Garden statistics  ===")
    print("=== Check year-old ")
    Flower.is_check_days(30)
    Flower.is_check_days(400)
    print("\n=== Flower ")
    rose.bloom()
    print("[statistics for Rose]")
    print("=== Tree ")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("\n=== Seed ")
    seed = Seed("Sunflower", 80.0, 25, "yellow", 0)
    seed.bloom()
    print("[make sunflower grow, age and bloom]")
    for _ in range(20):
        seed.grow_height_and_age(1)
    seed.bloom()
    print("\n=== Anonymous")
    plant = Plant.anonymous_plant()
    plant.show()
    
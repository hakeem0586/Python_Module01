#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ariandri <ariandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/29 14:50:14 by ariandri            #+#    #+#            #
#   Updated: 2026/05/22 15:31:23 by ariandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    class Statistics:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.shade_calls = 0

        def display(self):
            print(
                f"Stats: {self.grow_calls} grow,"
                f"{self.age_calls} age, {self.show_calls} show"
                )

    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int
            ) -> None:

        self.name = name
        self._height = height if height >= 0 else 0.0
        self._plant_age = plant_age if plant_age >= 0 else 0
        self.stats = self.Statistics()

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
        return plant_age > 365

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
        self.stats.show_calls += 1


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

    def grow(self) -> None:
        self._height += 8
        self.stats.grow_calls += 1

    def age_up(self):
        self.stats.age_calls += 1

    def bloom(self) -> None:
        self.show()
        print(f" Color: {self._color}")
        if not self._bloomed:
            print(f" {self.name.capitalize()} has not bloomed yet.")
            self._bloomed = True
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            plant_age: int,
            trunk_diameter: float,
            ) -> None:
        super().__init__(name, height, plant_age)
        self._trunk_diameter = trunk_diameter

    def grow(self):
        self.stats.grow_calls += 1

    def age_up(self):
        self.stats.age_calls += 1

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )
        self.stats.shade_calls += 1

    def show(self):
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


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

    def grow_height_and_age(self) -> None:
        self._height += 30
        self._plant_age += 20
        self._number_of_seeds = 42
        self.stats.grow_calls += 1
        self.stats.age_calls += 1

    def bloom(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._number_of_seeds == 0:
            print(f" {self.name.capitalize()} has not bloomed yet.")
        else:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        print(f" Seeds: {self._number_of_seeds}")


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()

    if isinstance(plant, Tree):
        print(f"{plant.stats.shade_calls} shade")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_check_days(30))
    print("Is 400 days more than a year? ->", Plant.is_check_days(400))

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.bloom()
    show_statistics(rose)
    rose.grow()
    rose.bloom()
    show_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    show_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_statistics(oak)

    print("\n=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    sun.bloom()
    print("[make sunflower grow, age and bloom]")
    sun.grow_height_and_age()
    sun.bloom()
    show_statistics(sun)

    print("\n=== Anonymous")
    a = Plant.anonymous_plant()
    a.show()
    show_statistics(a)

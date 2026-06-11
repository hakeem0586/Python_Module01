#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ariandri <ariandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 08:53:42 by ariandri            #+#    #+#            #
#   Updated: 2026/06/11 15:39:40 by ariandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
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
        if new_height < 0:
            print(
                f"{self.name.capitalize()}: Error, "
                f"height can't be negative"
            )
            print("Height update rejected")
            return
        print(f"Height updated: {new_height}cm")
        self._height = new_height + 0.0

    def get_age(self) -> int:
        return self._plant_age

    def set_age(self, new_plant_age: int) -> None:
        if new_plant_age < 0:
            print(
                f"{self.name.capitalize()}: Error, "
                f"age can't be negative"
            )
            print("Age update rejected\n")
            return
        print(f"Age updated: {new_plant_age} days\n")
        self._plant_age = new_plant_age

    def grow(self) -> None:
        self._height += 0.8

    def grow_age(self) -> None:
        self._plant_age += 1

    def show(self) -> None:
        print(
            f"Plant created: {self.name.capitalize()}: "
            f"{round(self._height, 1)}cm, "
            f"{round(self._plant_age, 1)} days old\n"
        )


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-10)
    print(
        f"Current state: {rose.get_name().capitalize()}: "
        f"{round(rose.get_height(), 1)}cm, "
        f"{rose.get_age()} days old")

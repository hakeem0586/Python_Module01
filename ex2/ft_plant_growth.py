#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ariandri <ariandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/09 13:05:53 by ariandri            #+#    #+#            #
#   Updated: 2026/04/09 14:37:58 by ariandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{round(self.height, 1)}cm, "
            f"{self.plant_age} days old"
        )


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    day1 = plant.height
    plant.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age()
        plant.show()
        day7 = plant.height
    total = round(day7 - day1, 1)
    print(f"Growth this week: {total}cm")

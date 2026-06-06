#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ariandri <ariandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/14 08:53:59 by ariandri            #+#    #+#            #
#   Updated: 2026/04/14 08:54:00 by ariandri           ###   ########.fr      #
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
            f"Created: {self.name.capitalize()}: "
            f"{round(self.height, 1)}cm, "
            f"{self.plant_age} days old"
        )


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for plant in plants:
        plant.show()

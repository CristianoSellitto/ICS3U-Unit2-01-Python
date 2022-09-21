#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in September 2022
# A program that finds the area and perimeter for a circle

import math


def main():
    # Finds the area and perimeter of a circle with a radius of 15mm

    print("A circle is has a radius of 15mm")
    print("\nThis circle's area is {}mm²".format(math.pi * 15**2))
    print("This circle's perimeter is {}mm".format(math.pi * (15 * 2)))

    print("\nDone.")


if __name__ == "__main__":
    main()

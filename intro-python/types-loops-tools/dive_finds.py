#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script flow and debugging. Print your own fortune cookie!

Copyright (c) 2018-2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import random


DIVEFINDS = [
    "engagement rings 💍 and other rings ",
    "completely ruined mobile phones 📱",
    "⌚ Apple, Rolex, and Timex watches",
]


def generate_find() -> str:
    """Use a random selection to determine the scuba diver's find."""
    return random.choice(DIVEFINDS)


def calculate_number_items(number_dives):
    """Returns the multiplier for the random amounts of found objects."""
    how_many = random.randint(1, 15)
    dive_items = how_many * number_dives
    
    return dive_items


def create_dive_finds(number_dives):
    """Make and return the items the scuba diver finds in this dive.

    The message should include the diver's finds and amounts.
    """
    # TODO: Create a message telling a scuba diver what they found by 
    # calling generate_find() and calculate_number_items() and 
    # then composing and returning the message and numbers.
    finds = generate_find()
    number_items = calculate_number_items(number_dives)

    return "In {} dives, you found {} {}".format(number_dives, number_items, finds)
    #raise NotImplementedError()


def main():
    """Explain the scuba diver game in a command prompt."""
    print("You're a scuba diver, let's see what you find on your dives today!")

    # Prompt the user for how many dives they are going on
    number_dives = input("How many dives are you taking today?  ")
    number_dives = int(number_dives.strip())

    # Create and display their finds
    dive_finds_message = create_dive_finds(number_dives)
    print("\nHere are your finds, you lucky diver!\n")
    print(dive_finds_message)


if __name__ == '__main__':
    main()

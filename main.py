#/!usr/bin/env python3
#-*- coding: utf-8 -*-

''' This is the main program for the keyboard typing program. '''

import os
from functions import TypingTest

# MAIN MENU
def print_menu():
    '''^'''

    os.system("clear")
    print("\nw3lc0m3 t0 k3yb04rd typ1ng pr4ct1c3!\n")
    print("# Play")
    print("------")
    print("(1) easy")
    print("(2) medium")
    print("(3) hard")
    print("(4) randomized")
    print("\n# Scoreboard")
    print("------------")
    print("(5) view")
    print("(r) reset")
    print("\n# Other")
    print("--------")
    print("(q) quit")

print_menu()

# MENU HANDLER
def main():
    '''^'''
    typing_test = TypingTest()

    while True:

        choice = input("\nPick your choice: ")

        if choice == "1":
            typing_test.main_typing_test("easy.txt")

        elif choice == "2":
            typing_test.main_typing_test("medium.txt")

        elif choice == "3":
            typing_test.main_typing_test("hard.txt")

        elif choice == "4":
            typing_test.random_typing_test()

        elif choice == "5":
            typing_test.view_score("score.txt")

        elif choice == "r":
            typing_test.reset_score("score.txt")

        elif choice == "q":
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

import random
import tkinter as tk


def Menu():
    print("/ *************************************** \ \n| *************************************** |\n| ******* Welcome to game thingy! ******* |\n| *******    Select your Level!   ******* |\n| *************************************** |") 
    print("| Levels | [1]Easy | [2]Medium | [3]Hard  |")
    level_selector = int(input("Select Your Level! :"))

    match level_selector:

        case 1:
            print("Preparing level 1....")
            level1()

def level1():
    low = 0
    high = 12
    lives = 5
    num_que = 0

    #engine
    while lives > 0 and num_que < 10:
        num1 = 4
        num2 = random.randint(low, high)
        que = num1 * num2

        print(f"{num1} x {num2} = ?")
        answer = int(input("Answer = "))
        
        if answer == que:
            num_que += 1
            print(f"| correct! | Lives: {lives} | Questions Left: {num_que}/10 |")
                
        elif answer != que:
            lives -= 1
            num_que += 1
            print(f"| incorrect! | lives: {lives} | Questions Left: {num_que}/10 |")

        else:
            print("you have died...")
            break

Menu()



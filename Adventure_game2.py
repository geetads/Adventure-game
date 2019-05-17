import time
import random


enemies = ["witch", "gorgon", "pirate", "troll"]
enemies_list = random.choice(enemies)
enemy = enemies_list
weapons = ["sword", "gun", "magic wand"]
weapons_list = random.choice(weapons)
weapon = weapons_list


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("Welcome To Adventure Game")
    print_pause("You find yourself in an open field,filled with "
                "grass and yellow wild flowers!!")
    print("Rumor has it that", enemy, "is somewhere around here..")
    time.sleep(2)
    print_pause("In front of you is a House.")
    print_pause("To your right is a dark cave.")


def House(items):
    print_pause("You approach to the door of the house")
    print("The door opens and steps out a", enemy, "!!")
    time.sleep(2)
    print("It's the house of", enemy, "...")
    time.sleep(2)
    print("The", enemy, "attacks you !!")
    time.sleep(2)
    if weapon in items:
        decide = input("Would you like to fight (1) or run away(2):\n")
        if decide == '1':
            print("You have the new", weapon, "which you found in cave!!")
            time.sleep(2)
            print("The", enemy, "got scared of the", weapon, "runs away...")
            time.sleep(2)
            print_pause("You are victorious!!")
        elif decide == '2':
            print_pause("You decide to went back and no one follwed you!")
        else:
            print_pause("Sorry, I don't understand")
    else:
        print_pause("You feel under prepared with only having a dagger..")
        decide = input("Would you like to fight (1) or run away(2):\n")
        if decide == '1':
            print_pause("You decided to fight.You do your best..")
            print("but your dagger is no match for", enemy, "!")
            time.sleep(3)
            print_pause("You have been defeated !!")
        elif decide == '2':
            print_pause("You decide to went back and no one followed you!!")
        else:
            print_pause("Sorry, I don't understand.")
    play_again()


def play_again():
    choice = input("would you like to play again y or n:\n").lower()
    if 'n' in choice:
        print_pause("Ok,Good bye")
    elif 'y' in choice:
        print_pause("Good,Restart the game again!!")
        play_game()
    else:
        print_pause("Sorry, I don't understand.")
        play_again()


def cave(items):
    print_pause("You Enter in the cave.")
    print_pause("It is a very small cave.")
    if weapon in items:
        print("But you have already visited the cave and got a", weapon)
        time.sleep(2)
        print_pause("Nothing more to do here,you went back.")
    else:
        print("You found a", weapon)
        time.sleep(2)
        print_pause("You keep that with you!!")
        items.append(weapon)
    choose(items)


def choose(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    response = input("What would you like to do,Please enter 1 or 2:\n")
    if response == '1':
        House(items)
    elif response == '2':
        cave(items)
    else:
        print_pause("Sorry,I don't understand")
        choose(items)


def play_game():
    items = []
    intro()
    choose(items)


play_game()

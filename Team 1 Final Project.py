#Name Zachary Martin, Kevin Zheng, Samuel Raymond, Ethan Wright
#Assignment: Final Project Scrum
#https://docs.google.com/document/d/1xLITZ3sbBAi-nxTY1c0BQ9JA3w3nUmJXvG8FJAbmSRQ/edit?tab=t.0

import random
import time

def Start_Adventure():

    print("Which type of adventure would you like to go on.")
    print("Your option are Kevin, Samuel, Ethan")

    choice = input("Type Kevin, Ethan, or Samuel to choose your adventure")

    if choice == "Kevin" or choice == "kevin":
        print("Kevin's adventure")
        Kevin()
    elif choice == "Ethan" or choice == "ethan":
        print("Ethan's adventure")
        Ethan()
    elif choice == "Samuel" or choice == "samuel" or choice == "Sam" or choice == "sam":
        print("Samuel's Adventure")
        Samuel()

def Samuel():
        print("you have chosen Samuels minecraft adventure")
        print ("you have appeared in a MINECRAFT world and you are in hardcore mode")
        print ("you have two options try to find a village or chop a tree to get wood")
        print ("put in tree or village")
        sam1 = input()
        if sam1 == "tree":
            print("tree")
        if sam1 == "village":
            print("village")
        else:
            print ("pick again")

        print ("you have now collected a bunch of wood")
        print ("do you build a house or go mining")
        print ("put in house or mine")
        sam1 = input()
        if sam1 == "tree":
            print("tree")
        if sam1 == "village":
            print("village")
        else:
            print ("pick again")

        print("you keep going trying to find a village but end up in a dessert")
        print("do you try to keep going or give up")
        print("put in try or give")
        sam1 = input()
        if sam1 == "try":
            print("try")
            print("YOU DIE of hunger after searching so long")
        if sam1 == "give":
            print("give")
            print("YOU DIE of a creeper after not paying attention to your surroundings")
        else:
            print("pick again")

        print("you make a small camp")
        print("do you build or chop trees or get ore")
        print("put in chop or ore")
        sam1 = input()
        if sam1 == "chop":
            print("chop")
            print("YOU DIE to a zombie sneaking up to you")
        if sam1 == "ore":
            print("ore")
            print("YOU DIE to a skeleton shooting you in the back")
        else:
            print("pick again")

        print("you make a basic house")
        print("do you build a go out or stay")
        print("put in go or stay")
        sam1 = input()
        if sam1 == "go":
            print("go")
            print("YOU DIE because you looked at a enderman and he called you ugly")
        if sam1 == "stay":
            print("stay")
            print("YOU LIVE all alone :(")
        else:
            print("pick again")

        print("you find a cave full of iron and coal")
        print("do you make armor or keep mining")
        print("put in armor or mine")
        sam1 = input()
        if sam1 == "armor":
            print("armor")
            print("YOU DIE while you were making armor a spider snuck in threw your door and killed you")
        if sam1 == "mine":
            print("mine")
            print("YOU DIE of lead poisoning")
        else:
            print("pick again")

        print("you have collected a bunch of wood")
        print("do you build a house or go mining")
        print("put in house or mine")
        sam1 = input()
        if sam1 == "house":
            print("house")
        if sam1 == "mine":
            print("mine")
        else:
            print("pick again")

        print("you dont find a village")
        print("do you keep exploring or settle down")
        print("put in keep or settle")
        sam1 = input()
        if sam1 == "keep":
            print("keep")
        if sam1 == "settle":
            print("settle")
        else:
            print("pick again")

        print("you have chosen Samuels minecraft adventure")
        print("you have appeared now in the world on MINECRAFT and you are in hardcore")
        print("you have two options try to find a village or chop a tree to get wood")
        print("put in tree or village")
        sam1 = input()
        if sam1 == "tree":
            print("tree")
        if sam1 == "village":
            print("village")
        else:
            print("pick again")

def Kevin():
    print("well monkey you seem to have choosen me. Well what do u want to hunt")
    path = input("Choose: Slime or Goblin")
    if path.lower() == "slime":
        print("alright so u want to hunt slimes")
        slime()
    elif path.lower() == "goblin":
        print("alright so u want to hunt goblin")
        goblin()
def slime():
    print("You make your way through the dense, foggy forest, the ground squelching beneath your boots. The air smells faintly of decay,")
    print("And you can hear the occasional soft squish as slimes move about in the swamp. As you approach the pit, ")
    print("You spot a small group of slimes, their gelatinous bodies shimmering in the dim light. "
          "They seem to be gathered around something shiny in the mud. You ready your weapon, preparing for battle.")

    slimechoice = int(input("Choose: 1. Attack the slimes head-on and try to destroy them quickly."
          " or 2. Approach cautiously, hoping to learn more about what they are doing. What do you want to do"))
    if slimechoice == 1:
        print("you are going to face them head on")
        slimeheadon()

    elif slimechoice == 2:
        print("you are going to sneak around")
        slimesneak()
def slimeheadon():
    print("Why would u choose to do this you died no ending you are a goober")
    print("ggez no ending")
    quit()
def slimesneak():
    print("This doesn't work either goon you shouldn't have chosen this idiot.")
    print("The God of this world kills u no ending HAHAHAHA")
    quit()
def goblin():
    print("You walk through the trees, your footsteps light on the forest floor.")
    print("The Goblin Den is located deep within the rocky hills, and as you approach, the sounds of goblins laughing and shouting grow louder.")
    print("You spot a few goblins near the entrance, grinning mischievously as they make their way into the cave with stolen goods.")
    print("You can either sneak up on them or confront them head-on. You have a variety of tools at your disposal, but you know goblins are tricky creatures.")
    time.sleep(5)
    gobs = int(input("Choose: 1 Face the goblins head on or 2 sneak up on them"))
    if gobs  == 1:
        GobheadOn()
    if gobs == 2:
        Gobsneak()
def GobheadOn():
    print("You charge head on into the swarm of goblins")
    print("The goblins gnawed at you, small and twisted, with skin like moss and eyes that glinted in the dark.")
    print("The goblins teared apart your flesh and broke serval bones, but you swing your sword and kill dozens")
    print("You are bleeding, tired, and restless, but alive")
    coward = int(input("Choose: 1. Keep pushing until you wipe them out or 2. Leave and escape"))
    if coward == 1:
        print("You push forward and fight")
        print(" A fresh wave of goblins scuttled over the stone like rats. You meet them with a roar, swinging his sword in great arcs, severing limbs, breaking skulls. ")
        print("You took wounds deep slashes across your ribs. The goblins surged. You killed three more then five. ")
        time.sleep(3)
        print("But they were endless. Dawn came and you finally fell. Your sword lay beside you, soaked in blood, ")
        print(" As you take your last breath a goblin the last goblin looked at you, staring at you")
        print("By dawn, the goblins were gone and you a nameless figure were gone too")
        print("Ending 1 achieved THE GOAT")
        time.sleep(2)
        quit()
    if coward == 2:
        print("You died on the way back idiot should've been watching the path you were walking on")
        print("how do you step on a large comical spike idiot")
        print("no ending for u ")
        quit()
def Gobsneak():
    print("You sneak around moved low through the hollow, where twisted roots formed natural tunnels beneath the earth. ")
    print("Every breath was slow, controlled. Every step tested before weight was given.")
    print("You reach the edge of the goblin territory")
    time.sleep(5)
    choice2 = int(input("Chose: 1 Explore the root tunnel or 2 follow the ridge trail"))
    if choice2 == 1:
        rootTunnel()

    elif choice2 == 2:
        ridgetrail()
def rootTunnel():
    print("As you crawl through the roots, you hear goblin voices echoing from up ahead. A patrol.")
    print("You tuck yourself into a muddy crevice, barely daring to breathe as their filthy feet squelch past. One stops... sniffs... but moves on.")
    print("You’ve reached the outer edge of the goblin camp. Fires flicker, and goblins drink, fight, and howl.")
    print("You head towards to the biggest structure and what you think is the captain of the goblins.")
    print("You sneak in")
    print("You noctice the captain sleeping")
    print("You swiftly assinate the captain and you make your way out")
    print("Ending 3 achieved JOHN CENA")
    time.sleep(5)
    quit()
def ridgetrail():
    print("You proceed on with this wet and moist trail heading deeper and deeper in the goblin's lair")
    print("As you head closer towards the goblins a stray goblin noticed you")
    print("You however don't notice him and as a result he stabs you.")
    print("Ending 2 achieved TRASH AH DEATH")
    quit()

def Ethan():
    print("Welcome to pirate Adventure!")
    print("You are on a sandy beach, ready to explore.")
    while True:
        print("what do you do?")
        print("1. Search the beach")
        print("2. Go to the ship")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("You find a map to a treasure.")
            action = input("What do you do")
            if action == "search":
                print("You find the treasure now you use all that treasure to go home")
                break
        elif choice == "2":
                print("You head towards the ship")
                action = input("What to do on the ship. Print Sail.")
                if action == "sail":
                    print("The ship sails to a island")
                    print("On the island you find treasure")
                    print("full of gold")
                    print("you take all the treasure and went home")
                    break
                elif action == "home":
                    print("You decide to go home to your family")
                    break
                else:
                    print("I don't understand")
Start_Adventure()
print("Thanks for going through our adventure hope you enjoyed it")
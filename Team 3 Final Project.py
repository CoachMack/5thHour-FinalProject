#Names: Dom Acuna, Ethan Morris, Eli Hopkins, Quinn Dickey
#Team: 3
#Class: 5th Hour
#Assignment: Final Project

#Scrum Document: https://docs.google.com/document/d/1QlLv549T28qxmCLBgokRRFzVg8NNIGeDH-oDUunlrB8/edit?pli=1&tab=t.0

import random


def food_likes_you(food):
    return hash(food) % 2 == 0


foods = ["Pizza", "Burger", "Sushie", "Nachos", "Tacos", "Burritos", "Spagetti", "Lasagna",
         "Pie", "Icecream", "Hotdogs", "Chilidogs", "Cake", "Oatmeal", "Fish",
         "Chicken", "Shrimp", "Pancakes", "Cheesecake", "Popsicle", "Rice", "Noodles",
         "Skittles", "Oreos", "Peanut Butter", "Chocolate", "Peanut Brittle", "Apple", "Applesause",
         "Bannana", "Bacon", "Ham", "Jello", "Fishsticks", "Chicken Nuggets", "Fries", "Tater Tots", "Gum",
         "Turkey", "Potatos", "Mashed Potatos", "Corn On The Cob", "Bean", "Lolipop", "Bread", "Cornbread",
         "Sandwich", "Cheetos"]

matchlist = []

liked = []
disliked = []
matched = []

print("Welcome to Food Tinder! 🔮")
print("Type 'l' to like, 'd' to dislike, or 'q' to quit.\n")

def food_list_10():
    for x in range (10):
        match = random.choice(foods)
        matchlist.append(match)
        foods.remove(match)
food_list_10()
def food_match():
    for food in matchlist:
        while True:
            print(f"Do you like {food} 👀?")
            choice = input("[l]ike 👍🏽 / [d]islike 👎🏽 / [q]uit 🤚🏽: ").strip().lower()

            if choice == 'q':
                break
            elif choice == 'l':
                if food_likes_you(food):
                    matched.append(food)
                    print("It's a match! 🎉\n")
                else:
                    liked.append(food)
                    print(f"They swiped left... 😢\n")
                break
            elif choice == 'd':
                disliked.append(food)
                print(f"You swiped left 😈\n")
                break
            else:
                print("INVALID!! 🫦 Please type 'l', 'd', or 'q'.\n")
food_match()
print("\n=== Results ===")
print("💘 Matches:", matched)
print("👍 You liked:", liked)
print("👎 You disliked:", disliked)

if matched:
    print("\nWho would you like to go on a date with? 💕")
    for i, food in enumerate(matched):
        print(f"{i + 1}. {food}")

    while True:
        pick = input("Enter the number of your chosen food bae: ").strip()
        if pick.isdigit() and 1 <= int(pick) <= len(matched):
            chosen = matched[int(pick) - 1]
            print(f"\nYou and {chosen} are going on a romantic date! 🥂🍽️")
            break
        else:
            print("Pick a valid number from the list! 😤")
else:
    print("\nNo matches today... time to cry- 😢")

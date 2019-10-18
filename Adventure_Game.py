import time

import random


monster_list = ["troll", "cyclops", "minotaur"]
mst = random.choice(monster_list)  # mst is the monster variable


def print_pause(message, delay=0):
    print(message)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        for option in options:
            if option in choice:
                return choice
        print_pause("Sorry, I don't understand.")


def reconsidering(mst, items):
    print_pause("On second thougth, you decide to go\n", 2)
    print_pause("back inside the house and reevaluate.\n", 2)
    print_pause("You have suddently remembered that\n", 2)
    print_pause("you like having your head attached to your neck.\n", 2)
    print_pause("...But that poor woman. She really needs your help. \n", 2)
    fight_or_not(mst, items)


def fight_or_not(mst, items):
    fight_or_not = valid_input("Would you like to: "
                               "(1) fight or (2) run away?\n",
                               ["1", "2"])
    if '1' in fight_or_not:
        if "first" in items:
            first_choice_fight(mst)
        elif "second" in items:
            second_choice_fight(mst)
        elif "third" in items:
            third_choice_fight(mst)
    elif '2' in fight_or_not:
        reconsidering(mst, items)


def intro(mst):
    print_pause("You wake up in your bed at home to the desperate\n", 2)
    print_pause("screams for help from a woman outside your house!\n", 2)
    print_pause("You get up & crack the door open a bit to look outside\n", 2)
    print_pause("You see a " + mst + " violently roaring at a big tree,\n", 2)
    print_pause("& vigorously shaking it back-and-forth.\n", 2)
    print_pause("The woman you heard screeming\n", 2)
    print_pause("earlier is hanging on one of\n", 2)
    print_pause("the tree's top branches with a horrified expression.\n", 2)
    print_pause("You go in & shut the door before the creature sees you.\n", 2)
    print_pause("You are still wearing your pajamas,\n", 2)
    print_pause("and dont have a weapon at hand.\n", 2)
    print_pause("The house is dimly lit by the light coming\n", 2)
    print_pause("from the home's only window located in the attic.\n", 2)
    print_pause("Quickly you begin to consider what you'll do.\n\n\n", 4)


def first_choice(mst, items):
    print_pause("You run outside on your pajamas with nothing\n", 2)
    print_pause("but your bare hands to defend yourself and others.\n", 2)
    print_pause("The " + mst + " takes a quick look at you and\n", 2)
    print_pause("begins to laugh loudly and uncontrollably.\n", 2)
    print_pause("Suddently, he stops laughing.\n", 2)
    print_pause("His face, now full of hate\n", 2)
    print_pause("is squared directly at you with violent anticipation.\n", 4)
    fight_or_not(mst, items)


def second_choice(mst, items):
    print_pause("Quickly, you pick up your grandfather's\n", 2)
    print_pause("sword and shield\n", 2)
    print_pause("hanging on the wall, hoping to defeat\n", 2)
    print_pause("the beast with them.\n", 2)
    print_pause("You run out & head for the " + mst + ",\n", 2)
    print_pause("ready to strike.\n", 2)
    print_pause("The " + mst + " sees you & picks up a massive bludgeon\n", 2)
    print_pause("he had behind the tree, made from a broken tree branch.\n", 2)
    print_pause("He turns to you and raises his weapon ready for combat.\n", 4)
    fight_or_not(mst, items)


def third_choice(mst, items):
    print_pause("You quickly get some matches\n", 2)
    print_pause("& a candle from the kitchen.\n", 2)
    print_pause("You light the candle and\n", 2)
    print_pause("head straight for the basement.\n", 2)
    print_pause("There in a corner you find\n", 2)
    print_pause("what you've been looking for:\n", 2)
    print_pause("a very old chest. With the candle\n", 2)
    print_pause("in one hand, you search\n", 2)
    print_pause("the chest for an item your grandfather left you before\n", 2)
    print_pause("he past away. You quickly find it. It is a wooden staff\n", 2)
    print_pause("with a dark green, egg shaped stone\n", 2)
    print_pause("cradled on its head.\n", 2)
    print_pause("No time to waste. You reach the top floor in two jumps.\n", 2)
    print_pause("You burst thru the door & toward the " + mst + ".\n", 4)
    fight_or_not(mst, items)


def first_choice_fight(mst):
    print_pause("The " + mst + " starts to run towards you...\n", 2)
    print_pause("this doesn't look good.\n", 2)
    print_pause("With one hand he lifts you from the ground\n", 2)
    print_pause("& swallows you whole.\n", 2)
    print_pause("The End.\n", 4)


def second_choice_fight(mst):
    print_pause("You & the " + mst + " run towards each other...\n", 2)
    print_pause("weapons in hand.\n", 2)
    print_pause("A battle between you begins. Trading blows repeatedly.\n", 2)
    print_pause("Out of the corner of your eye you notice something.\n", 2)
    print_pause("You see the woman got off the tree,\n", 2)
    print_pause("& is now running away.\n", 2)
    print_pause("As the battle continues, you hope to at least\n", 2)
    print_pause("help her escape, perhaps at\n", 2)
    print_pause("the expense of your own life.\n", 2)
    print_pause("You are badly injured and fatigued... This is it.\n", 2)
    print_pause("With one final blow,\n", 2)
    print_pause("the " + mst + " defeats you, forever.\n", 4)


def third_choice_fight(mst):
    print_pause("You aim the staff at the beast; but then you notice.\n", 2)
    print_pause("The " + mst + " knocked the woman off the tree.\n", 2)
    print_pause("No time left.\n", 2)
    print_pause("Then you remember the right spell:\n", 2)
    print_pause("'begone foul beast!'.\n", 2)
    print_pause("A bright green bolt of light shoots out of the staff\n", 2)
    print_pause("& hits the ground under the " + mst + ".\n", 2)
    print_pause("Two thick & tall vines spring\n", 2)
    print_pause("from the ground and begin to\n", 2)
    print_pause("wip the " + mst + " . Horrified with fear, the beast\n", 2)
    print_pause("tries to escape, but is chased away by dozens of vines\n", 2)
    print_pause("sprouting from the ground until\n", 2)
    print_pause("he dissapears in the distance.\n", 2)
    print_pause("The threat now eliminated you discover the woman\n", 2)
    print_pause("is unharmed, save for a few bruises from the fall.\n", 2)
    print_pause("She is grateful for saving her.\n", 2)
    print_pause("You offer to escort her back to her village\n", 2)
    print_pause("...just in case ;)\n", 4)


def choices(mst, items):
    print_pause("Enter (1) to run outside and try to\n", 1)
    print_pause("help the poor screaming woman.\n\n", 4)
    print_pause("Enter (2) to look around the room for\n", 1)
    print_pause("a weapon you can use to defend the woman.\n\n", 4)
    print_pause("Enter (3) to light a candle to more\n", 1)
    print_pause("effectively search for a weapon inside the house.\n\n", 4)
    choice = valid_input("1. SAVE HER NOW!!!\n"
                         "2. Quick look around first.\n"
                         "3. Take the time to find the best weapon.\n",
                         ["1", "2", "3"])
    if '1' in choice:
        items.append("first")
        first_choice(mst, items)
    elif '2' in choice:
        items.append("second")
        second_choice(mst, items)
    elif '3' in choice:
        items.append("third")
        third_choice(mst, items)


def play_again():
    response = valid_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n",
                           ["yes", "no"])
    if "no" in response:
        print_pause("OK, goodbye!", 2)
        False  # Returns False if player entered "no" in response
    elif "yes" in response:
        print_pause("Very good, let's play again.\n", 2)
        play_game()


def play_game():
    items = []
    intro(mst)
    choices(mst, items)
    while True:
        if not play_again():  # If play_again returns False, exits
            break


play_game()

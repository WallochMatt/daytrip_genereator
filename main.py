
import random

list_of_destinations = ["park", "waterpark", "arcade", "bar", "Medieval Times"]
list_of_transports = ["car", "Uber", "carriage", "bike", "unicorn"]
list_of_entertainment = ["watch a movie", "go jet skiing", "hit the range", "LARP", "play D&D"]
list_of_restaurants = ["Kyoto Sushi", "Tanpopo Ramen", "Maharaja", "Culver's", "Bel Air Cantina"]

master_list = [list_of_destinations, list_of_transports, list_of_entertainment, list_of_restaurants]

def select_choice(list, previous_value):
    new_value = random.choice(list)
    if previous_value == new_value:
        return select_choice(list, previous_value)
    return new_value

def trip_start(complete):
    trip_maker = [select_choice(list_of_destinations, ""), select_choice(list_of_transports, ""),select_choice(list_of_entertainment, ""), select_choice(list_of_restaurants, "")]

    while complete is False:
       
        if primes_trip(trip_maker) == 0: #YES
            print(f"\n Great! Have fun on your trip to the {trip_maker[0]}, by way of {trip_maker[1]} where you can stop to {trip_maker[2]} and eat at {trip_maker[3]}.")
            return True

        elif 1: #NO
            reroll_trip(trip_maker)

def primes_trip(trip_maker):
     print(f"\n How about a trip to the {trip_maker[0]}, by way of {trip_maker[1]} where we can stop to {trip_maker[2]} and eat at {trip_maker[3]}.")
     trip_yes = int(input("\n Would you like to go on this trip? \n YES: 0 \n NO: 1 \n Choice: "))
     return trip_yes


def reroll_trip(trip_maker):
    print("Lets see what we can change... \n")
    for index in range (len(trip_maker)): 
        happy = int(input(f"How does {trip_maker[index]} sound?: ")) 
            
        if happy == 0: #YES
            pass

        elif happy == 1: #NO
            trip_maker[index] = select_choice(master_list[index], trip_maker[index])
                
trip_start(False)

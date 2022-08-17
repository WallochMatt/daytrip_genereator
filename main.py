
import random

list_of_destinations = ["park", "waterpark", "arcade", "bar", "Medieval Times"]
list_of_restaurants = ["Kyoto Sushi", "Tanpopo Ramen", "Mah Raja", "Culver's", "Bel Air Cantina"]
list_of_transports = ["car", "Uber", "carriage", "bike", "unicorn"]
list_of_entertainment = ["watch a movie", "go jet skiing", "hit the range", "LARP", "play D&D"]

master_list = [list_of_destinations, list_of_restaurants, list_of_transports, list_of_entertainment]

def select_choice(list, previous_value):
    new_value = random.choice(list)
    if previous_value == new_value:
        return select_choice(list, previous_value)
    return new_value
trip_maker = [select_choice(list_of_destinations, ""), select_choice(list_of_transports, ""),select_choice(list_of_entertainment, ""), select_choice(list_of_restaurants, "")] # need ()?

                                                #   ^  Empty string indicating previous value, which goes in empty, checks only after initial fill in the functio

complete = False

while not complete:
    print(f"How about a trip to the {trip_maker[0]}, by way of {trip_maker[1]} where we can stop to {trip_maker[2]} and eat at {trip_maker[3]}.")
    for index in range (len(trip_maker)):
        happy = int(input(f"How does {trip_maker[index]} sound?: ")) #make happy a one time check, then check specifics 
        
        if happy == 0: #YES
            pass
        if happy == 1: #NO
            trip_maker[index] = select_choice(master_list[index], trip_maker[index])
            






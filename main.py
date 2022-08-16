
import random

list_of_destinations = ["park", "waterpark", "arcade", "bar", "Medieval Times"]
list_of_restaurants = ["Kyoto Sushi", "Tanpopo Ramen", "Mah Raja", "Culver's", "Bel Air Cantina"]
list_of_transports = ["car", "Uber", "carriage", "bike", "unicorn"]
list_of_entertainment = ["watch a movie", "go jet skiing", "hit the range", "LARP", "play D&D"]

temporary_check = "" #this is part of my copy prevention/exclusion

def select_choice(list, previous_value):#i might be able to set a parameter for the index, so the function will rerun if it chooses the index, ie repeated choice
    new_value = random.choice(list)
    if previous_value == new_value:
        #temporary_check = rand_destin #second part of excluding disliked option
        return select_choice(list, previous_value)#may need to remove or change argument back in here
    return new_value

#if I have time I could create a default parameter
master_list = [select_choice(list_of_destinations, ""), select_choice(list_of_transports, ""),select_choice(list_of_entertainment, ""), select_choice(list_of_restaurants, "")] # need ()?
complete = False

while not complete:
    print(f"How about a trip to the {master_list[0]}, by way of {master_list[1]} where we can stop to {master_list[2]} and eat at {master_list[3]}.")
    for index in master_list:
        happy = int(input("How does that sound?: "))
        if happy == 0: #YES
            pass
        if happy == 1: #NO
            temporary_check = index #probably do not need temp check anymore






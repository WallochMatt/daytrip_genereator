
import random

list_of_destinations = ["park", "waterpark", "arcade", "bar", "Medieval Times"]
list_of_restaurants = ["Kyoto Sushi", "Tanpopo Ramen", "Mah Raja", "Culver's", "Bel Air Cantina"]
list_of_transports = ["car", "Uber", "carriage", "bike", "unicorn"]
list_of_entertainment = ["watch a movie", "go jet skiing", "hit the range", "LARP", "play D&D"]

temporary_check = ""

def gives_destination(temporary_check):#i might be able to set a parameter for the index, so the function will rerun if it chooses the index, ie repeated choice
    rand_destin = random.choice(list_of_destinations)
    if temporary_check == rand_destin:
        gives_destination(index)
    return rand_destin  

def gives_restaurants():
    rand_resta = random.choice(list_of_restaurants)
    return rand_resta

def gives_transport():
    rand_transp = random.choice(list_of_transports)
    return rand_transp

def gives_entertainment():
    rand_ent = random.choice(list_of_entertainment)
    return rand_ent

master_list = [gives_destination(), gives_transport(), gives_entertainment(), gives_restaurants()] # need ()?

print(f"How about a trip to the {master_list[0]}, by way of {master_list[1]} where we can stop to {master_list[2]} and eat at {master_list[3]}.")
#keep in mind I changed these since the previous repo
#print(f"How about a trip to the {gives_destination()}, by way of {gives_transport()} where we can stop to {gives_entertainment()} and eat at {gives_restaurants()}.")

#Probably going to need a while loop
# for index in master_list:#good
#     #backup_index = index
#     happy = int(input(f"Are you happy with {index}?"))


        # if index == 0:
        #     gives_destination
        # if index == 1:
        #     gives_transport
        # if index == 2:
        #     gives_entertainment
        # if index == 3:
        #     gives_restaurants

    # if happy == 1:#YES
    #     pass
    # if happy == 0:#NO
    #     index = backup_index
complete = 0

while complete < 1:
    for index in master_list:
        happy = int(input(""))
        if happy == 1:
            pass
        elif happy == 0:
            temporary_check = index #trying to send this back into the function







import random
#randchoices and their list should become functions
#4+ items in lists
list_of_destinations = ["park", "waterpark", "arcade", "bar", "Medieval Times"]
list_of_restaurants = ["Kyoto Sushi", "Tanpopo Ramen", "Mah Raja", "Culver's", "Bel Air Cantina"]
list_of_transports = ["car", "Uber", "carriage", "bike", "unicorn"]
list_of_entertainment = ["watch a movie", "go jet skiing", "hit the range", "LARP", "play D&D"]

rand_destin = random.choice(list_of_destinations)
rand_resta = random.choice(list_of_restaurants)
rand_transp = random.choice(list_of_transports)
rand_ent = random.choice(list_of_entertainment)

# print(rand_destin)
# print(rand_resta)
# print(rand_transp)
# print(rand_ent)

#print(f"How about a trip to the {rand_destin}, by way of {rand_transp} where we can stop to {rand_ent} and eat at {rand_resta}.")

# user_input = 0 #WOnt be able to pick and choose parts
# while user_input != 1:
#     print(f"How about a trip to the {rand_destin}, by way of {rand_transp} where we can stop to {rand_ent} and eat at {rand_resta}.")
#     choice = input(("How does that sound? Y/N ?: "))
#     if choice.lower == "y":
#         print("GREAT!")
#         user_input += 1
#     elif choice.lower == "n":
#         print("Lets find something else!")
#     else:
#         pass


#could try a for loop tht confimrs each choice?
#might need a temp value for confrimin a trip as complete so i can store a copy of the trip, otherwise its  apt to be overwritten
# happy = int(input("1 yess 0 no"))
# if happy == 1:
#     print("YOUR TRIP IS ")#^you could use numbersa for more accurate user input selection
# elif happy == 0:
#     answer = int(input("WHat dont you like?: 1 2 3 4")) # FOR LOOP?
#     #print("whats is wrong?")
#     if answer == 1:
#         rand_destin#rerolll
#     if answer == 2:
#         print(rand_resta)
#     if answer == 3:
#         rand_transp
#     if answer == 4:
#         rand_ent



        # temp = index
        # new_index = index
        # index = new_index #wrong order could help
        # print(index)

master_list = [rand_destin, rand_resta, rand_transp, rand_ent]

#final_choice_list = []

print(f"How about a trip to the {master_list[0]}, by way of {master_list[2]} where we can stop to {master_list[3]} and eat at {master_list[1]}.")#good

for index in master_list:#good
    happy = int(input(f"Are you happy with {index}?"))
    counter = 0
    if happy == 1:#YES
        pass
    if happy == 0:#NO
        pass
        # new_index = master_list[]
        # index = new_index

import random
#4+ items in lists
list_of_destinations = ["park", "waterpark", "arcade", "bar", "Medieval Times"]
list_of_restaurants = ["Kyoto Sushi", "Tanpopo Ramen", "Mah Raja", "Culver's", "Bel Air Cantina"]
list_of_transports = ["car", "Uber", "carriage", "bike", "unicorn"]
list_of_entertainment = ["watch a movie", " go jet skiing", "hit the range", "LARP", "play D&D"]

rand_destin = random.choice(list_of_destinations)
rand_resta = random.choice(list_of_restaurants)
rand_transp = random.choice(list_of_transports)
rand_ent = random.choice(list_of_entertainment)

# print(rand_destin)
# print(rand_resta)
# print(rand_transp)
# print(rand_ent)

print(f"How about a trip to the {rand_destin}, by way of {rand_transp} where we can stop to {rand_ent} and eat at {rand_resta}.")
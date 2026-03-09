""" You will be creating a little store in your terminal. You will have a list of
dictionaries that will be displayed to the user. Each Dictionary will have at
least 3 properties (name, price and whatever you want)
PART ONE:
The user will select one item to purchase. You will then show the user
ONLY the name of the item they purchased. You will need to use the item
index to accomplish this task. """

""" legions = [
     { "name":"dark angels", "alliegence" : "loyal", "primarch": "lion"},
     {"name": "emperor's children", "alliegence": "traitor", "primarch": "fulgrim"},
     { "name": "iron warriors", "alliegence": "traitor", "primarch" : " perturabo"},
     {"name" : "salamanders","alliegence" : "loyal", "primarch" : "vulkan",}, 
     { "name":"white scars", "alliegence" : "loyal", "primarch": "jaghatai"},
     { "name":"space wolves", "alliegence" : "loyal", "primarch": "russ"},
     { "name":"imperial fists", "alliegence" : "loyal", "primarch": "dorn"},
     { "name":"night lords", "alliegence" : "traitor", "primarch": "curze"},
     { "name":"blood angels", "alliegence" : "loyal", "primarch": "sanguinius"},
     { "name":"iron hands", "alliegence" : "loyal", "primarch": "ferrus"}, 

]
# print(legions[0]["name"])
#angr, guil, mort, mag, hor, lorg, corv, alphi """
# i wrote all pf that forgetting we had to make  a store :(  
store = [
    {"name": "Dawnbringer", "weapon type": "hammer", "cost": 19999},
    {"name": "Oathbreaker", "weapon type": "hammer", "cost": 10400},
    {"name": "the W.M.'s Talons", "weapon type": "gauntlet", "cost":6799}, 
    {"name": "the Blade Encarmine", "weapon type": "sword", "cost":54050}, 
    {"name": "Fireblade", "weapon type": "sword", "cost":42900}, 
    {"name": "the Anathame", "weapon type": "EVIL blade", "cost": 75334}, 
    {"name": "Silence", "weapon type": "scythe", "cost":33300}, 
    {"name": "Storm's Voice", "weapon type": "ranged", "cost": 585}, 
    {"name": "a whetstone", "weapon type": "tool", "cost":1900}, 
    {"name": "the Blade of Laer", "weapon type": "EVIL sword", "cost":9600},  
]
# chosen = int(input("Input the number corresponding to the item would you like to purchase:"))
# ACTIVITY 1 
""" def shop():
    print("Welcome! Here is what is in stock today..")
    for index, item in enumerate(store):
            print(index, ":", item["name"])
    chosen = int(input("Input the number corresponding to the item would you like to purchase:"))
    print("You are purchasing a/the", store[chosen]["name"])

shop() """

#ACTIVITY 2 
cart = [] 
def shop():
        ct = []
        cs = 0.0
        print("Welcome! Here is what is in stock today..")
        for index, item in enumerate(store):
            print(index, ":", item["name"])
        chosen = int(input("Input the number corresponding to the item would you like to purchase:"))
        cart.append(chosen)
        ct.append(store[chosen]["cost"])
        print("You are purchasing", store[chosen]["name"], "for", store[chosen]["cost"],"TG.")
        while input("Would you like to continue shopping?:") in ("Yes","yes","y","YES", "yES", "yeS", "YeS"):
        #     for index, item in enumerate(store):
        #         print(index, ":", item["name"])
                chosen = int(input("Input the number corresponding to the item would you like to purchase:"))
                print("You are currently purchasing", store[chosen]["name"], "for", store[chosen]["cost"],"TG.")
                cart.append(chosen)
                ct.append(int(store[chosen]["cost"]))
        # print("Your cart contains.." )
        # for index, item in enumerate(cart):
        #     print(index, ":", item["name"])
        print("Thank you for shopping with us! You are purchasing items corresponding with numbers/number ", cart, "for a total of", sum(ct),"." )

shop()
# def make_pizza(*toppings, *base): ---This is not possible
# multiple *args parameters are not possible
def make_pizza(*toppings, base):
    print(toppings, base)


#    for toping in toppings:
#       print(toping)


Lily = make_pizza("Tomato", base="thin")
Mayuri = make_pizza("Corns", "oninon", "pinapple", base="chesse burst")
vinee = make_pizza("onion", "paneer", "chilli", "mashrooms", "olives", base="wheat")

#  Return multiple things in python
def make_pizza(*toppings, base="Wheat"):
    #    print(toppings, base)
    for topping in toppings:
        print(topping)
    return toppings, base


Swathi_t, Swathi_b = make_pizza("olive", "onion", "tomato")
Mayuri = make_pizza("Corns", "Paneer", base="cheese burst")
print(Swathi_t)
print(Swathi_b)
print(Mayuri)

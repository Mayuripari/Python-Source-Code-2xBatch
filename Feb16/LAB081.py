# Dictionary
# Dict- key value pair, unordered
# e.g. name = "Mayuri"
# key- name, value-Mayri
my_dict = {}
my_dict2 = dict()
print(my_dict)
print(my_dict2)

phonebook = {"Mayuri": 8987462920, "Batman": 1234567890, "wonder": 927392020200}
print(phonebook)
print(phonebook["Batman"])
print(len(phonebook))

phonebook2 = dict(batman=123, Cersei=324, GB=323)
print(phonebook2["GB"])
print(phonebook2['GB'])
print(phonebook2.get("GB"))
print(phonebook2.get('GB'))


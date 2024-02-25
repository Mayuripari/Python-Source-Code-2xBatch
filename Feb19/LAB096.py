# multiple parameter class - used arguments here so not used self to call the variables/param
class multi_param:
    def print_info(self, first_name, last_name, age):
        print("Your name is ", first_name, last_name, age)
    # we r not using self coz we r calling arguments- first name, last name, age


objref = multi_param()
Mayuri = objref.print_info("Mayuri", "Parit", 15)
Mita = objref.print_info("Mita", "K", 17)

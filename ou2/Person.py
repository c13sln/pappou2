def set_father(name):
    retname = name
    return retname


def set_mother(name):
    retname = name
    return retname


def set_first_name(name):
    first_name = name
    return first_name


def set_last_name(name):
    last_name = name
    return last_name


def set_date_of_birth(date):
    date_of_birth = date
    return date_of_birth


def set_date_of_death(date):
    date_of_death = date
    return date_of_death


father = set_father("Stefan")
mother = set_mother("Helén")
first_name = set_first_name("Sebastian")
last_name = set_last_name("Lundgren")
date_of_birth = set_date_of_birth("1993-04-14")

print("Name is: " + first_name + " " + last_name + " born: " + date_of_birth +" father is: " + father + " and mother is: " + mother)

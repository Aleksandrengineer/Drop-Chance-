import random

count = 0
swords = 0
shields = 0
staffs = 0
keys = 0
number_of_chests = 1000
while count < number_of_chests:
    count = count + 1
    random.seed(random.randint(0, 69420))
    random_number = random.random()
    if random_number < 0.4:
        swords = swords + 1
    elif random_number > 0.4 and random_number < 0.7:
        shields = shields + 1
    elif random_number > 0.7 and random_number < 0.9:
        staffs = staffs + 1
    elif random_number > 0.9:
        keys = keys + 1

print ("Number of Swords -", swords, "\nNumber of shields -", shields, "\nNumber of Staffs - ", staffs, "\nNumber of Keys - ", keys)
value_of_swords = swords * 1.5 * 2
value_of_shields = shields * 1.5 * 3
value_of_staffs = staffs * 1.5 * 5
value_of_keys = keys * 1 * 50
overall_value = value_of_keys+value_of_shields+value_of_staffs+value_of_swords
print("The overall value will be ", overall_value)
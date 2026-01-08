#The hotel's IT system contains a list of reserved rooms.
#The data is contained in the reservations.json file. 
#Write a program that prints the summary information as stated below.
#Break your program into smaller parts defining functions.

#number of rooms
#number of paid reservations
#number of unpaid reservations
#total value of paid reservations
#total value of unpaid reservations

import json

def number_of_rooms(reservations):
    return len(reservations)

def number_of_paid(reservations, is_paid_status):
    count = 0
    value = 0

    for room in reservations:

        if room["paid"] == is_paid_status:
            count += 1
            value = room["price_per_night"] * room["nights"]
            

    return count, value

def number_of_unpaid(reservations, isnt_paid_status):
    count = 0
    value = 0

    for room in reservations:
        if room["paid"] == isnt_paid_status:
            count += 1
            value += room["price_per_night"] * room["nights"]

    return count, value


filename = 'reservations.json'

with open(filename, 'r', encoding="utf-8") as file:
    data = json.load(file)

    content = data["reservations"]

    

    total_rooms = number_of_rooms(content)

    paid_count, paid_value = number_of_paid(content, True)

    unpaid_count, unpaid_value = number_of_unpaid(content, False)


print(f"Number of rooms: {total_rooms}")
print(f"Number of paid reservations: {paid_count}")
print(f"Number of unpaid reservations: {unpaid_count}")
print(f"Total value of paid reservations: {paid_value}")
print(f"Total value of unpaid reservations: {unpaid_value}")
        
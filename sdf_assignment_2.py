"""
Description: Assignment 2: Intro to Python
Author: Gavin Simon
Date: 09/22/2024
"""

#SIMPLE DATA TYPES

#type() function displays data types

name = "gavin"
print("name:", name, "type:",type(name))

driver_license = True
print("value:", driver_license, "type:", type(driver_license))

current_year = 2024
print("this year:", current_year, "type:", type(current_year))

current_year += 1
print("next year:", current_year, "type:", type(current_year))


#CALCULATIONS


# Declaring variables
GST = 0.05
PST = 0.07
vehicle = 70645.80

# Tax calculations
gst_cost = vehicle * GST
pst_cost = vehicle * PST
final_cost = vehicle + pst_cost + gst_cost

#printing results. Second print uses f string format it better.
# : after variable to format
# , adds commas to seperate thousands (1,000)
# .2f formats float to only display 2 decimal places

print("Pre-tax value:", vehicle, "Provincial Tax:", pst_cost, "Federal Tax:", gst_cost, "Total:", final_cost)
print(f"Pre-tax value: ${vehicle:,.2f} Provincial Tax: ${pst_cost:,.2f} Federal Tax: ${gst_cost:,.2f} Total: ${final_cost:,.2f}")

#LISTS

#Declaring and confirming list datatype
pumpkin_spice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(pumpkin_spice))

# adding name into list
pumpkin_spice.insert(6, "Gavin")
print(pumpkin_spice)

pumpkin_spice.pop(9)
print(pumpkin_spice)

chai_tea = ["A", "B", "C"]
london_fog = pumpkin_spice + chai_tea
print(london_fog)


#TUPLES

provinces = ("Manitoba", "Ontario", "Alberta", "QUebec")
print(type(provinces))
print(provinces)

#DICTIONARIES

currency = {'Nickle': 0.05, 'Dime': 0.10, 'Quarter': 0.25, 'Loonie': 100, 'Toonie': 200}
print(type(currency))
print(currency)

currency["nickle"] = 5
currency["dime"] = 10
currency["Quarter"] = 25
print(currency)

#SETS

multiples_of_two = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
print(type(multiples_of_two))
print(multiples_of_two)

multiples_of_five = {5, 10, 15, 20}
print(multiples_of_five)

unique_values = multiples_of_two.union(multiples_of_five)
print(unique_values)

shared_values = multiples_of_five.intersection(multiples_of_two)
print(shared_values)

only_in_multiples_of_two = multiples_of_two.difference(multiples_of_five)
print(only_in_multiples_of_two)

only_in_multiples_of_five = multiples_of_five.difference(multiples_of_two)
print(only_in_multiples_of_five)
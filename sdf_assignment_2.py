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


# Declaring variabels
GST = 0.05
PST = 0.07
vehicle = 70645.80

# Tax calculations
gst_cost = vehicle*GST
pst_cost = vehicle*PST
final_cost = vehicle+pst_cost+gst_cost

#printing results. Second print uses f string format it better.
# : after variable to format
# , adds commas to seperate thousands (1,000)
# .2f formats float to only display 2 decimal places

print("Pre-tax value:", vehicle, "Provincial Tax:", pst_cost, "Federal Tax:", gst_cost, "Total:", final_cost)
print(f"Pre-tax value: ${vehicle:,.2f} Provincial Tax: ${pst_cost:,.2f} Federal Tax: ${gst_cost:,.2f} Total: ${final_cost:,.2f}")

#LISTS

#TUPLES

#DICTIONARIES

#SETS

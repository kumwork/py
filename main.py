from kedar import validate_and_execute
""" 
from kedar import *
import kedar as h 
import kedar """



user_input = ""
while user_input != "exit":
    user_input = input("hey user, enter the number of days\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))
    for num_of_days_element in set(user_input.split(", ")):
       validate_and_execute(num_of_days_element)

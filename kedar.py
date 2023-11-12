calculations_to_seconds = 24*60*60
name_of_the_unit = "seconds"
def days_to_units(num_of_days):
    print(f"{num_of_days} days are  {num_of_days * 24}")
    condition_check = num_of_days > 0
    if num_of_days > 0:
        return f"{num_of_days} days in {num_of_days * calculations_to_seconds } {name_of_the_unit}"
    elif num_of_days == 0:
        return f"{num_of_days} is zero please type in positive number"
    else:
        return f"{num_of_days} is negative"

def validate_and_execute(num_of_days_element):
    try:
        user_input_number = int(num_of_days_element)
        # we want to do conversion only for positive integers
        if user_input_number > 0:
            answer = days_to_units(user_input_number)
            print(answer)
        elif user_input_number == 0:
            print ("You entered zero please type in positive number")
        else:
            print("u entered a negative number , please enter a positive number")

    except ValueError:
        print("ur input is not a positive number")

student_data = [
    {"name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow"},
    {"name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza"},
    {"name": "Julia", "hometown": "Houston", "favorite_food": "shrimp"}
]


# This function will enumerate through all students in student_data list
def list_names(student_data):
    for i, student in enumerate(student_data):
        print(f"{i + 1}. {student['name']}")


# This function will create prompts and add new student for the add option
def get_new_student():
    print("Please provide the following information for the new student:")
    new_name = input("Name: ")
    new_hometown = input("Hometown: ")
    new_favorite_food = input("Favorite Food: ")
    return student_data.append({"name": new_name, "hometown": new_hometown, "favorite_food": new_favorite_food})


# Loops through actions until user chooses to quit
while True:
    user_action = input("What would you like to do? View, Add or Quit: ")
    match user_action:
        case "Add":
            get_new_student()
        case "View":
            list_names(student_data)
            while True:
                total_sting = len(student_data)
                user_choice = int(input(f"Please select a student number (1 - {total_sting}): "))
                if 0 < user_choice <= total_sting:
                    while True:
                        chosen_student = student_data[user_choice - 1]
                        requested_info = input("Which category would you like to see? Hometown or Favorite Food: ")
                        match requested_info:
                            case "Hometown":
                                print("Hometown:", chosen_student["hometown"])
                                break
                            case "Favorite Food":
                                print("Favorite Food:", chosen_student["favorite_food"])
                                break
                            case _:
                                print("Sorry that choice wasn't valid. Please try again.")
                    break
                else:
                    print("Sorry the number selected isn't valid. Please try again")
        case "Quit":
            print("Thanks for playing. Goodbye!")
            break
        case _:
            print("Sorry the option you selected wasn't valid. Please try again.")




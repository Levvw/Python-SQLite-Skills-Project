input_message = """
 What do u want to do?
's' => Show all skills
'a' => Add new skill
'd' => Delete a skill
'u' => Update skill progress
'q' => Quit the app
Choose Option:
"""
user_input = input(input_message).strip().lower()
commands_list = ['s', 'a', 'd', 'u', 'q']
if user_input in commands_list:
    print(f"Command Entered {user_input}")
    if user_input == 's':
        show_skills()
    elif user_input == 'a':
        add_skills()
    elif user_input == 'd':
        delete_skills()
    elif user_input == 'u':
        update_skills()
    else:
        print("Program Closed")

else:
    print(f"sorry {user_input} command is not found")


def show_skills():
    pass


def add_skills():
    pass


def delete_skills():
    pass


def update_skills():
    pass

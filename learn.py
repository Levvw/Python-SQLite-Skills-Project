import sqlite3
db = sqlite3.connect("E:\Bodi\Python\skills.db")
cr = db.cursor()
uid = 1
# string formating isnt good for queries to prevent SQL injection
# but im doing it anyways for this one project
cr.execute(
    "create table if not exists skills (name text, progress text, user_id integer)")


def save_and_close():
    db.commit()
    db.close()
    print("DataBase connection is saved and closed")


def show_skills():
    cr.execute(f"select * from skills where user_id = {uid}")
    results = cr.fetchall()
    print(f"you have {len(results)} skill/s : ")
    if len(results) > 0:
        for row in results:
            print(f"skill => {row[0]}    Progress => {row[1]} ")

    save_and_close()


def add_skills():
    sk = input("Add a new Skill").strip().capitalize()
    prog = input(" write the progress of the skill").strip()
    cr.execute(
        f"insert into skills(name, progress, user_id) values('{sk}','{prog}','{uid}')")
    save_and_close()


def delete_skills():
    sk = input("Enter the skill name : ").strip().capitalize()
    cr.execute(
        f"delete from skills where name = '{sk}' and user_id = '{uid}' ")

    save_and_close()


def update_skills():
    sk = input("Write the new name of the Skill: ")
    prog = input("Write the new progress of the Skill: ")
    cr.execute(
        f"update skills set progress = '{prog}' where name = '{sk}' and '{uid}'")
    save_and_close()


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
        save_and_close()

else:
    print(f"sorry {user_input} command is not found")

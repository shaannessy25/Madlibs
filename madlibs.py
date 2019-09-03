# Got this madlib from hobbylark.com

def user_input():
    #Takes in all user inputs and stores them in a variable
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    a = [adjective, adjective2]
    verb = input("Enter a past tense verb: ")
    verb2 = input("Enter a verb: ")
    verb3 = input("Enter a verb ending with ing: ")
    verb4 = input("Enter a verb ending with ing: ")
    v = [verb, verb2, verb3, verb4]
    noun = input("Enter a noun: ")
    noun2 = input("Enter a plural noun: ")
    noun3 = input("Enter a noun: ")
    n = [noun, noun2, noun3]
    type_of_bird = input("Enter a type of bird: ")
    room = input("Enter a room: ")
    relative = input("Enter a relatives name: ")
    liquid = input("Enter a type of liquid: ")
    body_part = input("Enter a body part: ")
    # prints the madlib with variables
    print(f'''It was a {a[0]}, cold November day. I woke up to the {a[1]}\
 smell of {type_of_bird} roasting in the {room} downstairs. I {v[0]} down the stairs\
 to see if I could help {v[1]} the dinner. My mom said, 'See if {relative} needs a\
  fresh {n[0]}.' So I carried a tray of glasses full of {liquid} into the {v[2]}\
  {room}. When I got there, I could'nt believe my {body_part}! There were {n[1]}\
  {v[3]} on the {n[2]}! ''')


user_input()

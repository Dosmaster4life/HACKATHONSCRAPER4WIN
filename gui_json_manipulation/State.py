from tkinter import *
from xmlrpc.client import Boolean

# CONSTANTS
num_rows = 10
num_columns = 5 

#create a window
window = Tk()
window.title("Checkboxes")
window.geometry("1000x800")

# List of all US states
states = [
    'Alabama','Alaska','Arizona','Arkansas','California','Colorado',
    'Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho',
    'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
    'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
    'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
    'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
    'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee',
    'Texas','Utah','Vermont','Virginia','Washington','West Virginia',
    'Wisconsin','Wyoming'
    ]

states_dict = {
    'Alabama': [False, [0,0]],'Alaska': [False, [0,1]],
    'Arizona': [False, [0,2]],'Arkansas': [False, [0,3]],
    'California': [False, [0,4]],'Colorado': [False, [1,0]],
    'Connecticut': [False, [1,1]],'Delaware': [False, [1,2]],
    'Florida': [False, [1,3]],'Georgia': [False, [1,4]],
    'Hawaii': [False, [2,0]],'Idaho': [False, [2,1]],
    'Illinois': [False, [2,2]],'Indiana': [False, [2,3]],
    'Iowa': [False, [2,4]],'Kansas': [False, [3,0]],
    'Kentucky': [False, [3,1]],'Louisiana': [False, [3,2]],
    'Maine': [False, [3,3]],'Maryland': [False, [3,4]],
    'Massachusetts': [False, [4,0]],'Michigan': [False, [4,1]],
    'Minnesota': [False, [4,2]],'Mississippi': [False, [4,3]],
    'Missouri': [False, [4,4]],'Montana': [False, [5,0]],
    'Nebraska': [False, [5,1]],'Nevada': [False, [5,2]],
    'New Hampshire': [False, [5,3]],'New Jersey': [False, [5,4]],
    'New Mexico': [False, [6,0]],'New York': [False, [6,1]],
    'North Carolina': [False, [6,2]],'North Dakota': [False, [6,3]],
    'Ohio': [False, [6,4]],'Oklahoma': [False, [7,0]],
    'Oregon': [False, [7,1]],'Pennsylvania': [False, [7,2]],
    'Rhode Island': [False, [7,3]],'South Carolina': [False, [7,4]],
    'South Dakota': [False, [8,0]],'Tennessee': [False, [8,1]],
    'Texas': [False, [8,2]],'Utah': [False, [8,3]],
    'Vermont': [False, [8,4]],'Virginia': [False, [9,0]],
    'Washington': [False, [9,1]],'West Virginia': [False, [9,2]],
    'Wisconsin': [False, [9,3]],'Wyoming': [False, [9,4]]
    }

# for row in range(num_rows):
#     for column in range(num_columns):
#         index = num_columns * row + column
#         if list(states_dict.keys())[list(states_dict.values()).index(1)] == states[index]:
#             state_bool = BooleanVar()


# print("states_dict: ", states_dict)

"""
Grid of checkboxes for each state
"""

#create label that says "Target locations by:"
label = Label(window, text = "Target locations by:")
label.grid()

#create radio buttons
radio_button = Radiobutton(window, text = "None", value = 1)
radio_button1 = Radiobutton(window, text = "State", value = 2)
radio_button2 = Radiobutton(window, text = "City", value = 3)
radio_button3 = Radiobutton(window, text = "County", value = 4)
radio_button.grid(row = 0, column = 1)
radio_button1.grid(row = 0, column = 2)
radio_button2.grid(row = 0, column = 3)
radio_button3.grid(row = 0, column = 4)

"""
Select all states 
"""

#create a checkbox to select all checkboxes
# check_all = Checkbutton(window, text = "Select all")
# check_all.grid()

#move checkboxes down 1 row to make room for the select all checkbox
for row in range(num_rows):
    for column in range(num_columns):
        index = num_columns * row + column
        state = states[index]
        #create a checkbox for each state and set each checkbox to a variable
        checkbox = Checkbutton(window, text = state, variable = states[index])
        checkbox.grid(row = row + 1, column = column)
        checkbox.grid(sticky = W)

# # align checkbuttons to the left
# for row in range(num_rows):
#     for column in range(num_columns):
#         index = num_columns * row + column
#         state = states[index]
#         state.grid(sticky = W)

# def select_all():
#     for row in range(num_rows):
#         for column in range(num_columns):
#             index = num_columns * row + column
#             state.set(state_bools[index]) # Change state_bools to states_dict

#if the select all button is clicked, all checkboxes are selected
# check_all.config(command = select_all)

# Checkbutton(window, text = "Select all", command = select_all, variable = state_bools[index]).grid()

#track which checkboxes are checked
# def check():
#     if check_all.get() == 1:
#         for state in states:
#             state.select()
#     else:
#         for state in states:
#             state.deselect()


mainloop()
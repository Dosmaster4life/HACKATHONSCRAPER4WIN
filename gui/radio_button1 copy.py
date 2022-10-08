#create 5 columns with 10 checkboxes in each column

from tkinter import *
#create a window
window = Tk()
window.title("Checkboxes")
window.geometry("1000x800")

states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

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

#create a checkbox to select all checkboxes
check_all = Checkbutton(window, text = "Select all")
check_all.grid()

num_rows = 10
num_columns = 5 

#move checkboxes down 1 row to make room for the select all checkbox
for row in range(num_rows):
    for column in range(num_columns):
        index = num_columns * row + column
        state = states[index]
        #create a checkbox for each state and set each checkbox to a variable
        state = Checkbutton(window, text = state)
        state.grid(row = row + 1, column = column)


        # Checkbutton(window, text = state).grid(row = row + 2, column = column, sticky = W)

#create a select all button
def select_all():
    for row in range(num_rows):
        for column in range(num_columns):
            index = num_columns * row + column
            state = states[index]
            state.select()


#if the select all button is clicked, all checkboxes are selected
check_all.config(command = select_all)

Checkbutton(window, text = "Select all", command = select_all).grid()

#track which checkboxes are checked
# def check():
#     if check_all.get() == 1:
#         for state in states:
#             state.select()
#     else:
#         for state in states:
#             state.deselect()


mainloop()


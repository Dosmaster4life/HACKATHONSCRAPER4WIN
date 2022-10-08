#create 5 columns with 10 checkboxes in each column
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.ttk import Labelframe
import pandas as pd

#create a window
window = Tk()
window.title("Checkboxes")
window.geometry("1000x800")
# window.eval('tk::PlaceWindow . center')

center = LabelFrame(window, borderwidth=0, highlightthickness=0)
center.grid(row=0, column=0)
center.place(anchor="c", relx=.5, rely=.5)

top = LabelFrame(center, borderwidth=0, highlightthickness=0)
top.grid(column=0, row=0)

# title of program
title_label = Label(top, text="Pitch 59 Business Contact Scraper", font=("Arial Bold", 20))
title_label.grid(column=0, row=0, columnspan=5, pady=10)

## search text label/instructions
search_text_lf = LabelFrame(top, borderwidth=0, highlightthickness=0)
search_text_lf.grid(column=0, row=1, pady=5)

## search label
search_label = Label(search_text_lf, text="Enter business name or type: ", font=("Arial Bold", 15))
search_label.grid(column=0, row=0)

##search instructions
search_instructions = Label(search_text_lf, text="(separate multiple search queries by a comma)", font=("Arial", 10))
search_instructions.grid(column=0, row=1)

# search entry
search_entry = Entry(top, bd=5, width=50)
search_entry.grid(column=1, row=1)

# or label
or_label = Label(top, text="or")
or_label.grid(column=0, row=2, columnspan=5, pady=5)



    
   

def import_file():
        global file_display
        global filename
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("csv files", "*.csv"), ("all files", "*.*")))
        
        df = pd.read_csv(filename)
        file_display = Label(top, text=filename)
        file_display.grid(column=1, row=4)

        global csv_list 
        csv_list = df.values.tolist()
    #create global varilist from csv with pandas
    
    # csv_list = df.values.tolist()

# upload button that returns the list of csv values
import_file_button = Button(top, text="Upload csv file", command=import_file)
import_file_button.grid(column=0, row=3, columnspan=5, pady=10)

## clear upload button and file display
#clear = LabelFrame(top, borderwidth=0, highlightthickness=0)
#clear.grid(column=0, row=4, pady=5)


## clear button
#clear_button = Button(clear, text="Clear", command=import_file)
#clear_button.grid(column=0, row=0, pady=10)



### max results
max_results = LabelFrame(center, borderwidth=0, highlightthickness=0)
max_results.grid(column=0, row=1, pady=10)

### max results label
max_results_label = Label(max_results, text="Max results per query: ")
# change column locations
max_results_label.grid(column = 0, row=0, pady=10)

def validate_entry(value):
    try:
        # print(chr(value))
        if int(value) > 0:
            return value
        #else if value is a backspace, return value
        elif chr(value) == "\b":
            return value
        else:
            return False
    except ValueError:
        return value == ''

max_results_entry = Entry(max_results, bd =5)
max_results_entry.grid(column=1, row=0, pady=10)
max_results_entry.config(validate="key", validatecommand=(window.register(validate_entry), '%P'))

#### start button
def start_info():

    #return csv_list if not empty
        global csv_list
        if csv_list:
            flattened_list = [item for sublist in csv_list for item in sublist]
            print(flattened_list)
        else:
            #return list of entered variables
            search_text = search_entry.get()
            #make list from search_text
            search_text_list = search_text.split(",")
            #remove whitespace from list
            search_text_list = [x.strip() for x in search_text_list]
            csv_list = search_text_list

        global max_results
        max_results = max_results_entry.get()
        print(max_results)
    

start = LabelFrame(center, borderwidth=0, highlightthickness=0)
start.grid(column=0, row=2, pady=10)

start_button = Button(start, text="Start", command=start_info)
start_button.grid(column=0, row=0, pady=10)


mainloop()
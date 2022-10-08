from tkinter import *
from tkinter import ttk

# CONSTANTS
num_rows = 10
num_columns = 5

class App(Tk):
    def __init__(self):
        super().__init__()

        #create a window
        self.title("Checkboxes")
        self.geometry("1000x800")

        style = ttk.Style(self)

        # Create a reference to the checkbox boolean value for each state
        # AL-GA
        AL_bool = BooleanVar()
        AK_bool = BooleanVar()
        AZ_bool = BooleanVar()
        AR_bool = BooleanVar()
        CA_bool = BooleanVar()
        CO_bool = BooleanVar()
        CT_bool = BooleanVar()
        DE_bool = BooleanVar()
        FL_bool = BooleanVar()
        GA_bool = BooleanVar()
        # HI-MD
        HI_bool = BooleanVar()
        ID_bool = BooleanVar()
        IL_bool = BooleanVar()
        IN_bool = BooleanVar()
        IA_bool = BooleanVar()
        KS_bool = BooleanVar()
        KY_bool = BooleanVar()
        LA_bool = BooleanVar()
        ME_bool = BooleanVar()
        MD_bool = BooleanVar()
        # MA-NJ
        MA_bool = BooleanVar()
        MI_bool = BooleanVar()
        MN_bool = BooleanVar()
        MS_bool = BooleanVar()
        MO_bool = BooleanVar()
        MT_bool = BooleanVar()
        NE_bool = BooleanVar()
        NV_bool = BooleanVar()
        NH_bool = BooleanVar()
        NJ_bool = BooleanVar()
        # NM-SC
        NM_bool = BooleanVar()
        NY_bool = BooleanVar()
        NC_bool = BooleanVar()
        ND_bool = BooleanVar()
        OH_bool = BooleanVar()
        OK_bool = BooleanVar()
        OR_bool = BooleanVar()
        PA_bool = BooleanVar()
        RI_bool = BooleanVar()
        SC_bool = BooleanVar()
        # SD-WY
        SD_bool = BooleanVar()
        TN_bool = BooleanVar()
        TX_bool = BooleanVar()
        UT_bool = BooleanVar()
        VT_bool = BooleanVar()
        VA_bool = BooleanVar()
        WA_bool = BooleanVar()
        WV_bool = BooleanVar()
        WI_bool = BooleanVar()
        WY_bool = BooleanVar()

        #------------------Dictionary of states and their boolean values and coordinates------------------#

        # 'State_Name': [state_bool, state_row, state_column]
        states_dict = {
            'Alabama': [AL_bool, 0, 0],'Alaska': [AK_bool, 0, 1],
            'Arizona': [AZ_bool, 0, 2],'Arkansas': [AR_bool, 0, 3],
            'California': [CA_bool, 0, 4],'Colorado': [CO_bool, 1, 0],
            'Connecticut': [CT_bool, 1, 1],'Delaware': [DE_bool, 1, 2],
            'Florida': [FL_bool, 1, 3],'Georgia': [GA_bool, 1, 4],
            'Hawaii': [HI_bool, 2, 0],'Idaho': [ID_bool, 2, 1],
            'Illinois': [IL_bool, 2, 2],'Indiana': [IN_bool, 2, 3],
            'Iowa': [IA_bool, 2, 4],'Kansas': [KS_bool, 3, 0],
            'Kentucky': [KY_bool, 3, 1],'Louisiana': [LA_bool, 3, 2],
            'Maine': [ME_bool, 3, 3],'Maryland': [MD_bool, 3, 4],
            'Massachusetts': [MA_bool, 4, 0],'Michigan': [MI_bool, 4, 1],
            'Minnesota': [MN_bool, 4, 2],'Mississippi': [MS_bool, 4, 3],
            'Missouri': [MO_bool, 4, 4],'Montana': [MT_bool, 5, 0],
            'Nebraska': [NE_bool, 5, 1],'Nevada': [NV_bool, 5, 2],
            'New Hampshire': [NH_bool, 5, 3],'New Jersey': [NJ_bool, 5, 4],
            'New Mexico': [NM_bool, 6, 0],'New York': [NY_bool, 6, 1],
            'North Carolina': [NC_bool, 6, 2],'North Dakota': [ND_bool, 6, 3],
            'Ohio': [OH_bool, 6, 4],'Oklahoma': [OK_bool, 7, 0],
            'Oregon': [OR_bool, 7, 1],'Pennsylvania': [PA_bool, 7, 2],
            'Rhode Island': [RI_bool, 7, 3],'South Carolina': [SC_bool, 7, 4],
            'South Dakota': [SD_bool, 8, 0],'Tennessee': [TN_bool, 8, 1],
            'Texas': [TX_bool, 8, 2],'Utah': [UT_bool, 8, 3],
            'Vermont': [VT_bool, 8, 4],'Virginia': [VA_bool, 9, 0],
            'Washington': [WA_bool, 9, 1],'West Virginia': [WV_bool, 9, 2],
            'Wisconsin': [WI_bool, 9, 3],'Wyoming': [WY_bool, 9, 4]
            }

        lf = LabelFrame(self)
        lf.place(relx=.5, rely=.5, anchor="c")
        # lf.grid(row = 0, column = 0, sticky = S)
        """
        Checkbutton title text
        """
        checkbutton_label = Label(lf, text = "Target locations by:")
        checkbutton_label.grid(row = 0, column = 0, sticky = W)
        # checkbutton_label.place(relx=.5, rely=.5, anchor=W)

        label1 = Label(self)
        radio_button4 = Radiobutton(label1, text = "RADIO BUTTON", variable = 1, value = 1)
        radio_button4.grid(row = 0, column = 0, sticky = W)

        """
        Grid of checkboxes for each state
        """
        #create label that says "Target locations by:"
        # label = Label(window, text = "Target locations by:")
        # label.grid()

        #create radio buttons
        radio_button = Radiobutton(lf, text = "None", value = 1)
        radio_button1 = Radiobutton(lf, text = "State", value = 2)
        radio_button2 = Radiobutton(lf, text = "City", value = 3)
        radio_button3 = Radiobutton(lf, text = "County", value = 4)
        radio_button.grid(row = 0, column = 1)
        radio_button1.grid(row = 0, column = 2)
        radio_button2.grid(row = 0, column = 3)
        radio_button3.grid(row = 0, column = 4)

        """
        Select all states 
        """
        for row in range(num_rows):
            for column in range(num_columns):
                # index = num_columns * row + column
                # store dictionary key in a variable named state_name for each item in states_dict by dictionary values (state_row, state_column)
                for state_name, state_values in states_dict.items():
                    if state_values[1] == row and state_values[2] == column:
                        # create a checkbox for each state
                        checkbox = Checkbutton(lf, text = state_name, variable = state_values[0])
                        checkbox.grid(row = row + 1, column = column)
                        checkbox.grid(sticky = W)
                        print("State Bool: ", state_name, state_values[0].get())
        
    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

# Send Jeffey's function
# Pass in csv that is string of search quieries
# If Target Locations by is "None" only pass in search quieries



# Pass in a string that has all keys whose chechbuttons are selected, which are strings of the state names, as string of list of states selected

if __name__ == "__main__":
    app = App()
    app.mainloop()
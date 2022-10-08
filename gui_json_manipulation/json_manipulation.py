"""
Make a variable for each value in INPUT.json file that can be changed in Tkinter GUI.
"""
import json

# Open INPUT.json file
with open('crawler-google-places-master\storage\key_value_stores\default\INPUT.json', 'r') as f:
    data = json.load(f)

json_inputs_dict = json.load(open("crawler-google-places-master\storage\key_value_stores\default\INPUT.json"))

# Store each line of INPUT.json in a dictionary
for key, value in json_inputs_dict.items():
    globals()[key] = value



# list of all states in US
states_list = [
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


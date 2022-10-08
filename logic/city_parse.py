import csv

data_file = "us_cities_states_counties.csv"
def parse(data_file):

    with open(data_file, 'r') as csv_file:

        reader = csv.DictReader(csv_file, delimiter = "|")

        reader_list = []
        for row in reader:
            reader_list.append(dict(row))

        states = []
        for row in reader_list:
            if row.get("State full") not in states:
                states.append(row.get("State full"))
    

        #create dictionary object with the states list as keys and another dictionary within with city as key and all cities in state as values
    with open(data_file, 'r') as csv_file:

        state_dict = dict({each: {"cities":[row.get("City") for row in reader_list if row.get("State full") == each], "counties":[row.get("County") for row in reader_list if row.get("State full") == each] } for each in states})

        for each in states:
        #remove duplicate cities and counties in each state
            state_dict[each]["cities"] = list(set(state_dict.get(each).get("cities")))
            state_dict[each]["counties"] = list(set(state_dict.get(each).get("counties")))
        #with open('output.txt', 'a') as f:
            #f.write(str(state_dict))

        return state_dict

def return_script_query(business_list, state_list, search_type, state_dict):
    query_list = []
    if search_type == "State":
        for each_state in state_list:
            for each_business in business_list:
                query_list.append([f"{each_business} {each_state}"])

        print(query_list)
            
    if search_type == "City":
        for each_state in state_list:
            for each_city in state_dict[each_state]["cities"]:
                for each_business in business_list:
                    query_list.append([f"{each_business} {each_city} {each_state}"])



    if search_type == "County":
        for each_state in state_list:
           for each_county in state_dict[each_state]["counties"]:
                for each_business in business_list:
                    county = " ".join(word[0].upper()+word[1:] for word in each_county.lower().split(" "))
                    query_list.append([f"{each_business} {county} {each_state}"])

    return [item for sublist in query_list for item in sublist]

def main():
    state_dict = parse(data_file)
    #print(state_dict)
    query = return_script_query(["restaurants", "infant care", "refugee services"], ["Alaska"], "County", state_dict)
    print(query)

if __name__ == '__main__':
    main()


#main()
#jsonwrite.jsonWritethenScrape(return_script_query(["pizza"],["Alaska","Texas","Arizona"],"State",parse("us_cities_states_counties.csv")),1)
#jsonwrite.jsonWritethenScrape(return_script_query(["pizza","tacos","burgers"],["Alaska","Texas","Arizona"],"City",parse("us_cities_states_counties.csv")),1)
#jsonwrite.jsonWritethenScrape(return_script_query(["pizza","tacos","burgers"],["Alaska","Texas","Arizona"],"County",parse("us_cities_states_counties.csv")),1)

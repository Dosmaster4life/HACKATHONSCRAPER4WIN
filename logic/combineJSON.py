import pandas as pd
import json
import glob,os

json_Folder = 'data/' # copy the json files to this folder
json_Type = os.path.join(json_Folder, '*.json') # get all the json files in the folder
json_File_List = glob.glob(json_Type) # create a list of the json files
Data = []
for file in json_File_List: # loop through the list of json files
    with open(file) as f:
        json_data = pd.json_normalize(json.loads(f.read()))
        json_data['fileName'] = file.rsplit("/", 1)[-1]
    Data.append(json_data) # append the json data to the list
allData = pd.concat(Data) # combine the list of json data into one dataframe
json_Structure = json.loads(allData.to_json(orient="records")) # convert the dataframe to a json structure

allData_Flat = pd.io.json.json_normalize(json_Structure) # flatten the json structure


openingRevised = allData_Flat.openingHours.apply(pd.Series)
openingRevised.columns = [ 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday'] # rename the columns
openingRevised = openingRevised.applymap(lambda x: x['hours'] if isinstance(x, dict) else x)
# convert each phone number to this format: 123.456.7890 and with  extentions only if they exist
phone3 = allData_Flat.phone.apply(lambda x: x.replace('(','').replace(')','').replace('-','').replace(' ','').replace('.','')) # remove all the characters that are not numbers
phone3 = phone3.apply(lambda x: x[:3] + '.' + x[3:6] + '.' + x[6:10] + ' ext.' + x[10:] if len(x) > 10 else x[:3] + '.' + x[3:6] + '.' + x[6:10]) # add the periods and extension if it exists
#rename phone3 to phoneParsed
phone3.name = 'Phone Parsed'
allData_Flat = pd.concat([allData_Flat, openingRevised,phone3], axis=1)
allData_Flat.drop(columns=['orderBy','plusCode','isAdvertisement','rank','placeId','cid','url','searchPageUrl','reviewsCount','reviews',	'reviewsDistribution.oneStar',	'reviewsDistribution.twoStar','reviewsDistribution.threeStar','reviewsDistribution.fourStar','reviewsDistribution.fiveStar','price','menu','temporarilyClosed','permanentlyClosed','totalScore','openingHours','subTitle','fileName'
], inplace=True)


allData_Flat.to_excel("output.xlsx", index=False)
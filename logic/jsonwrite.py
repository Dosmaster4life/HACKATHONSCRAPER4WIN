import json
import os

import Scrape

def jsonWritethenScrape(searchTermList = [ "Pizza", "Chicken", "Steak"],maxResults = 1):

    data = {
        "searchStringsArray": searchTermList,
        "allPlacesNoSearch": "false",
        "maxCrawledPlaces": 100000000,
        "language": "en",
        "exportPlaceUrls": "false",
        "includeHistogram": "false",
        "includeOpeningHours": "true",
        "includePeopleAlsoSearch": "false",
        "additionalInfo": "false",
        "oneReviewPerRow": "false",
        "maxImages": 0,
        "maxReviews": 0,
        "scrapeReviewerName": "false",
        "scrapeReviewerId": "false",
        "scrapeReviewerUrl": "false",
        "scrapeReviewId": "false",
        "scrapeReviewUrl": "false",
        "maxPagesPerBrowser": 10,

        "scrapeResponseFromOwnerText": "false",
        "proxyConfig": {
            "useApifyProxy": False
        },
        "maxCrawledPlacesPerSearch": maxResults,
        "maxPageRetries": 3
    }

    # Overwrite the file with the new data in directory ../crawler-google-places-master/storage/datasets/key_value_stores/default/INPUT.json
    with open('../crawler-google-places-master/storage/key_value_stores/default/INPUT.json', 'w') as outfile:
        json.dump(data, outfile)
    # Run the file in the directory ../logic/Scrape.py
    Scrape.scrape()

    # create json

jsonWritethenScrape()
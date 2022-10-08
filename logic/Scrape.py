
# Run shell command "apify run --purge" in the directory HACKATHONSCRAPER4WIN/crawler-google-places-master in python
import subprocess
import os

# read file scrape.txt in current directory and set it to a variable
def scrape():
    with open('scrape.txt', 'r') as file:
        data = file.read().replace('\n', '')

    if (data != "true"):
        # view the output of the shell command

       # print(subprocess.run(["cd", "../crawler-google-places-master", ";apify run --purge"], shell=True))
        with open('scrape.txt', 'w') as file:
            file.write("true")
        os.system("cd ../crawler-google-places-master;apify run --purge")
        import combineJSON
        combineJSON.combine()
        # output scraping complete
        print("Scraping Complete, file written as output.xlsx")
        with open('scrape.txt', 'w'):
            file.write("false")




    else:
        os.system("cd ../crawler-google-places-master;apify run --purge")
        import combineJSON
        combineJSON.combine()
        # output scraping complete
        print("Scraping Complete, file written as output.xlsx")
        with open('scrape.txt', 'w'):
            file.write("false")



scrape()






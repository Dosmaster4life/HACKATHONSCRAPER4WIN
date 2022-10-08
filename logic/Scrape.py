
# Run shell command "apify run --purge" in the directory HACKATHONSCRAPER4WIN/crawler-google-places-master in python
import subprocess
import os
import shutil
import datetime
def backup():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")
    # create a directory with the current date and time

    os.mkdir("backup " + date + " " + time)
    # copy the output file to the new directory
    shutil.copy("output.xlsx", "backup " + date + " " + time + "/output.xlsx")
    # output backup complete
    print("Backup Complete")

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
        try:
            import combineJSON
            combineJSON.combine()
            backup()
            print("Scraping Complete, file written as output.xlsx")
        except:
            print("An error occured")
            pass
        with open('scrape.txt', 'w'):
            file.write("false")




    else:
        os.system("cd ../crawler-google-places-master;apify run")
        try:
            import combineJSON
            combineJSON.combine()
            backup()
            print("Scraping Complete, file written as output.xlsx")
        except:
            print("An error occured")
            pass

        # output scraping complete

        with open('scrape.txt', 'w'):
            file.write("false")



# create a backup directory for all prevous scrapes








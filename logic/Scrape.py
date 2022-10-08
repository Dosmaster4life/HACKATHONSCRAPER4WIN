
# Run shell command "apify run --purge" in the directory HACKATHONSCRAPER4WIN/crawler-google-places-master in python
import subprocess

# read file scrape.txt in current directory and set it to a variable
def scrape():
    with open('scrape.txt', 'r') as file:
        data = file.read().replace('\n', '')

    if (data == "false"):
        subprocess.run(["cd", "../crawler-google-places-master", "apify run --purge"], shell=True)
        subprocess.run(["pwd"], shell=True)
        with open('scrape.txt', 'w') as file:
            file.write("true")
    else:
        subprocess.run(["cd", "../crawler-google-places-master", "apify run"], shell=True)
        # get current directory
        subprocess.run(["pwd"], shell=True)
    # change subprocces directory


scrape()






# finish the apify run with

# import the necessary packages

import os

import shutil

import datetime
import subprocess

import time

os.system("cd ../crawler-google-places-master;apify run")


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


try:
    import combineJSON

    combineJSON.combine()
    backup()
    print("Scraping Complete, file written as output.xlsx")
except:
    print("An error occured")
    pass
subprocess.call(['open', "output.xlsx"])





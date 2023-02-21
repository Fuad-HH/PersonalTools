import re
import requests
from termcolor import colored
import os

# print status now
print(colored("Getting Job Oppeinings...\n", "green"));

# this part checks if there is a new job posting
url = "https://erecruitment.bb.org.bd/onlineapp/joblist.php";
page_data = requests.get(url);

flag_job = page_data.text.find("There are no advertised positions at the moment");

if flag_job==-1:
    print(colored("There might be available circulars on the BB application page.\n", "red"));
    
    # ask if user wants to see the page
    print(colored("Do you want to see the page? (y/n)", "green"));
    choice = input();
    # open the page if user wants to on google-chrome
    if choice=="y":
        print(colored("Opening the page on google-chrome...", "green"));
        os.system("google-chrome https://erecruitment.bb.org.bd/onlineapp/joblist.php");
else:
    print("No open job applications.\n");

# print status now
print(colored("Getting Admit Avaiability...\n", "green"));
# this part checks if there is any admit card available to download
url = "https://erecruitment.bb.org.bd/onlineapp/print_admit.php";
page_data = requests.get(url);

flag_admit = page_data.text.find("No admit card available to download");

if flag_admit==-1:
    print(colored("There might be available admit cards on the BB application page.\n", "red"));
    # ask if user wants to see the page
    print(colored("Do you want visit the admit download page? (y/n)", "green"));
    choice = input();
    # open the page if user wants to on google-chrome
    if choice=="y":
        print(colored("Opening the page on google-chrome...", "green"));
        os.system("google-chrome https://erecruitment.bb.org.bd/onlineapp/print_admit.php");
else:
    print("No admit card available to download.\n");
    
# check if both flags were -1
if flag_job==-1 and flag_admit==-1:
    # ask the user if he wants to be more sure
    print(colored("Do you want to be more sure by visiting the BB e-recruitment page? (y/n)", "yellow"));
    choice = input();
    # if yes, then visit the bb erecruitment home page
    if choice=="y":
        print(colored("Opening the BB recruitment page...", "green"));
        os.system("google-chrome https://erecruitment.bb.org.bd/onlineapp/home.php");

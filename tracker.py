# Job Application Tracker v2 
# Built by Abatar Bhattarai 

import csv 
import os 
from datetime import date 

FILE = "applications.csv"

def add_job():
    company = input("Company name:")
    role = input("Role: ")
    status = input("Status (Applied/Interview/Rejected):")
    today = str(date.today())

    with open(FILE, "a" , newline="") as f:
        writer=csv.writer(f)
        writer.writerow([company,role,status,today])
    print(f":saved: {company} |{role} | {status} | {today}")
           
def view_jobs():
        if not os.path.exists(FILE):
            print("No application yet.")
            return 
        with open(FILE, "r") as f:
            reader =csv.reader(f)
            for row in reader:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

#Run
print("1. Add application")
print("2. View application")
choice = input("choose: ")

if choice == "1":
    add_job()
elif choice == "2":
    view_jobs()


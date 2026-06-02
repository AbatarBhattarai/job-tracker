#Job Application Tracker 
#Built by Abatar Bhattarai

applications= []

def add_job(company,role,status):
    job = {"company":company,"role":role,"status":status}
    applications.append(job)
    print(f"Added: {company} | {role} | {status}")

def view_jobs():
    if len(applications) == 0:
        print("No applicationyet.")
    else:
        for job in applications:
            print(f"{job['company']} | {job['role']} | {job['status']}")

#Test it 
add_job("Google","Software Intern","Applied")
add_job("Amazon","Data Analyst Intern","Applied")
view_jobs()
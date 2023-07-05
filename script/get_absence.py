'''

This is a script created by Christopher Bannon for ...

'''


### IMPORTS ###
import requests
import os
import json
from dotenv import load_dotenv
from bases_and_tables import BASE_ID, ABSENCE_TABLE


# Load in api keys
load_dotenv()
airtable_key = os.environ['AIRTABLE_API_KEY']

# Credentials
base_id = BASE_ID
table_name = ABSENCE_TABLE

# We filter out students that have been resolved
filter_by_formula = "?filterByFormula=NOT(%7BResolved%7D)"

# Define the Airtable API endpoint URL
url = f'https://api.airtable.com/v0/{base_id}/{table_name}{filter_by_formula}'

# Set the request headers
headers = {
    'Authorization': f'Bearer {airtable_key}',
    'Content-Type': 'application/json'
}

def fetch_students():
    # Make a GET request to fetch records from the table
    response = requests.get(url, headers=headers)

    # Handle the response
    if response.status_code != 200:
         print(f'Request failed with status code {response.status_code}')
    
    records = response.json()['records']
    approved = []
    rejected = []
    for record in records:
        # Access record fields using the 'fields' key
        fields = record['fields']
        if fields.get("Rejected") == True:
            rejected.append(fields)
        elif fields.get("Approved") == True:
            approved.append(fields)
        else:
            print("Something went wrong! Please approve or reject the following event:")
            name = fields.get('Name')
            date = fields.get('created')
            print(f"Name: {name}\nDate: {date}\n")

    return approved, rejected
   


if __name__ == "__main__":
    approved, rejected =  fetch_students()
    with open("approved-students.json", "w") as write_file:
        json.dump(approved, write_file)
    with open("rejected-students.json", "w") as write_file:
        json.dump(rejected, write_file)
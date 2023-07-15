'''

This is a script created by Christopher Bannon for ...

'''


### IMPORTS ###
import requests
import os
import json
from tqdm import tqdm
from dotenv import load_dotenv
from logic.bases_and_tables import BASE_ID, get_table

load_dotenv()
airtable_key = os.environ['AIRTABLE_API_KEY']

# We filter out students that have been emailed already
filter_by_formula = "?filterByFormula=NOT(%7BEmailed%7D)"

# Set the request headers
headers = {
    'Authorization': f'Bearer {airtable_key}',
    'Content-Type': 'application/json'
}

def get_url(flag):
    '''Returns the url for the Airtable API endpoint'''
    table_name = get_table(flag)
    return f'https://api.airtable.com/v0/{BASE_ID}/{table_name}'

def fetch_students(flag: str) -> tuple[list, list]:
    '''Fetches students from Airtable
    
    Parameters:
    flag : The flag to determine what table to fetch students from.
    '''
    url = get_url(flag)
    response = requests.get(f'{url}/{filter_by_formula}', headers=headers)

    # Handle the response
    if response.status_code != 200:
         print(f'Request failed with status code {response.status_code}')
    
    records = response.json()['records']
    approved = []
    rejected = []
    for record in tqdm(records, desc=f"Fetching students from {flag} table"):
        # Access record fields using the 'fields' key
        fields = record['fields']

        if fields.get("Approved") == True:
            approved.append(record)
        else:
            rejected.append(record)

    return approved, rejected
   

def update_students(ids: list, flag: str) -> None:
    # our field to update
    fields = {'Emailed': True}
    data = {'fields': fields}
    data_json = json.dumps(data)
    url = get_url(flag)

    for id in tqdm(ids, desc=f"Updating students in {flag} table"):
        # Make a PATCH request to update the record
        response = requests.patch(f'{url}/{id}', headers=headers, data=data_json)
        if response.status_code != 200:
            print(f'Request failed with status code {response.status_code}')
        else:
            updated_record = response.json()['fields']
            print(f'Record updated successfully: {updated_record}')

def update_student(id: str, flag:str) -> None:
    # our field to update
    fields = {'Emailed': True}
    data = {'fields': fields}
    data_json = json.dumps(data)
    url = get_url(flag)

    # Make a PATCH request to update the record
    response = requests.patch(f'{url}/{id}', headers=headers, data=data_json)
    if response.status_code != 200:
        print(f'Request failed with status code {response.status_code}')
    else:
        updated_record = response.json()['fields']
        print(f'Record updated successfully: {updated_record}')


if __name__ == '__main__':
#     approved, rejected, ids = fetch_students()
# #     print(approved)
#     print(len(approved))
# #     print(rejected)
#     print(len(rejected))
#     print(len(ids))
    # test = fetch_students()
    # print(test)
    # update_student([test[0]['id']])
    pass
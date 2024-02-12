import sys
import os
from dotenv import load_dotenv
from openai import OpenAI
client = client = OpenAI()

load_dotenv()


# Please pass in the row from spreadsheet into the command line
# Please put the assignment in quotes if it has spaces
def main():
    # print_args()

    date = sys.argv[1]
    time = sys.argv[2]
    email = sys.argv[3]
    first_name = sys.argv[4]
    last_name = sys.argv[5]
    assignment = sys.argv[6]
    due_date = sys.argv[7]
    extension_days = sys.argv[8]
    extension_date = sys.argv[9]
    dsp = sys.argv[10]
    reason = sys.argv[11]

    flag = True

    while True:
        user_input = input("Accept Extension? y or n ")
        print('')
        if user_input.lower() == 'y':
            flag = True
            break
        elif user_input.lower() == 'n':
            flag = False
            break
        else:
            print("Please enter 'y' or 'n'")
            print('')
    
    email_body = read_email(flag)
    email_body = email_body.replace('~NAME~', first_name)
    email_body = email_body.replace('~ASSIGNMENT~', assignment)
    email_body = email_body.replace('~DATE~', extension_date)
    email_body = email_body.replace('~DUE_DATE~', due_date)

    print("SUBJECT: ")
    print("Extension Request for " + ask_gpt() + assignment)

    print("\nTO: ")
    print(email)

    print("\nCC: ")
    print(os.getenv('CC_EMAIL'))

    print("\nBODY:\n")
    print(email_body)


def ask_gpt() -> str:
    used = ""
    with open('used.txt', 'r') as f:
        used = f.read()

    prompt="Please only respond with 1 singular word. Do not elaborate. No extra text. Simply respond with a mis-spelling of the word 'extension'. Avoid using duplicates here: {used}",
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
    ]
    )

    # Send a request to GPT-3 with the provided prompt
    response = completion.choices[0].message
    used += ", {response}"
    with open('used.txt', 'w') as f:
        f.write(used)

    # Parse and return the response text
    return response
    

def read_email(flag: bool) -> str:
    '''True --> Accept | False --> Reject'''
    if flag:
        with open('email_accept.txt', 'r') as f:
            return f.read()
    else:
        with open('email_reject.txt', 'r') as f:
            return f.read()

def write_email(email_body: str, subject: str, to: str, cc: str):
    to_write = f"Subject: {subject}\nTo: {to}\nCC: {cc}\n\n{email_body}"
    with open('email.txt', 'w') as f:
        f.write(to_write)

def print_args():
    print("Arguments provided:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")

if __name__ == "__main__":
    print("GENERATING EMAIL STUFF...\n")
    main()
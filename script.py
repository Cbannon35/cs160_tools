'''
Main tool for CLI
'''
import sys, os
from tqdm import tqdm
from logic.json_logic import read_students, write_students, clear_students, read_emails, write_emails, clear_emails, read_email_template
from logic.airtable_logic import fetch_students, update_student, update_students
from dotenv import load_dotenv

def import_email_logic():
    global email, send_message, create_message
    from logic.email_logic import email, send_message, create_message

load_dotenv()
SENDER = os.environ['EMAIL_SENDER']

args = sys.argv[1:]

commands_help = {"help": "Prints this help message", 
            "fetch [OPTION]": "Fetches students from Airtable", 
            "generate": "Generates emails to send to students", 
            "email": "Sends generated emails to students",
            "view [OPTION]": "Views result of fetch and generate",
            "clear": "Clears students and emails", 
            "exit/quit": "Exits the program"}

flags_help = {
    "-a": "absence",
    "-e": "extension",
    "-s": "students",
    "-m": "emails",
    "-all": "all"
}

def help(*args) -> None:
    print('''\n
            -------------------------------------------------------
            |        _  _     _        __  __                     |
            |       | || |___| |_ __  |  \/  |___ _ _ _  _        |
            |       | __ / -_) | '_ \ | |\/| / -_) ' \ || |       |
            |       |_||_\___|_| .__/ |_|  |_\___|_||_\_,_|       |
            |                  |_|                                |
            -------------------------------------------------------
\n''')
    print("Typical Usage: python script.py [COMMAND] [OPTION]\n")

    print("OPTIONS:\n")
    # print("The following flags and what they refer to:\n")
    # max_flag_length = max(len(flag) for flag in flags_help.keys())
    for flag, description in flags_help.items():
        # flag_aligned = f"{flag:>{max_flag_length}}"
        # description_aligned = description
        # print(f"\t{flag_aligned} \t->\t {description_aligned}")
        print(f"\t{description}")

    print("\nCOMMANDS:\n")
    max_command_length = max(len(command) for command in commands_help.keys())
    for command, msg in commands_help.items():
        command_aligned = f"{command:>{max_command_length}}"
        msg_aligned = msg
        print(f"\t{command_aligned} \t->\t {msg_aligned}")

def fetch(flag : str) -> None:
    '''Fetches students from Airtable and writes them to students.json'''
    valid_flags = ["absence", "extension"]
    if flag not in valid_flags:
        print("Invalid flag! Try 'absence' or 'extension'")
        return
    approved, rejected = fetch_students(flag)
    write_students(approved, rejected, flag)
    # return absence, extension

def generate():
    '''Generates emails to send to students'''
    approved, rejected, absence_or_extension = read_students()
    if absence_or_extension is None:
        print("No students fetched! Try 'fetch [OPTION]'")
        return
    
    template = read_email_template(absence_or_extension)
    rejected_template = template['rejected']
    approved_template = template['approved']
    approved_emails = []
    rejected_emails = []
    for student in tqdm(approved, desc="Generating approved emails"):
        # also valid because of airtable script: body = student['fields']['Email Text']
        # Student, Event, Date = student['fields']['Name'], student['fields']['Activity'], student['fields']['Date']
        # body = f"{approved_template['body']}"
        # body = body.replace("{Student}", Student)
        # body = body.replace("{Event}", Event)
        # body = body.replace("{Date}", Date)
        body = student['fields']['Email Text']
        generated_email = {"sender": SENDER, "to": student['fields']['Student Email'], "subject": approved_template['subject'], "body": body, "Cc": approved_template['Cc']}
        approved_emails.append((generated_email, student['id']))
    for student in tqdm(rejected, desc="Generating rejected emails"):
        # Student, Event, Date = student['fields']['Name'], student['fields']['Activity'], student['fields']['Date']
        # body = f"{rejected_template['body']}"
        # body = body.replace("{Student}", Student)
        # body = body.replace("{Event}", Event)
        # body = body.replace("{Date}", Date)
        body = student['fields']['Email Text']
        generated_email = {"sender": SENDER, "to": student['fields']['Student Email'], "subject": rejected_template['subject'], "body": body, "Cc": rejected_template['Cc']}
        rejected_emails.append((generated_email, student['id']))
    
    all_emails = approved_emails + rejected_emails
    write_emails(all_emails, absence_or_extension)
    print(f"Generated {len(all_emails)} emails!")

def email():
    '''Sends emails to students'''
    emails, absence_or_extension = read_emails()
    if absence_or_extension is None:
        print("No emails generated! Try 'generate [OPTION]'")
        return
    import_email_logic()
    sent = []
    failed = []
    for mail, record_id in tqdm(emails, desc="Sending emails"):
        print(mail, record_id)
        # sender, to, subject, body, Cc = email['sender'], email['to'], email['subject'], email['body'], email['Cc']
        test = create_message(mail['sender'], mail['to'], mail['subject'], mail['body'], mail['Cc'])
        print(test)
        if email(mail['sender'], mail['to'], mail['subject'], mail['body'], mail['Cc']):
            sent.append(record_id)
        else:
            print(f"Failed to send email to {mail['to']}")
            failed.append((mail, record_id))
        
    if len(failed) != 0:
        print(f"Failed to send {len(failed)} emails!")
        print("Writing failed emails to emails.json...")
        print("Please view emails.json to see which emails failed to send.")
        write_emails(failed, absence_or_extension)
    else:
        print("Successfully sent all emails!")
        print("Deleting emails from emails.json...")
        clear_emails()
    
    print("Updating Airtable...")
    update_students(sent, absence_or_extension)



def view(flag : str) -> None:
    '''Displays the students or the emails json in a readable format'''
    if flag == "students":
        absence, extension, absence_or_extension = read_students()
        if absence_or_extension is None:
            print("No students fetched! Try 'fetch [OPTION]'")
            return
        print(f"Approved for {absence_or_extension}: {len(absence)}\n")
        for student in absence:
            print(f"\t{student['fields']['Name']}")
        print(f"\nDenied for {absence_or_extension}: {len(extension)}\n")
        for student in extension:
            print(f"\t{student['fields']['Name']}")
    elif flag == "emails":
        emails, absence_or_extension = read_emails()
        if absence_or_extension is None:
            print("No emails generated! Try 'generate [OPTION]'")
            return
        print(f"Emails: {len(emails)}\n")
        for email in emails:
            print(f'{email}\n')
    else:
        print("Invalid flag! Try 'students' or 'emails'")

def clear(flag: str) -> None:
    '''Cleans up the students or the emails json'''
    if flag == "students":
        clear_students()
        print("Cleared students!\n")
    elif flag == "emails":
        clear_emails()
        print("Cleared emails!\n")
    elif flag == "all":
        clear_students()
        clear_emails()
        print("Cleared both students and emails!\n")
    else:
        print("Invalid flag! Try 'students' or 'emails'")

def quit():
    sys.exit(0)

commands = {"help": (help, 0),
            "fetch": (fetch, 1),
            "generate": (generate, 0),
            "email": (email, 0),
            "view": (view, 1),
            "clear": (clear, 1),
            "quit": (quit, 0),
            "exit": (quit, 0)}

# def validate_flag(flag):
#     '''Makes sure the flag is a valid flag'''
#     if flag not in ["", "students", "-s", "emails", "-e", "absence", "-a", "extension", "-e", "all", "-all"]:
#         print("Invalid flag!")
#         return False
#     return True

def parse(user_input: str) -> None:
    '''Parses the user input and calls the appropriate function'''
    # print(user_input)
    user_input = user_input.split()
    command = user_input[0]
    flags = user_input[1:]

    if command not in commands:
        print("Invalid command! Type 'help' for a list of commands.")
        return 
    
    func, arg_len = commands[command]

    if len(user_input) - 1 != arg_len:
        print(f"Invalid number of arguments! Type 'help' for a list of commands.")
        return
    
    # if validate_flag(user_input[1]):
    #     func(user_input[1])
    func(*flags)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        print("for now, please just run the script without any arguments")
    else:
        # No arguments provided
        print("""
            -------------------------------------------------------
            |        _    _      _                                |
            |       | |  | |    | |                               |
            |       | |  | | ___| | ___ ___  _ __ ___   ___       |
            |       | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \      |
            |       \  /\  /  __/ | (_| (_) | | | | | |  __/      |
            |        \/  \/ \___|_|\___\___/|_| |_| |_|\___|      |
            |                                                     |
            -------------------------------------------------------
        """)
        # print("\t\t\t<--Welcome to the 160 Script-->\n")
        print("\t\t\tType 'help' to display commands\n")
        while True:
            user_input = input(">>>")

            parse(user_input)
    
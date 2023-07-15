from logic.email_logic import email, send_message, create_message
import sys

# get system args
args = sys.argv[1:]

def check_args():
    if len(args) != 5:
        print('Incorrect number of args passed')
        return False
    return True

def main():
    if len(args) == 0:
        message = create_message('bannon.c.35@berkeley.edu', 
                             'bannon.c.35@gmail.com', 
                             'bannon.c.35@berkeley.edu', 
                             'Email test pt 2', 
                             'This is the body of the email')
    
        send_message(message)
        send_message(message)
        send_message(message)
    else:
        email(args[0], args[1], args[2], args[3], args[4])

if __name__ == '__main__':
    main()


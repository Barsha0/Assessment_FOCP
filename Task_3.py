#imported random module, regular expression module and type module.
import random
import re
import types

network_error_percentage = 10                                          #to check for 10% network error.
chat_op = ['Janice','John','Alice','Jane','Peter','Fiona','Ian']       #List of chat operators.

def greet_goodbye(user):                                                #Define function called greet_goodbye
    print(f'Thank You, {user}, for using PopChat. See you again soon!')    #last messege display after all question_response.
    exit(0)                                                             #program terminate here.

#All question prompt.
question_prompt = [
    {
        'types': ['wifi'],
        'responses': [
            'WiFi is excellent across the campus.',
            'No WiFi issue has been reported so far today.'
        ],
    },
    {
        'types': ['library'],
        'responses': [
            'The library is closed today.',
        ],
    },
    {
        'types': ['deadline'],
        'responses': [
            'Your deadline has been extended by two working days.'
        ],
    },
    {
        'types': ['presentation'],
        'responses': [
            'Presentation has been postpone',
            'Presentation scheduled for tomorrow has been canceled for now.',
            'Presentation starting tomorrow at 8:30 am'
        ],
    },
    {
        'types': ['meeting'],
        'responses': [
            'Meeting has been postponed',
            'Meeting has been cancelled',
            'No meeting today.',
        ],
    },
    {
        'types': ['bye', 'exit'],
        'responses': greet_goodbye,
    },
]


def get_email_input():                                                          #define a function called get_email_input.
    email = input("Please enter your Poppleton email address: ")                #Asking for input email from the user
    is_email_valid = bool(re.match("^[a-zA-Z0-9_.]{2,}@pop.ac.uk$", email))     #Email is only valid if given condition meet.

    #if entered email is valid this if part will execute.
    if is_email_valid:                                                           #checking condition for validation of email
        user = email.split('@')[0].title()                                       #breaking into 2 part user and domain.And title will convert upper case to lower.

        return user, email                                                       #to return user and email

    #if entered email is invalid this else part will execute.
    else:
        print(f'Invalis email address\n"{email}" is invalid email at pop.ac.uk') #if email is invalid then it will display this message.
        exit(0)                                                                  #if email is invalid program terminate here.


def ask_and_respond_question(user):                                              #define function called ask_and respond_question having one parameter user.
    question = input("---> ").lower().strip()                                    #asking for input from user and strip function will remove the white space.
    stall_phrases = ['Hmm', 'Oh, yes, I see', 'Tell me more']                    #If no matching word is found, the program should respond randomly with these phrases.

    #loop start from here.
    for question_type_response in question_prompt:
        question_types = question_type_response.get('types')

        for question_type in question_types:
            if question_type in question:
                responses = question_type_response.get('responses')

                if isinstance(responses, list):                             #function to returns true or false if a variable matches a specified data type.
                    print(random.choice(responses))                         #for selecting random responses
                elif isinstance(responses, types.FunctionType):
                    responses(user)                                         
                return

    print(random.choice(stall_phrases))                                    #select one random phrase If no matching word is found.


def check_network_error(user):                                              #define function called check_network_error to check the error
    chance = random.randint(1, 100)                                         #10% probablity to display error message.Randint returns an integer number selected element from the specified range.

    if chance > network_error_percentage:                                   #the chance is greater than network error.
        return

    print('*** NETWORK ERROR ***')                                         #Display Network error message 1 time if it is executed for 10 times.
    greet_goodbye(user)                                                    #And after error message the greet_goodbye function is call.


def main():                                                                #Define function called main.
    print("Welcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")         

    user, email = get_email_input()                                         #Calling the get_email_function.
    operator = random.choice(chat_op)                                       #Pick any random operator from the helpdesk list

    #The chat system should greet the user by name. The user's name is the left-hand part of their email (before the @).
    print(f'Hi, {user}! Thank you, and Welcome to PopChat!\n'f'My name is {operator}, and it will be my pleasure to help you.')

    #while loop executes if it's 10% probablity to get error message otherwise the chat system should then prompt the user to enter their question.
    while True:
        check_network_error(user)
        ask_and_respond_question(user)


if __name__ == '__main__':                   #to check weather it is script or module.
    main()                                   #call the main function.

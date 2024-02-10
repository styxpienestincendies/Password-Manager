user = input('Enter your username: ')
pass1 = input('Enter your password: ')
credentials = {'user_username': user, 'pass_password': pass1}

passwords = {}

def login():
    entered_user = input('Enter your username: ')
    entered_pass = input('Enter your password: ')

    if entered_user == credentials['user_username'] and entered_pass == credentials['pass_password']:
        return True
    else:
        print('Invalid username or password. Access denied.')
        return False


def add_password():
    if login():
        website = input("Enter Website Name: ")
        username = input("Enter Your  Username: ")
        password = input("Enter Your Password: ")
        passwords[website] = {'username': username, 'password': passwords}
        print('Your password has been saved')


def view_password():
    if login():
        is_password = input('Enter the Website Name: ')
        if is_password in passwords:
            print("Username: ", passwords[is_password]["username"])
            print("Username: ", passwords[is_password]["password"])
        else:
            print('That is Incorrect')


def delete_password():
    if login():
        del_password = input('Enter the Website Name: ')
        if del_password in passwords:
            del passwords[del_password]
            print('Password Delete')
        else:
            print('Website is not found.')


def view_all_passwords():
    if login():
        print("All Passwords:")
        for website, info in passwords.items():
            print("Website:", website)
            print("Username:", info["username"])
            print("Password:", info["password"])
            print("----------------------")


while True:
    user_input = int(input('''
Welcome to your Personal Password Manager
Here our your corresponding options:
0 - Add a Password
1 - View a specific Password
2 - Delete a Password
3 - View all your Passwords
4 - Exit
'''))

    if user_input == 0:
        add_password()
    elif user_input == 1:
        view_password()
    elif user_input == 2:
        delete_password()
    elif user_input == 3:
        view_all_passwords()
    elif user_input == 4:
        break
    else:
        print('Invalid Option. Please choose from 0-4')

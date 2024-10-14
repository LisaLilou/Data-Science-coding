# Import dateime to then use in the add_task function
import datetime

# Function "register user": Create a function that can register students
    # Ask for the user's new usernam and password
        # Confirm the password by creating a while loop for the user to input the correct password twice, if not ask again
    # Append the confirmed password to the user.txt file
def register_user(menu_options):
    if menu_options=="r":
            new_username= input("Please enter a new username: ")
            username_list.append(new_username)
            new_password= input("Enter your new password: ")
            confirming_password= input("Confirm password: ")
            while new_password!= confirming_password:
                  print("The passwords do not match. Please try again.")
                  new_password= input("Enter your new password: ")
                  confirming_password= input("Confirm password: ")
            if new_password==confirming_password:
                password_list.append(new_password)
            with open('user.txt','w+') as file: 
                for i in range(len(username_list)):
                    file.write(username_list[i]+", "+ password_list[i]+"\n")
    return("New username and password registered. \n")

# Function "add task": Create a function that can add tasks to the tasks.txt file
    # Ask for the user's input on the username of the task assigned to, title, description and due date
        # Use the datetime imported to get the date the task was assigned
        # Default task completion to "No"
    # Create a list from the users input in the same order as in the file
    # Append the list to the tasks.txt file
def add_task(menu_options):
    if menu_options=="a":
        print("\nInsert the following information of the task: \n")
        task_username=input("The username of the person whom the task is assigned to: ")
        task_title=input("Title: ")
        task_description=input("Description: ")
        task_date_assigned= datetime.date.today().strftime("%Y-%m-%d")
        task_due_date=input("Due date (e.g yyyy-mm-dd): ")
        task_completion="No"
        task=[task_username,task_title,task_description,task_date_assigned,task_due_date,task_completion]
        with open('tasks.txt','a')as file:
            file.write("\n"+", ".join(task))
    return("You have added your task \n")

# Function "view all": Create a function that can show all the tasks in tasks.txt file
    # Create a for loop that prints the tasks in order in a legible order
def view_all(menu_options):
    if menu_options=="va":
        tasks=read_tasks()
        print(f"\nTasks:\n")
        for task in tasks:
            print(f"Username: {task[0]}")
            print(f"Task title: {task[1]}")
            print(f"Description: {task[2]}")
            print(f"Date assigned: {task[3]}")
            print(f"Due date: {task[4]}")
            print(f"Task completed: {task[5]} \n")
    return("\n")

# Function "view mine": Create a function that can show the tasks in tasks.txt file of the user who logged in
    # Create a for loop where if the username in the task equals to the username logged in it prints out the tasks assigned to them
def view_mine(menu_options):
    if menu_options=="vm":
        tasks=read_tasks()
        print(f"\nTasks assigned:\n")
        for task in tasks:
            if task[0]== username:
                print(f"Username: {task[0]}")
                print(f"Task title: {task[1]}")
                print(f"Description: {task[2]}")
                print(f"Date assigned: {task[3]}")
                print(f"Due date: {task[4]}")
                print(f"Task completed: {task[5]} \n")
    return("")

# Function "display statistics":Create a function that can show the number of tasks and users registered
    # Use a counter to count the number of usernames in user.txt and tasks in tasks.txt
    # Print the total
def display_statistics(menu_options):
    if menu_options=="ds":
        print("\nStatistics:\n")
        print(f"Total amount of usernames registered : {str(count_username)}")
        print(f"Total amount of tasks : {str(count_task)}\n")
    return("")

# Create a list where the usernames and passwords will be appended to in the register task function
username_list=[]
password_list=[]

# Create a counter for the amount of usernames and tasks assigned in each file
count_username= 0
count_task=0

# Open the user.txt file to read only
    # Create a for loop for each line that split's it and appends the first word to the username and the second to the password
    # Add one each time to the counter for the username
with open('user.txt', 'r+')as file:
    for line in file:
        line_2=line.rstrip("\n")
        splitting_items=line_2.split(", ")
        username_list.append(splitting_items[0])
        password_list.append(splitting_items[1])
        count_username+=1

# Create a function that the tasks in tasks.txt file
    # Open the tasks.txt file to read only
    # Create a list
    # Create a for loop for each line that split's it by the comma
        # Append the split line in the list created above
    # Add one each time to the counter for the tasks
def read_tasks():
    with open('tasks.txt','r+')as file:
        tasks=[]
        for line in file:
            split_line=line.strip().split(", ")
            tasks.append(split_line)
    return tasks
with open('tasks.txt','r+')as file:
        for line in file: 
            count_task+=1

#====Login Section====

# Ask the user for their username and password and store it as input at the start
username=input("Username: ")
password=input("Password: ")

# Create a while loop that only allows the user to log in if their username and password is registered in the user.txt file
    # Return error messages if they enter invalid information, until they register correctly
    # Print otu a statemnt that they have logged in correctly
while username not in username_list or password not in password_list:
    if username in username_list and password not in password_list:
        print("Invalid password. Please try again.")
        username=input("Username: ")
        password=input("Password: ")
    if username not in username_list and password in password_list:
        print("Username not found. Please try again.")
        username=input("Username: ")
        password=input("Password: ")
    if username not in username_list and password not in password_list:
        print("Invalid input. Please try again.")
        username=input("Username: ")
        password=input("Password: ")
if username in username_list or password in password_list:
    print("You have logged in succesfully \n")

# Create a while loop that once the user has logged in can see the menu
    # Using an if statement offer two different menus as only the admin is allowed to register users and display statistics
        # Within this if statement assign value to each menu option by using the fuctions above
        # If the user enters "e" exit the loop 
        # If the user inputs an option not seen in the menu, print out an error message
while True:
    if username== "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
    else:
          menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
    if menu == "r":
         print(register_user(menu))
    elif menu =="a":
         print(add_task(menu))
    elif menu=="va":
        print(view_all(menu))
    elif menu=="vm":
        print(view_mine(menu))
    elif menu=="ds":
        print(display_statistics(menu))
    elif menu=="e":
        print('Goodbye!!!')
        exit()
    else:
        print("You have entered an invalid input. Please try again \n")
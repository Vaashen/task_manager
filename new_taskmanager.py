from datetime import datetime 
from datetime import date


# creating a function called menu()
# in the function,
# the function will check which user is logged in
# if an admin is logged in they will be promted with a different menu then a normal user
def menu():
    while True:
        if login == 'admin':
            menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports 
ds - display statistics
e - Exit
Choose an option: ''').lower()

        else:
            menu = input('''\nSelect one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
Choose an option: ''').lower()
        
        # if the option chosen is 'r'
        # the register_user() function will be called
        if menu == 'r':
            register_user()
        
        # if the option chosen is 'a'
        # the add_task() function will be called   
        elif menu == 'a':
            add_task()
        
        # if the option chosen is 'va'
        # the view_all() will be called    
        elif menu == 'va':
            view_all()
        
        # if the option chosen is 'vm'
        # the view_mine() function will be called
        elif menu == 'vm':
            view_mine()
            
        elif menu == 'gr':
            generate_reports()
        
        # if the option chosen is 'stats'
        # the statistics() function will be called    
        elif menu == 'ds':
            statistics()
        
        # if the option chosen is 'e'
        # the indented statement will be displayed,
        # and it will exit the while loop   
        elif menu == 'e':
            print('Good Bye')
            exit()
        
        # if any other input is given 
        # the indented statement will be displayed
        else:
            print('Please choose an option from the menu.')
            
        return()


# creating another function called register_user()
# in this function,
# this function is only available for an admin 
# it will allow the admin to register a new user and password for that user 
# and will be able to write the information to the user.txt file
def register_user():
    while True:
        new_username = input("Enter a new username : ")
        new_password = input("Enter a new password : ")
        password_confirm = input('Confirm password : ')
        
        # creating a while loop within the if statement 
        # if the password and reconfirmation password entered by the user do not match
        # the user will be continuously asked to enter the password till they match
        while password_confirm != new_password:
            print("Please make sure you have entered the correct password!")
            reconfirm = input("Confirm password : ")
            
            # the while loop will only break once the password adn reconfirmation password match
            if reconfirm == new_password:
                break
        
        # formatting the username and password into one line
        info = f'\n{new_username}, {new_password}'
        
        # opening the user.txt file
        # writing the formatted lines into the txt file
        # closing the file once the line has been written
        # calling the menu() after that 
        f = open('user.txt', 'a')
        f.writelines(info)
        f.close()         
        menu()
        return()


# creating another function called add_task()
# in this function
# the user will be asked a couple questions relating to a task they want to add to the tasks.txt file
# once the user inputs all the answers 
# it will open the tasks.txt file adn write all the information in a neat, readable sentence in the txt file
def add_task():
    while True:
        title = input("Task name : ")
        user_name = input("Assigned to : ")
        date = input("Date Assigned : ")
        due_date = input("Due Date : ")
        task_complete = input("Task Completion ('Yes' or 'No') : ")
        description = input("Task Description : \n\t")
        
        # formatting the users details into one line
        task_info = f'\n{user_name}, {title}, {description}, {date}, {due_date}, {task_complete}'
         
        # opening the tasks.txt file 
        # writing the formatted line to the file
        # closing the file
        # calling the menu() again
        with open('tasks.txt', 'a') as f:
            f.writelines(task_info)

        menu()
        return()


# creating another function called view_all()
# in this function
# the function will open the tasks.txt file and split each line 
# the task will then take each index once the line is split and store it in a variable 
def view_all():
    with open('tasks.txt', 'r') as f:
        for line in f:
            information = line.split(',')
            task = information[1]
            name = information[0]
            description = information[2]
            date = information[3]
            due_date = information[4]
            complete = information[5]
                
            # formatting each word into the correct format required 
            task_detail = f''' ---------------------------------------------------------------------------
            \n\t\tTask : \t\t\t{task}
            \tAssigned to :  \t\t{name} 
            \tDate Assigned : \t{date}                            
            \tDue Date : \t\t{due_date}
            \tTask Completion : \t{complete}
            \tDescription : \n\t{description}
            -----------------------------------------------------------------'''
                
            # printing the formatted statement in a user-friendly manner
            print(task_detail) 
        
# calling the menu() function again
        menu()
        return()
  
  
# creating another function called view_mine()
# in this function
# the function will open the tasks.txt file and split the lines again
# it will then check if the first index of each line is the same name as the username of the user logged in
# it will then print out only the users tasks  
def view_mine():
    tasks = 0
    all_tasks = []
        
# opening the tasks.txt file
# using a for loop to read each line in the file
    with open('tasks.txt', 'r') as f:
        for line in f:
            info = line.strip().split(', ')
            all_tasks.append(info)
            
            # using an if statement to see which line is allocated to that username 
            if info[0] == login:
                tasks += 1
                
                # formatting the line into the correct format
                task_info = (f'''\nTask {tasks} : {info[1]}\n
                  Date Assigned : \t{info[3]}
                  Due Date : \t\t{info[4]}
                  Task Completed : \t\t{info[5]}
                  Task Description : \n\t{info[2]}''')

                # displaying all the users tasks in the formatted format
                print(task_info)
        
        # creating a while loop
        while True:
            # asking theuser to choose if they want to edit a task or return to main menu
            edit_task = input('''\nWould you like edit a task:
1 - edit a task
-1 - main menu
Choose an option: ''')
            
            # checking the users input
            # asking the user which task number they want to edit 
            if edit_task == '1':
                task_num = int(input('Give the number of the task you want to edit: '))
                task_num = task_num - 1
                
                # displaying another menu to the user, asking which edit option they want ot make on the task
                edit_menu = input('''\nWhat would you like to edit:
'm' - mark a task as complete
'user' - change the user to which the task is assigned to
'due date' - change the due date of a task
Choose an option: ''').lower()
                
                # checking if the task has already been completed
                if all_tasks[task_num][5] == 'Yes':
                    print('You cannot edit a completed task')
                
                # if task has not been completed 
                # check what edit option the user had chosen 
                if all_tasks[task_num][5] != 'Yes':
                    # marking a task complete
                    if edit_menu == 'm':
                        all_tasks[task_num][5] = 'Yes'
                    
                    # assigning a new user to the task that the user wants to edit
                    elif edit_menu == 'user':
                        new_user = input("Enter the user's name you want to assign to the task")
                        all_tasks[task_num][0] = new_user
                    
                    # changing the due date of the task the user wants to edit
                    elif edit_menu == 'due date':
                        new_due_date = input('Enter the new due date for this task: ')
                        all_tasks[task_num][4] = new_due_date
                    
                    else:
                        print('Please make sure you choose an option.')
            
            # if user chose -1, display the main menu
            elif edit_task == '-1':
                menu()

            else:
                print('Please choose from 1 or -1.')
            
            # writing the new changes back to the task.txt file
            with open('tasks.txt', 'r+') as file:
                for x in all_tasks:
                    x = ', '.join(x)
                    x = x + '\n'
                    file.write(x)

            return()
                    

# function for creating the task and user overview txt files
def generate_reports():
    num_tasks = 0
    completed_tasks = 0
    uncompleted_task = 0
    over_due_incomplete = 0
    user_task_dict = {}
    completed_task_dict = {}
    incomplete_task_dick = {}
    uncomplete_overdue_dict = {}

    with open('tasks.txt', 'r') as f:
        for line in f:
            num_tasks += 1
            line_list = line.strip().split(', ')
            name = line_list[0]
            
            # checking for any completed tasks
            if 'Yes' in line:
                completed_tasks += 1
            
            # checking for any incomplete tasks 
            if 'No' in line:
                uncompleted_task += 1
            
            # getting the date from the txt file adn converting it to a real date format
            over_due = line_list[4]
            over_due = datetime.strptime(over_due, "%d %b %Y").date()
            
            # checking for any tasks that are incomplete and overdue 
            if 'No' in line and over_due < date.today():
                over_due_incomplete += 1
            
            # Dictionary for total tasks assigned to the user
            if name in user_task_dict:
                user_task_dict[name] += 1
            else:
                user_task_dict[name] = 1
            
            # Dictionary for total tasks completed by the user
            if name in completed_task_dict:
                if line_list[5] == 'Yes':
                    completed_task_dict[name] += 1
            else:
                if line_list[5] == 'Yes':
                    completed_task_dict[name] = 1
            
            # Dictionary for tasks that are incomplete by the user
            if name in incomplete_task_dick:
                if line_list[5] == 'No':
                    incomplete_task_dick[name] += 1
            else:
                if line_list[5] == 'No':
                    incomplete_task_dick[name] = 1
            
            # Dictionary for incomplete and overdue tasks by the user
            if name in uncomplete_overdue_dict:
                if over_due < date.today():
                    if line_list[5] == 'No':
                        uncomplete_overdue_dict[name] += 1
            else:
                if over_due < date.today():
                    if line_list[5] == 'No': 
                        uncomplete_overdue_dict[name] = 1
        
        # calculating the percentages for the tasks that are incomplete and over due        
        percentage_incomplete = uncompleted_task / num_tasks * 100
        percentage_overdue = over_due_incomplete / num_tasks * 100
        
        # formatting the info in a user-friendly manner
        overview = f'''The total number of tasks: {num_tasks}
The total number of completed tasks: {completed_tasks}
The total number of incomplete tasks: {uncompleted_task}
The total number of incomplete and overdue tasks: {over_due_incomplete}
Percentage of incomplete tasks: {round(percentage_incomplete, 2)}%
Percentage of overdue tasks: {round(percentage_overdue, 2)}%'''
        
        # writing the info to the task_overview.txt file
        with open('task_overview.txt', 'w') as f:
            f.write(overview)
    
    # opening the user_overview.txt file
    with open('user_overview.txt', 'w') as output:
        with open('user.txt', 'r') as f:
            num_user = 0
            for line in f:
                num_user += 1
        
        # writing the total number of users
        output.write(f'Total number of users: {num_user}')
        output.write(f'\nTotal number of tasks: {num_tasks}')
        
        # calculating the percentages of the total amount of tasks assigned to a user
        # calculating the total number of tasks assigned to a user 
        for name in user_task_dict.keys():
            num_task_per_user = user_task_dict[name]
            percentage_vs_total_tasks = num_task_per_user / num_tasks * 100
            output.write(f'\nUser {name} has {num_task_per_user} tasks')
            output.write(f'- This is {round(percentage_vs_total_tasks, 2)}% of the total number of tasks')
        
        # calculating what percentage of tasks are completed by the assigned user 
        for name in completed_task_dict.keys():
            completed_task_per_user = completed_task_dict[name]
            percentage_per_user = completed_task_per_user / num_tasks * 100 
            output.write(f'\nUser {name} has completed {round(percentage_per_user, 2)}% of the total tasks')
        
        # calculating the percentage of incomplete tasks by the assigned user   
        for name in incomplete_task_dick.keys():
            num_incomplete_task_user = incomplete_task_dick[name]
            percentage_incomplete = num_incomplete_task_user / num_tasks * 100
            output.write(f'\n\nUser {name} has {round(percentage_incomplete, 2)}% of incomplete tasks')
        
        # calculating the percentage of uncompleted and overdue tasks assigned to a user 
        for name in uncomplete_overdue_dict.keys():
            uncompleted = uncomplete_overdue_dict[name]
            percentage_uncomplete = uncompleted / num_tasks * 100 
            output.write(f'\nUser {name} has {round(percentage_uncomplete, 2)}% of tasks that are incomplete and overdue')
    
    menu()
    return()


# creating another function called statistics()
# this function will only be available for the admin
# it will display the number of users saved in the user.txt file 
# it will also display all the tasks in the tasks.txt file  
def statistics():
    print('-------Task Overview-------')
    with open('task_overview.txt', 'r') as f:
        for line in f:
            print(line)
    
    print('\n\n-------User Overview-------')           
    with open('user_overview.txt', 'r') as file:
        for line in file:
            print(line)
    
    menu()
    return()


# opening the user.txt file
# creating an empty dictionary
# then splitting each line in the txt file
# storing the first index (username) as a key in the dictionary
# storing the second index (password) as a value for the relevant key
with open('user.txt', 'r+') as file:
    usernames_and_passwords = {}
    
    for lines in file.readlines():
        line = lines.strip().split(', ')
        usernames = line[0]
        passwords = line[1]
        usernames_and_passwords[usernames] = passwords

# creating a while loop
# in the while loop 
# the user will be asked to enter their username and password
# it will use an if statement to read through the dictionary above
# it will check if the username entered is valid and that the password corresponds with the username
# it will then call the menu function 
# if either the username or password is incorrect, the menu function will not be displayed 
# until it is correct             
while True:
    login = input('\nEnter your username: ')
    login_pass = input('Enter your password: ')
    
    if usernames_and_passwords.get(login) == login_pass:
        print('Welcome. You have successfully logged in.')
        menu()

    else:
        print('The username or password you have entered is incorrect. Please Try again.')
        
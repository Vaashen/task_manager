# task_manager

<!--Introduction-->

> This project contains a simple Task manger program. The program will be able to :

* register new users
* add a task
* view all
* view mine/ mark the task as complete
* generate reports 
* Show Statistics

This program will read and write from and to, two different text files called, tasks.txt and user.txt. Tasks.txt will contain all the tasks assigned to every user and user.txt will contain the login details for each user (username and password).

The user.txt file will already contain the login details for the admin by default, you can choose to keep it or change it, however this will require you to make a few cahanges in the code itself.

If a admin logs in they will have full access to the options listed above, if they choose to generate reports, two new files will be generated, task_overview.txt and user_overview.txt. 

However if a normal user logs in they will only be able to: add a task, view all tasks, and  view mine.

<!--Instructions-->
<br>

>## How to run the Program
First you will need to create a folder, and inside the folder, copy and paste the task_manager.py, tasks.txt and user.txt files in it.

Next you will need an editor to run the program on, I would strongly recommend you use Visual Studio Code, as it is very easy and simple to use and setup.if you do not have VSC installeed on your device, tap [here](https://code.visualstudio.com/download) to download it, click on the device you are using and wait for it to download, once done, open and follow the setup instructions.

In VSC, on the top left hand side, you will see a tap called "File" tap on it and select "Open Folder". Find the folder you created that contians the files and double click on that folder. Your VSC should now have the files openeed on the left and side.

if you tap on the user.txt file you will see admin is  already there, this is the default login details for the admin, you can change it to whatever you feel comfortable with, **note that admin is the username and adm1n is the password. if you do dedcide to change these details, tap on the task_manager.py file and look at line 11 of the code, you will see admin there, change it to the new admin username you have choosen.**

Now to actually run the code, on the top rigth had side , you will see what looks like a play button, tap in it and it should open up the therminal, this is where you willbe asked to login in, if there are no other users besides the admin one, login in using the your admin details. You will then be promted with a menu, play around with it to get used to what each function does.

<br>

>## Link to my Repo
You can find my repository [here](https://github.com/Vaashen/task_manager)

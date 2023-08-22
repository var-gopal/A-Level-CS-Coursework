# datetime  library for access to datetime  related functions  for date manipulation
import datetime
import hashlib  # importing  hashlib library for access to MD5 encryption  of passwords
import os  # importing  os library to clear screen at appropriate  times

import mysql.connector  # importing  mysql.connector  library to connect to database
import prettytable  # importing  prettytable  library for output formatting

db = mysql.connector.connect(
    user="root", password="abcd4321", host="localhost", database="coursework"
)  # assigning  variable  as database  connector
cursor = db.cursor()  # assigning  variable  as database  cursor


class User:  # User Class
    @staticmethod
    def set_name(user_count, name):  # function  to add name of user to the database
        # SQL query to update the name column in the user table
        sql = "UPDATE user SET Name = %s WHERE UID = %s"
        val = (name, user_count)
        cursor.execute(sql, val)  # executes  the SQL query along with the value
        db.commit()  # enforces  the required  changes to the database

    @staticmethod
    def set_age(
        user_count, age
    ):  # function  to add the age of the user to the database
        sql = "UPDATE user SET Age = %s WHERE UID = %s"
        val = (age, user_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add username  of the user to the database
    def set_username(user_count, username):
        sql = "UPDATE user SET UName = %s WHERE UID = %s"
        val = (username, user_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_password(user_count):  # function  to set the user's  password
        valid = False  # boolean value that indicates  the validity  of the password
        password = ""
        while not valid:
            password = input("Please enter a new password:  ")
            uppercase = (
                0  # stores the numbers of uppercase  characters  in the password
            )
            lowercase = (
                0  # stores the numbers of lowercase  characters  in the password
            )
            digit = 0  # stores the numbers of digits in the password
            length = True  # boolean value indicating  whether the password  meets the minimum length
            for (
                x
            ) in password:  # looping through each character  in the entered password
                if x.isdigit():  # checking  if the selected  character  is a digit
                    digit += 1
                else:
                    if 65 <= ord(x) <= 90:  # checking  for uppercase  characters
                        uppercase += 1
                    elif 97 <= ord(x) <= 122:  # checking  for lowercase  characters
                        lowercase += 1
            if (
                len(password) < 8
            ):  # checking  if the password  meets the minimum length requirement
                length = False
            if (not length) or (digit < 1) or (uppercase < 1) or (lowercase < 1):
                valid = False
                print("Invalid  Password.")
                print("Password  must meet the following  conditions:  ")
                print("1) Have at least 1 digit.")
                print("2) Have at least 1 uppercase  letter.")
                print("3) Have at least 1 lowercase  letter.")
                print("4) Have a minimum length of 8 characters.")
                print("Try Again.")
            else:
                valid = True
        password_confirm = input("Please enter your password again: ")
        # password  re-entry for confirmation

        while password != password_confirm:  # password  confirmation
            print("Passwords  do not match.")
            password = input("Enter a new password:  ")
            password_confirm = input("Enter your password  again for confirmation:  ")

        # hashing the password  using MD5 encryption  from the hashlib library
        hashed = hashlib.md5(password.encode())
        sql = "UPDATE user SET HashVal = %s WHERE UID = %s"
        val = (hashed.hexdigest(), user_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def change_password(current_user_id):  # function  to change password
        old = input("Enter current password:  ")
        # accepting  original  password  for confirmation  before change
        # calling function  the verify password
        while not User.check_password(old, current_user_id):
            old = input("Incorrect  Password.  Try again: ")

        # calling function  to set new password
        User.set_password(current_user_id)

    @staticmethod
    def check_password(password, current_user_id):
        hashed = (hashlib.md5(password.encode())).hexdigest()
        # hashing input password  for comparison  with hashed value
        sql = "SELECT HashVal FROM user WHERE UID = %s "
        val = (current_user_id,)
        cursor.execute(sql, val)
        real_password = cursor.fetchall()  # retrieving  the hash from the database
        # comparing  stored hash to generated  hash
        if hashed == real_password[0][0]:
            return True
        else:
            return False


class Event:  # Event Class
    @staticmethod
    def set_name(
        event_count, name
    ):  # function  to add the name of the event to the database
        sql = "UPDATE event SET EName = %s WHERE EID = %s"
        val = (name, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the start time to the database
    def set_start_time(event_count, start_time):
        sql = "UPDATE event SET ESTime = %s WHERE EID = %s"
        val = (start_time, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the end time to the database
    def set_end_time(event_count, end_time):
        sql = "UPDATE event SET EETime = %s WHERE EID = %s"
        val = (end_time, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the start date the database
    def set_start_date(event_count, start_date):
        sql = "UPDATE event SET ESDate = %s WHERE EID = %s"
        val = (start_date, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the end date to the database
    def set_end_date(event_count, end_date):
        sql = "UPDATE event SET EEDate = %s WHERE EID = %s"
        val = (end_date, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the all day value to the database
    def set_all_day(event_count, all_day):
        sql = "UPDATE event SET AllDay = %s WHERE EID = %s"
        val = (all_day, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_busy(
        event_count, busy
    ):  # function  to add the busy value of the event to the database
        sql = "UPDATE event SET Busy = %s WHERE EID = %s"
        val = (busy, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the notes about the event to the database
    def set_notes(event_count, notes):
        sql = "UPDATE event SET Notes = %s WHERE EID = %s"
        val = (notes, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add repeat cycle to the database
    def set_repeat(event_count, event_repeat):
        sql = "UPDATE event SET ERepeat = %s WHERE EID = %s"
        val = (event_repeat, event_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add repeat id to the database
    def set_repeat_id(event_count, event_repeat_id):
        sql = "UPDATE event SET ERepeatID  = %s WHERE EID = %s"
        val = (event_repeat_id, event_count)
        cursor.execute(sql, val)
        db.commit()


class Task:  # Task Class
    @staticmethod
    def set_name(
        task_count, name
    ):  # function  to add the name of the task to the database
        sql = "UPDATE task SET TName = %s WHERE TID = %s"
        val = (name, task_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_date(
        task_count, date
    ):  # function  to add the date of the task to the database
        sql = "UPDATE task SET TDate = %s WHERE TID = %s"
        val = (date, task_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_priority(
        task_count, priority
    ):  # function  to add the priority  to the database
        sql = "UPDATE task SET Priority  = %s WHERE TID = %s"
        val = (int(priority), task_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_notes(
        task_count, notes
    ):  # function  to add notes about the task to the database
        sql = "UPDATE task SET Notes = %s WHERE TID = %s"
        val = (notes, task_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add the repeat cycle to the database
    def set_repeat(task_count, task_repeat):
        sql = "UPDATE task SET TRepeat = %s WHERE TID = %s"
        val = (task_repeat, task_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    # function  to add repeat id to the database
    def set_repeat_id(task_count, task_repeat_id):
        sql = "UPDATE task SET TRepeatID  = %s WHERE TID = %s"
        val = (task_repeat_id, task_count)
        cursor.execute(sql, val)
        db.commit()


class EPlan:  # Event Plan Class
    @staticmethod
    def set_name(event_plan_count, name):  # function  to add the name to the database
        sql = "UPDATE eplan SET EPName = %s WHERE EPID = %s"
        val = (name, event_plan_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_repeat(event_plan_count, event_plan_repeat):
        # function to add the repeat cycle to the database
        sql = "UPDATE eplan SET EPRepeat  = %s WHERE EPID = %s"
        val = (event_plan_repeat, event_plan_count)
        cursor.execute(sql, val)
        db.commit()

    @staticmethod
    def set_repeat_id(event_plan_count, event_plan_repeat_id):
        # function  to add the repeat id to the database
        sql = "UPDATE eplan SET EPRepeatID  = %s WHERE EPID = %s"
        val = (event_plan_repeat_id, event_plan_count)
        cursor.execute(sql, val)
        db.commit()


class Calendar:  # Calendar  Class
    user_obj = User()  # object to access data and methods of the user class
    event_obj = Event()  # object to access data and methods of the event class
    task_obj = Task()  # object to access data and methods of the task class
    # object to access data and methods of the event plan class
    event_plan_object = EPlan()

    # setting the number users in the database  at the start of the program
    try:
        sql = "SELECT MAX(UID)  FROM user"
        cursor.execute(sql)
        user_count = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        user_count = 1

    # setting the number events in the database  at the start of the program
    try:
        sql = "SELECT MAX(EID)  FROM event"
        cursor.execute(sql)
        event_count = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        event_count = 1

    # setting the number tasks in the database  at the start of the program
    try:
        sql = "SELECT MAX(TID) FROM task"
        cursor.execute(sql)
        task_count = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        task_count = 1

    # setting the number event plans in the database  at the start of the program
    try:
        sql = "SELECT MAX(EPID)  FROM eplan"
        cursor.execute(sql)
        event_plan_count = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        event_plan_count = 1

    try:
        sql = "SELECT MAX(ERepeatID)  FROM event"
        cursor.execute(sql)
        current_repeat_id = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        current_repeat_id = 1

    try:
        sql = "SELECT MAX(TRepeatID)  FROM task"
        cursor.execute(sql)
        if int(cursor.fetchall()[0][0]) > current_repeat_id:
            sql = "SELECT MAX(TRepeatID)  FROM task"
            cursor.execute(sql)
            current_repeat_id = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        current_repeat_id = current_repeat_id

    try:
        sql = "SELECT MAX(EPRepeatID)  FROM eplan"
        cursor.execute(sql)
        if int(cursor.fetchall()[0][0]) > current_repeat_id:
            sql = "SELECT MAX(EPRepeatID)  FROM eplan"
            cursor.execute(sql)
            current_repeat_id = int(cursor.fetchall()[0][0]) + 1
    except TypeError:
        current_repeat_id = current_repeat_id

    current_user_id = 0
    # initializing  the current user id variable  so it can be accessed  be all methods in the class
    date_format = "%Y-%m-%d"

    def main_menu(self):  # function containing  all menus of the program
        choice = 1
        while choice != 4:  # loop for first menu
            os.system("cls")
            print("Options:  ")
            print("1) Create New User")
            print("2) Login")
            print("3) Delete User")
            print("4) Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                choice = 0
            os.system("cls")
            if choice == 1:
                self.__create_new_user()
                input("Press Enter to Continue.")
            elif choice == 2:
                if self.__login():
                    choice_1 = 1
                    while choice_1 != 6:  # loop for second (main) menu
                        os.system("cls")
                        print("Main Menu: ")
                        print("1) Events")
                        print("2) Tasks")
                        print("3) Event Plans")
                        print("4) Delete All Data")
                        print("5) Change Password")
                        print("6) Log Out")
                        try:
                            choice_1 = int(input("Enter your choice: "))
                        except ValueError:
                            choice_1 = 0
                        os.system("cls")
                        choice_2 = 1
                        if choice_1 == 1:
                            # loop for first submenu (events)
                            while choice_2 != 6:
                                os.system("cls")
                                print("Events Menu: ")
                                print("1) New Event")
                                print("2) Show All Events")
                                print("3) Search Events")
                                print("4) Edit An Event")
                                print("5) Delete An Event")
                                print("6) Back To Main Menu")
                                try:
                                    choice_2 = int(input("Enter your choice: "))
                                except ValueError:
                                    choice_2 = 0
                                os.system("cls")
                                if choice_2 == 1:
                                    self.__create_new_event()
                                elif choice_2 == 2:
                                    self.__show_events()
                                elif choice_2 == 3:
                                    self.__search_event()
                                elif choice_2 == 4:
                                    self.__edit_event()
                                elif choice_2 == 5:
                                    self.__delete_event()
                                elif choice_2 < 1 or choice_2 > 6:
                                    print("Invalid  Input. Try Again.")
                                input("Press Enter to Continue.")
                        elif choice_1 == 2:
                            # loop for second submenu (tasks)
                            while choice_2 != 7:
                                os.system("cls")
                                print("Tasks Menu: ")
                                print("1) New Task")
                                print("2) Show All Tasks")
                                print("3) Complete  A Task")
                                print("4) Search Tasks")
                                print("5) Edit A Task")
                                print("6) Delete A Task")
                                print("7) Back To Main Menu")
                                try:
                                    choice_2 = int(input("Enter your choice: "))
                                except ValueError:
                                    choice_2 = 0
                                os.system("cls")
                                if choice_2 == 1:
                                    self.__create_new_task()
                                elif choice_2 == 2:
                                    self.__show_tasks()
                                elif choice_2 == 3:
                                    self.__complete_task()
                                elif choice_2 == 4:
                                    self.__search_task()
                                elif choice_2 == 5:
                                    self.__edit_task()
                                elif choice_2 == 6:
                                    self.__delete_task()
                                elif choice_2 < 1 or choice_2 > 7:
                                    print("Invalid  Input. Try Again.")
                                input("Press Enter to Continue.")
                        elif choice_1 == 3:
                            # loop for third submenu (event plans)
                            while choice_2 != 6:
                                os.system("cls")
                                print("Event Plans Menu: ")
                                print("1) New Event Plan")
                                print("2) Show All Event Plans")
                                print("3) Search Event Plans")
                                print("4) Edit An Event Plan")
                                print("5) Delete An Event Plan")
                                print("6) Back To Main Menu")
                                try:
                                    choice_2 = int(input("Enter your choice: "))
                                except ValueError:
                                    choice_2 = 0
                                os.system("cls")
                                if choice_2 == 1:
                                    self.__create_new_event_plan()
                                elif choice_2 == 2:
                                    self.__show_event_plans()
                                elif choice_2 == 3:
                                    self.__search_event_plan()
                                elif choice_2 == 4:
                                    self.__edit_event_plan()
                                elif choice_2 == 5:
                                    self.__delete_event_plan()
                                elif choice_2 < 1 or choice_2 > 6:
                                    print("Invalid  Input. Try Again.")
                                input("Press Enter to Continue.")
                        elif choice_1 == 4:
                            self.__delete_all_data()
                            input("Press Enter to Continue.")
                        elif choice_1 == 5:
                            self.user_obj.change_password(self.current_user_id)
                            # calling function  to change password
                            input("Press Enter to Continue.")
                        elif choice_1 == 6:
                            self.current_user_id = 0
                            print("Logged out.")
                            input("Press Enter to Continue.")
                        else:
                            print("Invalid  Input. Try Again.")
                            input("Press Enter to Continue.")
            elif choice == 3:
                self.__delete_user()
                input("Press Enter to Continue.")
            elif choice == 4:
                print("Goodbye.")
                input("Press Enter to Continue.")
            else:
                print("Invalid  Input. Try Again.")
                input("Press Enter to Continue.")

    def __create_new_user(self):  # function  to create a new event
        # adding default values for the user in the database
        sql = "INSERT INTO user(Name,  Age, UName, HashVal)  VALUES (%s , %s , %s , %s)"
        val = ("", 0, "", "")
        cursor.execute(sql, val)
        db.commit()

        # accepting  name of event from user   55
        name = input("Please enter your full name: ")
        # checking  for errors in input
        while not self.__error_checker("Blank", name):
            name = input("You entered a blank. Try again: ")

        # calling function  to add name to database
        self.user_obj.set_name(self.user_count, name)

        valid = False  # variable  to indicate  whether age is a valid integer value
        age = 0
        while not valid:
            try:
                age = int(input("Please enter your age: "))
                valid = True
            except ValueError:
                print("Invalid  entry.")
                valid = False

        # calling function  to add age to database
        self.user_obj.set_age(self.user_count, age)

        username = input("Please an appropriate  username:  ")
        while not self.__error_checker("Blank", username):
            # checking  whether the input username  is blank
            username = input("You entered a blank. Try again: ")

        self.user_obj.set_username(self.user_count, username)
        # calling function  to add username  to database

        self.user_obj.set_password(self.user_count)
        # calling function  to set and add password  to database

        self.user_count += 1  # adding to user count

    def __login(self):
        # checking  validity  of username
        username = input("Please enter your username:  ")
        while not self.__error_checker("Blank", username):
            username = input("You entered a blank. Try again: ")

        username_validation = False
        sql = "SELECT UName FROM user"
        cursor.execute(sql)
        username_list = cursor.fetchall()

        for (
            x
        ) in (
            username_list
        ):  # loop to check if the entered username  exists in the database
            for y in x:
                if username == y:
                    username_validation = True
                    break
                else:
                    continue
            if username_validation:
                break

        # checking  validity  of password
        password = input("Please enter your password:  ")
        if username_validation:
            sql = "SELECT HashVal FROM user WHERE UName = %s"
            val = (username,)
            cursor.execute(sql, val)
            # checking  whether hash from database  matches hash of entered password
            if (cursor.fetchall()[0][0]) == (
                hashlib.md5(password.encode())
            ).hexdigest():
                sql = "SELECT UID FROM user WHERE UName = %s"
                val = (username,)
                cursor.execute(sql, val)
                self.current_user_id = int(cursor.fetchall()[0][0])
                print("Successful  Login.")
                return True
            else:
                print("Login Unsuccessf ul.")
                print("Invalid  Username  or Password.")
                return False
        else:
            print("Login Unsuccessful.")
            print("Invalid  Username  or Password.")
            return False

    def __create_new_event(self):
        # inserting  default values for the event in the database
        sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat, ERepeatID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (
            "",
            "00:00:00 ",
            "00:00:00 ",
            "2000-01-01",
            "2000-01-01",
            0,
            0,
            "",
            "",
            0,
        )
        cursor.execute(sql, val)
        db.commit()

        # adding the name of the event
        name = input("Please enter the name of the event: ")
        while not self.__error_checker("Blank", name):
            name = input("You entered a blank. Try again: ")

        self.event_obj.set_name(self.event_count, name)

        # adding the all day property  of the event
        all_day = (input("Is the event an All Day event (Y/N): ")).upper()
        while self.__error_checker("Bool", all_day) == "Invalid":
            print("Invalid  Input. Try Again")
            all_day = (input("Is the event an All Day event (Y/N): ")).upper()

        all_day = self.__error_checker("Bool", all_day)
        self.event_obj.set_all_day(self.event_count, int(all_day))

        if all_day == "0":
            # adding the start date of the event
            start_date = input("Enter the start date for the event (YYYY-MM-DD): ")
            while not self.__error_checker("Date", start_date):
                print("Invalid  Format. Try Again.")
                start_date = input("Enter the start date again (YYYY-MM-DD): ")
            self.event_obj.set_start_date(self.event_count, start_date)

            # adding the end date of the event
            end_date = input("Enter the end date for the event (YYYY-MM-DD): ")
            overlap = True
            while overlap:
                while not self.__error_checker("Date", end_date):
                    print("Invalid  Format. Try Again.")
                    end_date = input("Enter the end date again (YYYY-MM-DD): ")
                overlap = self.__error_checker("Overlap  Date", start_date, end_date)
                if overlap:
                    print("End date cannot be earlier than start date. Try Again.")
                    end_date = input("Enter the end date again (YYYY-MM-DD): ")

            self.event_obj.set_end_date(self.event_count, end_date)

            # adding the start time of the event
            start_time = input("Enter the start time for the event (HH:mm:ss):  ")
            while not self.__error_checker("Time", start_time):
                print("Invalid  Format. Try Again.")
                start_time = input("Enter the start time for the event (HH:mm:ss):  ")

            self.event_obj.set_start_time(self.event_count, start_time)

            # adding the end time of the event
            end_time = input("Enter the end time for the event (HH:mm:ss):  ")
            overlap = True
            while overlap:
                while not self.__error_checker("Time", end_time):
                    print("Invalid  Format. Try Again.")
                    end_time = input("Enter the end time for the event (HH:mm:ss):  ")

                overlap = self.__error_checker("Overlap  Time", start_time, end_time)
                if overlap:
                    print("End tIme cannot be earlier than start time. Try Again.")
                    end_time = input("Enter the end time again (HH:mm:ss):  ")

            self.event_obj.set_end_time(self.event_count, end_time)
        else:
            # adding a single date for both start and end date as the event is an all day event
            date = input("Enter the date for the event (YYYY-MM-DD): ")
            while not self.__error_checker("Date", date):
                print("Invalid  Format. Try Again.")
                date = input("Enter the date again (YYYY-MM-DD): ")

            self.event_obj.set_start_date(self.event_count, date)
            self.event_obj.set_end_date(self.event_count, date)
            self.event_obj.set_end_time(self.event_count, "23:59:59")

        # adding the busy property  of the event
        busy = (input("Will you be busy during the event (Y/N): ")).upper()
        while self.__error_checker("Bool", busy) == "Invalid":
            print("Invalid  Input. Try Again")
            busy = (input("Will you be busy during the event (Y/N): ")).upper()

        busy = self.__error_checker("Bool", busy)
        self.event_obj.set_busy(self.event_count, int(busy))

        # adding notes regarding  the event
        print("Add notes (1000 character  limit): ")
        notes = input("")
        while not self.__error_checker("Notes", notes):
            print("Character  limit exceeded.  Try Again: ")
            notes = input("")

        self.event_obj.set_notes(self.event_count, notes)

        # adding the repeat cycle of the event
        event_repeat = input(
            "Enter repeat cycle (None, Daily, Weekly, Monthly,  Yearly):  "
        ).upper()
        while not self.__error_checker("Repeat", event_repeat):
            print("Invalid  Input. Try Again.")
            event_repeat = input(
                "Enter repeat cycle again (None, Daily, Weekly, Monthly,  Yearly):  "
            ).upper()

        self.event_obj.set_repeat(self.event_count, event_repeat)
        self.event_obj.set_repeat_id(self.event_count, self.current_repeat_id)

        # adding the event id and its user id to the user and event link table in the database
        sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
        val = (self.current_user_id, self.event_count)
        cursor.execute(sql, val)
        db.commit()

        self.event_count += 1
        self.__event_repeater(self.event_count - 1)

    def __create_new_task(self):
        # adding the default values for the task to the database
        sql = "INSERT  INTO task(TName,  TDate, Priority,  Notes, TRepeat,  Completed,  TRepeatID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = ("", "2000-1-1", 0, "", "", 0, 0)
        cursor.execute(sql, val)
        db.commit()

        # adding the name of the task
        name = input("Please enter the name of the task: ")
        while not self.__error_checker("Blank", name):
            name = input("You entered a blank. Try again: ")

        self.task_obj.set_name(self.task_count, name)

        # adding the date of the task
        date = input("Enter the date for the event (YYYY-MM-DD): ")
        while not self.__error_checker("Date", date):
            print("Invalid  Format. Try Again.")
            date = input("Enter the end date again (YYYY-MM-DD): ")

        self.task_obj.set_date(self.task_count, date)

        # adding the priority  if the task
        priority = input(
            "Enter the priority  of the task (0-lowest, 1, 2, 3-highest):  "
        )
        valid = False
        while (
            not valid
        ):  # loop to check whether the user inputted  a valid priority  level
            if priority in ["0", "1", "2", "3"]:
                valid = True
            else:
                valid = False
                print("Invalid  Input. Try Again.")
                priority = input(
                    "Enter the priority  of the task again (0-lowest, 1, 2, 3-highest):  "
                )

        self.task_obj.set_priority(self.task_count, int(priority))

        # adding notes regarding  the task
        print("Add notes (1000 character  limit): ")
        notes = input("")
        while not self.__error_checker("Notes", notes):
            print("Character  limit exceeded.  Try Again: ")
            notes = input("")

        self.task_obj.set_notes(self.task_count, notes)

        # adding the repeat cycle for the task
        task_repeat = input(
            "Enter repeat cycle (None, Daily, Weekly, Monthly,  Yearly):  "
        ).upper()
        while not self.__error_checker("Repeat", task_repeat):
            print("Invalid  Input. Try Again.")
            task_repeat = input(
                "Enter repeat cycle again (None, Daily, Weekly, Monthly,  Yearly):  "
            ).upper()

        self.task_obj.set_repeat(self.task_count, task_repeat)
        self.task_obj.set_repeat_id(self.task_count, self.current_repeat_id)

        # adding the task id and its respective  user id to the link table in the database
        sql = "Insert into userandtasklink  (UID, TID) VALUES (%s, %s)"
        val = (self.current_user_id, self.task_count)
        cursor.execute(sql, val)
        db.commit()

        self.task_count += 1
        self.__task_repeater(self.task_count - 1)

    def __create_new_event_plan(self):
        # adding the default values of the event plan to the database
        sql = "INSERT INTO eplan(EPName,  EPRepeat,  EPRepeatID)  VALUES (%s, %s, %s)"
        val = ("", "", 0)
        cursor.execute(sql, val)
        db.commit()

        # adding the name of the event plan
        name = input("Please enter the name of the event plan: ")
        while not self.__error_checker("Blank", name):
            name = input("You entered a blank. Try again: ")

        self.event_plan_object.set_name(self.event_plan_count, name)

        # adding the repeat cycle of the event plan
        event_plan_repeat = input(
            "Enter repeat cycle (None, Daily, Weekly, Monthly,  Yearly):  "
        ).upper()
        while not self.__error_checker("Repeat", event_plan_repeat):
            print("Invalid  Input. Try Again.")
            event_plan_repeat = input(
                "Enter repeat cycle again (None, Daily, Weekly, Monthly,  Yearly):  "
            ).upper()

        self.event_plan_object.set_repeat(self.event_plan_count, event_plan_repeat)
        self.event_plan_object.set_repeat_id(
            self.event_plan_count, self.current_repeat_id
        )

        print("Options:  ")
        print("1) Create new events")
        print("2) Add existing  events")
        choice = 0
        valid = False  # indicates  the validity  of the input of the user
        while not valid:
            try:
                choice = int(input("Enter your choice: "))
                valid = True
            except ValueError:
                print("Invalid  Input. Try Again.")
                valid = False

        if choice == 1:  # option for new events
            num_of_events = 0
            valid = False
            while not valid:
                try:
                    num_of_events = int(
                        input("How many events would you like to create: ")
                    )
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            for i in range(num_of_events):
                print("Event " + str(i + 1) + ": ")
                self.__create_new_event()
                sql = "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                val = (self.event_plan_count, self.event_count - 1)
                cursor.execute(sql, val)
                db.commit()

            if (
                input("Would you like to add some existing  events as well (Y/N)?")
            ).upper() == "Y":
                sql = "SELECT EID FROM userandeventlink  WHERE UID = %s"
                val = (self.current_user_id,)
                cursor.execute(sql, val)
                valid_events = cursor.fetchall()

                self.__show_events()
                print(
                    "Adding existing  events to event plan: (Press enter if you are done adding events)"
                )
                for i in range(len(valid_events)):
                    temp = input(
                        "Enter the ID of event "
                        + str(i + 1)
                        + " to add to the event plan: "
                    )
                    if temp.isnumeric():
                        if (int(temp),) in valid_events:
                            sql = "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                            val = (self.event_plan_count, int(temp))
                            cursor.execute(sql, val)
                            db.commit()
                        else:
                            print(temp + " is not a valid id.")
                    elif temp.strip() == "":
                        break
                    else:
                        mistype = ""
                        valid = False
                        while not valid:
                            mistype = input(
                                "Did you mistype an event ID? (Yes/No)"
                            ).upper()
                            if (
                                mistype == "YES"
                                or mistype == "Y"
                                or mistype == "NO"
                                or mistype == "N"
                            ):
                                valid = True
                            else:
                                print("Invalid  Input. Try Again.")
                                valid = False
                        if mistype == "YES" or mistype == "Y":
                            i -= 1
                        elif mistype == "NO" or mistype == "N":
                            break

        elif choice == 2:  # option for pre-existing  events
            sql = "SELECT EID FROM userandeventlink  WHERE UID = %s"
            val = (self.current_user_id,)
            cursor.execute(sql, val)
            valid_events = cursor.fetchall()

            self.__show_events()
            print(
                "Adding existing  events to event plan: (Press enter if you are done adding events)"
            )

            for i in range(len(valid_events)):
                temp = input(
                    "Enter the ID of event "
                    + str(i + 1)
                    + " to add to the event plan: "
                )
                if temp.isnumeric():
                    if (int(temp),) in valid_events:
                        sql = (
                            "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                        )
                        val = (self.event_plan_count, int(temp))
                        cursor.execute(sql, val)
                        db.commit()
                    else:
                        print(temp + " is not a valid id.")
                elif temp.strip() == "":
                    break
                else:
                    valid = False
                    while not valid:
                        mistype = input("Did you mistype an event ID? (Yes/No)").upper()
                        if mistype == "YES" or mistype == "Y":
                            i -= 1
                        elif mistype == "NO" or mistype == "N":
                            break
                        else:
                            print("Invalid  Input. Try Again.")

        sql = "Insert into userandeplanlink  (UID, EPID) VALUES (%s, %s)"
        val = (self.current_user_id, self.event_plan_count)
        cursor.execute(sql, val)
        db.commit()

        self.event_plan_count += 1
        self.__event_plan_repeater(self.event_plan_count - 1)

    def __event_repeater(self, event_id):
        sql = "SELECT  * FROM event WHERE EID = %s"
        val = (event_id,)
        cursor.execute(sql, val)
        selected_event = cursor.fetchall()

        name = selected_event[0][1]
        start_time = selected_event[0][2]
        end_time = selected_event[0][3]
        start_date = selected_event[0][4]
        end_date = selected_event[0][5]
        all_day = selected_event[0][6]
        busy = selected_event[0][7]
        notes = selected_event[0][8]
        repeat_cycle = selected_event[0][9]
        repeat_id = selected_event[0][10]

        if repeat_cycle is not "NONE":
            if repeat_cycle == "DAILY":
                for i in range(364):
                    start_date += datetime.timedelta(days=1)
                    end_date += datetime.timedelta(days=1)
                    sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat, ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        start_time,
                        end_time,
                        start_date.strftime(self.date_format),
                        end_date.strftime(self.date_format),
                        all_day,
                        busy,
                        notes,
                        repeat_cycle,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding event id and user id to the userandeventlink  table in the database
                    sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_count += 1
            elif repeat_cycle == "WEEKLY":
                for i in range(51):
                    start_date += datetime.timedelta(days=7)
                    end_date += datetime.timedelta(days=7)
                    sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat, ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        start_time,
                        end_time,
                        start_date.strftime(self.date_format),
                        end_date.strftime(self.date_format),
                        all_day,
                        busy,
                        notes,
                        repeat_cycle,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding event id and user id to the userandeventlink  table in the database
                    sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_count += 1
            elif repeat_cycle == "MONTHLY":
                for i in range(59):
                    start_date += datetime.timedelta(days=28)
                    end_date += datetime.timedelta(days=28)
                    sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat, ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        start_time,
                        end_time,
                        start_date.strftime(self.date_format),
                        end_date.strftime(self.date_format),
                        all_day,
                        busy,
                        notes,
                        repeat_cycle,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding event id and user id to the userandeventlink  table in the database
                    sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_count += 1
            elif repeat_cycle == "YEARLY":
                for i in range(49):
                    start_date += datetime.timedelta(days=365)
                    end_date += datetime.timedelta(days=365)
                    sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat, ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        start_time,
                        end_time,
                        start_date.strftime(self.date_format),
                        end_date.strftime(self.date_format),
                        all_day,
                        busy,
                        notes,
                        repeat_cycle,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding event id and user id to the userandeventlink  table in the database
                    sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_count += 1
            self.current_repeat_id += 1

    def __task_repeater(self, task_id):
        sql = "SELECT  * FROM task WHERE TID = %s"
        val = (task_id,)
        cursor.execute(sql, val)
        selected_task = cursor.fetchall()

        name = selected_task[0][1]
        date = selected_task[0][2]
        priority = selected_task[0][3]
        notes = selected_task[0][4]
        repeat_cycle = selected_task[0][5]
        completion = selected_task[0][6]
        repeat_id = selected_task[0][7]

        if repeat_cycle is not "NONE":
            if repeat_cycle == "DAILY":
                for i in range(364):
                    date += datetime.timedelta(days=1)
                    sql = "INSERT  INTO task(TName,  TDate, Priority,  Notes, TRepeat,  Completed, TRepeatID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        date.strftime(self.date_format),
                        priority,
                        notes,
                        repeat_cycle,
                        completion,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding task id and user id to the userandtasklink  table in the database
                    sql = "Insert into userandtasklink  (UID, TID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.task_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.task_count += 1
            elif repeat_cycle == "WEEKLY":
                for i in range(51):
                    date += datetime.timedelta(days=7)
                    sql = "INSERT  INTO task(TName,  TDate, Priority,  Notes, TRepeat,  Completed, TRepeatID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        date.strftime(self.date_format),
                        priority,
                        notes,
                        repeat_cycle,
                        completion,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding task id and user id to the userandtasklink  table in the database
                    sql = "Insert into userandtasklink  (UID, TID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.task_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.task_count += 1
            elif repeat_cycle == "MONTHLY":
                for i in range(59):
                    date += datetime.timedelta(days=28)
                    sql = "INSERT INTO task(TName, TDate, Priority, Notes, TRepeat, Completed, TRepeatID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        date.strftime(self.date_format),
                        priority,
                        notes,
                        repeat_cycle,
                        completion,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding task id and user id to the userandtasklink  table in the database
                    sql = "Insert into userandtasklink  (UID, TID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.task_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.task_count += 1
            elif repeat_cycle == "YEARLY":
                for i in range(49):
                    date += datetime.timedelta(days=365)
                    sql = "INSERT  INTO task(TName,  TDate, Priority,  Notes, TRepeat,  Completed, TRepeatID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    val = (
                        name,
                        date.strftime(self.date_format),
                        priority,
                        notes,
                        repeat_cycle,
                        completion,
                        repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    # adding task id and user id to the userandtasklink  table in the database
                    sql = "Insert into userandtasklink  (UID, TID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.task_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.task_count += 1
            self.current_repeat_id += 1

    def __event_plan_repeater(self, event_plan_id):
        sql = "SELECT  * FROM eplan WHERE EPID = %s"
        val = (event_plan_id,)
        cursor.execute(sql, val)
        selected_event_plan = cursor.fetchall()

        event_plan_name = selected_event_plan[0][1]
        event_plan_repeat_cycle = selected_event_plan[0][2]
        event_plan_repeat_id = selected_event_plan[0][3]

        sql = "SELECT  EID FROM eventandeplanlink  WHERE EPID = %s"
        val = (event_plan_id,)
        cursor.execute(sql, val)
        list_of_event_ids = cursor.fetchall()

        if event_plan_repeat_cycle is not "NONE":
            if event_plan_repeat_cycle == "DAILY":
                for i in range(364):
                    sql = "INSERT INTO eplan(EPName,  EPRepeat,  EPRepeatID)  VALUES (%s, %s, %s)"
                    val = (
                        event_plan_name,
                        event_plan_repeat_cycle,
                        event_plan_repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    for x in list_of_event_ids:
                        for y in x:
                            sql = "SELECT  * FROM event WHERE EID = %s"
                            val = y, 64
                            cursor.execute(sql, val)
                            selected_event = cursor.fetchall()

                            name = selected_event[0][1]
                            start_time = selected_event[0][2]
                            end_time = selected_event[0][3]
                            start_date = selected_event[0][4]
                            end_date = selected_event[0][5]
                            all_day = selected_event[0][6]
                            busy = selected_event[0][7]
                            notes = selected_event[0][8]
                            repeat_cycle = selected_event[0][9]
                            repeat_id = selected_event[0][10]

                            start_date += datetime.timedelta(days=(i + 1))
                            end_date += datetime.timedelta(days=(i + 1))

                            sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat,  ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (
                                name,
                                start_time,
                                end_time,
                                start_date.strftime(self.date_format),
                                end_date.strftime(self.date_format),
                                all_day,
                                busy,
                                notes,
                                repeat_cycle,
                                repeat_id,
                            )
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                            val = (self.current_user_id, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                            val = (self.event_plan_count, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            self.event_count += 1

                    sql = "Insert into userandeplanlink  (UID, EPID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_plan_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_plan_count += 1
            elif event_plan_repeat_cycle == "WEEKLY":
                for i in range(51):
                    sql = "INSERT INTO eplan(EPName,  EPRepeat,  EPRepeatID)  VALUES (%s, %s, %s)"
                    val = (
                        event_plan_name,
                        event_plan_repeat_cycle,
                        event_plan_repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    for x in list_of_event_ids:
                        for y in x:
                            sql = "SELECT  * FROM event WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            selected_event = cursor.fetchall()

                            name = selected_event[0][1]
                            start_time = selected_event[0][2]
                            end_time = selected_event[0][3]
                            start_date = selected_event[0][4]
                            end_date = selected_event[0][5]
                            all_day = selected_event[0][6]
                            busy = selected_event[0][7]
                            notes = selected_event[0][8]
                            repeat_cycle = selected_event[0][9]
                            repeat_id = selected_event[0][10]

                            start_date += datetime.timedelta(days=((i + 1) * 7))
                            end_date += datetime.timedelta(days=((i + 1) * 7))

                            sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat,  ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (
                                name,
                                start_time,
                                end_time,
                                start_date.strftime(self.date_format),
                                end_date.strftime(self.date_format),
                                all_day,
                                busy,
                                notes,
                                repeat_cycle,
                                repeat_id,
                            )
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                            val = (self.current_user_id, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                            val = (self.event_plan_count, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            self.event_count += 1

                    sql = "Insert into userandeplanlink  (UID, EPID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_plan_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_plan_count += 1
            elif event_plan_repeat_cycle == "MONTHLY":
                for i in range(59):
                    sql = "INSERT INTO eplan(EPName,  EPRepeat,  EPRepeatID)  VALUES (%s, %s, %s)"
                    val = (
                        event_plan_name,
                        event_plan_repeat_cycle,
                        event_plan_repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    for x in list_of_event_ids:
                        for y in x:
                            sql = "SELECT  * FROM event WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            selected_event = cursor.fetchall()

                            name = selected_event[0][1]
                            start_time = selected_event[0][2]
                            end_time = selected_event[0][3]
                            start_date = selected_event[0][4]
                            end_date = selected_event[0][5]
                            all_day = selected_event[0][6]
                            busy = selected_event[0][7]
                            notes = selected_event[0][8]
                            repeat_cycle = selected_event[0][9]
                            repeat_id = selected_event[0][10]

                            start_date += datetime.timedelta(days=((i + 1) * 28))
                            end_date += datetime.timedelta(days=((i + 1) * 28))

                            sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat,  ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (
                                name,
                                start_time,
                                end_time,
                                start_date.strftime(self.date_format),
                                end_date.strftime(self.date_format),
                                all_day,
                                busy,
                                notes,
                                repeat_cycle,
                                repeat_id,
                            )
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                            val = (self.current_user_id, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                            val = (self.event_plan_count, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            self.event_count += 1

                    sql = "Insert into userandeplanlink  (UID, EPID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_plan_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_plan_count += 1
            elif event_plan_repeat_cycle == "YEARLY":
                for i in range(49):
                    sql = "INSERT INTO eplan(EPName,  EPRepeat,  EPRepeatID)  VALUES (%s, %s, %s)"
                    val = (
                        event_plan_name,
                        event_plan_repeat_cycle,
                        event_plan_repeat_id,
                    )
                    cursor.execute(sql, val)
                    db.commit()

                    for x in list_of_event_ids:
                        for y in x:
                            sql = "SELECT  * FROM event WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            selected_event = cursor.fetchall()

                            name = selected_event[0][1]
                            start_time = selected_event[0][2]
                            end_time = selected_event[0][3]
                            start_date = selected_event[0][4]
                            end_date = selected_event[0][5]
                            all_day = selected_event[0][6]
                            busy = selected_event[0][7]
                            notes = selected_event[0][8]
                            repeat_cycle = selected_event[0][9]
                            repeat_id = selected_event[0][10]

                            start_date += datetime.timedelta(days=((i + 1) * 365))
                            end_date += datetime.timedelta(days=((i + 1) * 365))

                            sql = "INSERT  INTO event(EName,  ESTime, EETime, ESDate, EEDate, AllDay, Busy, Notes, ERepeat,  ERepeatID)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (
                                name,
                                start_time,
                                end_time,
                                start_date.strftime(self.date_format),
                                end_date.strftime(self.date_format),
                                all_day,
                                busy,
                                notes,
                                repeat_cycle,
                                repeat_id,
                            )
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "Insert into userandeventlink  (UID, EID) VALUES (%s, %s)"
                            val = (self.current_user_id, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                            val = (self.event_plan_count, self.event_count)
                            cursor.execute(sql, val)
                            db.commit()

                            self.event_count += 1

                    sql = "Insert into userandeplanlink  (UID, EPID) VALUES (%s, %s)"
                    val = (self.current_user_id, self.event_plan_count)
                    cursor.execute(sql, val)
                    db.commit()

                    self.event_plan_count += 1
            self.current_repeat_id += 1

    def __show_events(self):
        # using SQL joins to select only the events which belong to the current active user
        sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,  event.EETime, event.AllDay, 
        event.Busy,  event.Notes
        FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
        INNER JOIN user on userandeventlink.UID  = user.UID)
        WHERE user.UID  = %s"""
        val = (self.current_user_id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()

        if not result:
            print("There are no events to be displaye d.")
            return [False, result]
        else:
            # printing  all the events from the query result
            print("List of events: ")
            formatter = prettytable.PrettyTable()
            formatter.field_names = [
                "ID",
                "Name",
                "Start Date",
                "End Date",
                "Start Time",
                "End Time",
                "All Day",
                "Busy",
                "Notes",
            ]
            formatter.align["Name"] = "l"
            formatter.align["Notes"] = "l"
            for i in range(len(result)):
                formatter.add_row(
                    [
                        result[i][0],
                        result[i][1],
                        result[i][2],
                        result[i][3],
                        result[i][4],
                        result[i][5],
                        ("Yes" if result[i][6] == 1 else "No"),
                        ("Yes" if result[i][7] == 1 else "No"),
                        result[i][8],
                    ]
                )
            print(formatter)
            formatter.clear()

            sorter = True
            while sorter:
                print("Would you like to sort the events? (Yes/No)")
                sort = input().upper()
                if sort == "YES":
                    print("What would you like to sort the event by: ")
                    print("1) ID")
                    print("2) Name")
                    print("3) Start Date")
                    print("4) End Date")
                    print("5) Start Time")
                    print("6) End Time")
                    valid = False
                    while not valid:
                        try:
                            choice = int(input("Enter your choice: "))
                        except ValueError:
                            choice = 0
                        if choice == 1:
                            sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,
                            event.EETime,  event.AllDay,  event.Busy,  event.Notes
                            FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
                            INNER JOIN user on userandeventlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY event.EID  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of events: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Start Date",
                                "End Date",
                                "Start Time",
                                "End Time",
                                "All Day",
                                "Busy",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        result[i][3],
                                        result[i][4],
                                        result[i][5],
                                        ("Yes" if result[i][6] == 1 else "No"),
                                        ("Yes" if result[i][7] == 1 else "No"),
                                        result[i][8],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 2:
                            sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,
                            event.EETime,  event.AllDay,  event.Busy,  event.Notes
                            FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
                            INNER JOIN user on userandeventlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY event.EName  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of events: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Start Date",
                                "End Date",
                                "Start Time",
                                "End Time",
                                "All Day",
                                "Busy",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        result[i][3],
                                        result[i][4],
                                        result[i][5],
                                        ("Yes" if result[i][6] == 1 else "No"),
                                        ("Yes" if result[i][7] == 1 else "No"),
                                        result[i][8],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 3:
                            sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,
                            event.EETime,  event.AllDay,  event.Busy,  event.Notes
                            FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
                            INNER JOIN user on userandeventlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY event.ESDate  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of events: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Start Date",
                                "End Date",
                                "Start Time",
                                "End Time",
                                "All Day",
                                "Busy",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        result[i][3],
                                        result[i][4],
                                        result[i][5],
                                        ("Yes" if result[i][6] == 1 else "No"),
                                        ("Yes" if result[i][7] == 1 else "No"),
                                        result[i][8],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 4:
                            sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,
                            event.EETime,  event.AllDay,  event.Busy,  event.Notes
                            FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
                            INNER JOIN user on userandeventlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY event.EEDate  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of events: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Start Date",
                                "End Date",
                                "Start Time",
                                "End Time",
                                "All Day",
                                "Busy",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        result[i][3],
                                        result[i][4],
                                        result[i][5],
                                        ("Yes" if result[i][6] == 1 else "No"),
                                        ("Yes" if result[i][7] == 1 else "No"),
                                        result[i][8],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 5:
                            sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,
                            event.EETime,  event.AllDay,  event.Busy,  event.Notes
                            FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
                            INNER JOIN user on userandeventlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY event.ESTime  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of events: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Start Date",
                                "End Date",
                                "Start Time",
                                "End Time",
                                "All Day",
                                "Busy",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        result[i][3],
                                        result[i][4],
                                        result[i][5],
                                        ("Yes" if result[i][6] == 1 else "No"),
                                        ("Yes" if result[i][7] == 1 else "No"),
                                        result[i][8],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 6:
                            sql = """SELECT  event.EID,  event.EName,  event.ESDate,  event.EEDate,  event.ESTime,
                            event.EETime,  event.AllDay,  event.Busy,  event.Notes
                            FROM ((event INNER JOIN userandeventlink  on userandeventlink.EID  = event.EID)
                            INNER JOIN user on userandeventlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY event.EETime  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of events: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Start Date",
                                "End Date",
                                "Start Time",
                                "End Time",
                                "All Day",
                                "Busy",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        result[i][3],
                                        result[i][4],
                                        result[i][5],
                                        ("Yes" if result[i][6] == 1 else "No"),
                                        ("Yes" if result[i][7] == 1 else "No"),
                                        result[i][8],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        else:
                            print("Invalid  Choice. Try Again.")
                            valid = False
                elif sort == "NO":
                    sorter = False
                else:
                    print("Invalid  Input. Try Again.")
                    sorter = True
            return [True, result]

    def __show_tasks(self):
        # using SQL joins to select only the tasks which belong to the current active user
        sql = """SELECT  task.TID,  task.TName,  task.TDate,  task.Priority,  task.Completed,  task.Notes
        FROM ((task INNER JOIN userandta sklink on userandtasklink.TID  = task.TID)
        INNER JOIN user on userandtasklink.UID  = user.UID)
        WHERE user.UID  = %s"""
        val = (self.current_user_id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()

        if not result:
            print("There are no tasks to be displayed.")
            return [False, result]
        else:
            # printing  all the tasks from the query result
            print("List of tasks: ")
            formatter = prettytable.PrettyTable()
            formatter.field_names = [
                "ID",
                "Name",
                "Date",
                "Priority",
                "Completed",
                "Notes",
            ]
            formatter.align["Name"] = "l"
            formatter.align["Notes"] = "l"
            for i in range(len(result)):
                formatter.add_row(
                    [
                        result[i][0],
                        result[i][1],
                        result[i][2],
                        (
                            "None"
                            if result[i][3] == 0
                            else (
                                "Low"
                                if result[i][3] == 1
                                else ("Med" if result[i][3] == 2 else "High")
                            )
                        ),
                        ("Yes" if result[i][4] == 1 else "No"),
                        result[i][5],
                    ]
                )
            print(formatter)
            formatter.clear()

            sorter = True
            while sorter:
                print("Would you like to sort the tasks? (Yes/No)")
                sort = input().upper()
                if sort == "YES":
                    print("What would you like to sort the tasks by: ")
                    print("1) ID")
                    print("2) Name")
                    print("3) Date")
                    print("4) Priority")
                    print("5) Completion")
                    valid = False
                    while not valid:
                        try:
                            choice = int(input("Enter your choice: "))
                        except ValueError:
                            choice = 0
                        if choice == 1:
                            sql = """SELECT  task.TID,  task.TName,  task.TDate,  task.Priority,  task.Completed,  task.Notes
                            FROM ((task INNER JOIN userandtasklink  on userandtasklink.TID  = task.TID)
                            INNER JOIN user on userandtasklink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY task.TID  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of tasks: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Date",
                                "Priority",
                                "Completion",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        (
                                            "None"
                                            if result[i][3] == 0
                                            else (
                                                "Low"
                                                if result[i][3] == 1
                                                else (
                                                    "Med"
                                                    if result[i][3] == 2
                                                    else "High"
                                                )
                                            )
                                        ),
                                        ("Yes" if result[i][4] == 1 else "No"),
                                        result[i][5],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 2:
                            sql = """SELECT  task.TID,  task.TName,  task.TDate,  task.Priority,  task.Completed,  task.Notes
                            FROM ((task INNER JOIN userandtasklink  on userandtasklink.TID  = task.TID)
                            INNER JOIN user on userandtasklink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY task.TName  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()
                            print("List of tasks: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Date",
                                "Priority",
                                "Completion",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        (
                                            "None"
                                            if result[i][3] == 0
                                            else (
                                                "Low"
                                                if result[i][3] == 1
                                                else (
                                                    "Med"
                                                    if result[i][3] == 2
                                                    else "High"
                                                )
                                            )
                                        ),
                                        ("Yes" if result[i][4] == 1 else "No"),
                                        result[i][5],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 3:
                            sql = """SELECT  task.TID,  task.TName,  task.TDate, task.Priority,  task.Completed,  task.Notes
                            FROM ((task INNER JOIN userandtasklink  on userandtasklink.TID  = task.TID)
                            INNER JOIN user on userandtasklink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY task.TDate  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()
                            print("List of tasks: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Date",
                                "Priority",
                                "Completion",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        (
                                            "None"
                                            if result[i][3] == 0
                                            else (
                                                "Low"
                                                if result[i][3] == 1
                                                else (
                                                    "Med"
                                                    if result[i][3] == 2
                                                    else "High"
                                                )
                                            )
                                        ),
                                        ("Yes" if result[i][4] == 1 else "No"),
                                        result[i][5],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        elif choice == 4:
                            sql = """SELECT  task.TID,  task.TName,  task.TDate,  task.Priority,  task.Completed,  task.Note s
                            FROM ((task INNER JOIN userandtasklink  on userandtasklink.TID  = task.TID)
                            INNER JOIN user on userandtasklink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY task.Priority  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()
                            print("List of tasks: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Date",
                                "Priority",
                                "Completion",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        (
                                            "None"
                                            if result[i][3] == 0
                                            else (
                                                "Low"
                                                if result[i][3] == 1
                                                else (
                                                    "Med"
                                                    if result[i][3] == 2
                                                    else "High"
                                                )
                                            )
                                        ),
                                        ("Yes" if result[i][4] == 1 else "No"),
                                        result[i][5],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()
                            valid = True
                        elif choice == 5:
                            sql = """SELEC T task.TID,  task.TName,  task.TDate,  task.Priority,  task.Completed,  task.Notes
                            FROM ((task INNER JOIN userandtasklink  on userandtasklink.TID  = task.TID)
                            INNER JOIN user on userandtasklink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY task.Completed  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of tasks: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = [
                                "ID",
                                "Name",
                                "Date",
                                "Priority",
                                "Completion",
                                "Notes",
                            ]
                            formatter.align["Name"] = "l"
                            formatter.align["Notes"] = "l"
                            for i in range(len(result)):
                                formatter.add_row(
                                    [
                                        result[i][0],
                                        result[i][1],
                                        result[i][2],
                                        (
                                            "None"
                                            if result[i][3] == 0
                                            else (
                                                "Low"
                                                if result[i][3] == 1
                                                else (
                                                    "Med"
                                                    if result[i][3] == 2
                                                    else "High"
                                                )
                                            )
                                        ),
                                        ("Yes" if result[i][4] == 1 else "No"),
                                        result[i][5],
                                    ]
                                )
                            print(formatter)
                            formatter.clear()

                            valid = True
                        else:
                            print("Invalid  Choice. Try Again.")
                            valid = False
                elif sort == "NO":
                    sorter = False
                else:
                    print("Invalid  Input. Try Again.")
                    sorter = True
            return [True, result]

    def __show_event_plans(self):
        # using SQL joins to select only the event plans which belong to the current active user
        sql = """SELECT  eplan.EPID,  eplan.EPName
        FROM ((eplan INNER JOIN userandeplanlink  on userandeplanlink.EPID  = eplan.EPID)
        INNER JOIN user on userandeplanlink.UID  = user.UID)
        WHERE user.UID  = %s"""
        val = (self.current_user_id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()

        if not result:
            print("There are no event plans to be displayed.")
            return [False, result]
        else:
            # # printing  all the event plan from the query result
            print("List of Event Plans: ")
            formatter = prettytable.PrettyTable()
            formatter.field_names = ["ID", "Name", "Events"]
            formatter.align["Name"] = "l"
            formatter.align["Events"] = "l"
            for i in range(len(result)):
                # query to select names of the events that are a part of the relevant  event plan
                sql = """SELECT  event.EName
                FROM ((event INNER JOIN eventandeplanlink  on eventandeplanlink.EID  = event.EID)
                INNER JOIN eplan on eventandeplanlink.EPID  = eplan.EPID)
                WHERE eventandeplanlink.EPID  = %s"""
                val = (result[i][0],)
                cursor.execute(sql, val)
                result2 = cursor.fetchall()
                list_of_events = ""
                for k in range(len(result2)):
                    for l in range(len(result2[k])):
                        if k == (len(result2) - 1) or len(result2) == 1:
                            list_of_events += result2[k][l]
                        else:
                            list_of_events += result2[k][l] + ", "
                formatter.add_row([result[i][0], result[i][1], list_of_events])
            print(formatter)
            formatter.clear()

            sorter = True
            while sorter:
                print("Would you like to sort the event plans by name? (Yes/No)")
                sort = input().upper()
                if sort == "YES":
                    print("What would you like to sort the event plans by: ")
                    print("1) ID")
                    print("2) Name")
                    valid = False
                    while not valid:
                        try:
                            choice = int(input("Enter your choice: "))
                        except ValueError:
                            choice = 0
                        if choice == 1:
                            sql = """SELECT  eplan.EPID,  eplan.EPName
                            FROM ((eplan INNER JOIN userandeplanlink  on userandeplanlink.EPID  = eplan.EPID)
                            INNER JOIN user on userandeplanlink.UID  = user.UID)
                            WHERE user.UID  = %s ORDER BY eplan.EPName  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of Event Plans: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = ["ID", "Name", "Events"]
                            formatter.align["Name"] = "l"
                            formatter.align["Events"] = "l"
                            for i in range(len(result)):
                                # query to select names of events that are a part of the event plan
                                sql = """SELECT  event.EName
                                FROM ((event INNER JOIN eventandeplanlink  on eventandeplanlink.EID = event.EID)
                                INNER JOIN eplan on eventandeplanlink.EPID  = eplan.EPID)
                                WHERE eventandeplanli nk.EPID = %s"""
                                val = (result[i][0],)
                                cursor.execute(sql, val)
                                result2 = cursor.fetchall()

                                list_of_events = ""
                                for k in range(len(result2)):
                                    for l in range(len(result2[k])):
                                        if k == (len(result2) - 1) or len(result2) == 1:
                                            list_of_events += result2[k][l]
                                        else:
                                            list_of_events += result2[k][l] + ", "
                                formatter.add_row(
                                    [result[i][0], result[i][1], list_of_events]
                                )
                            print(formatter)
                            formatter.clear()
                            valid = True
                        elif choice == 2:
                            sql = """SELECT  eplan.EPID,  eplan.EPName
                            FROM ((eplan INNER JOIN userandeplanlink  on userandeplanlink.EPID  = eplan.EPID)
                            INNER JOIN user on userandeplanlink.UID  = user.UID)   75
                            WHERE user.UID  = %s ORDER BY eplan.EPID  ASC"""
                            val = (self.current_user_id,)
                            cursor.execute(sql, val)
                            result = cursor.fetchall()

                            print("List of Event Plans: ")
                            formatter = prettytable.PrettyTable()
                            formatter.field_names = ["ID", "Name", "Events"]
                            formatter.align["Name"] = "l"
                            formatter.align["Events"] = "l"
                            for i in range(len(result)):
                                # query to select names of events that are a part of the event plan
                                sql = """SELECT  event.EName
                                FROM ((event INNER JOIN eventandeplanlink  on eventandeplanlink.EID = event.EID)
                                INNER JOIN eplan on eventandeplanlink.EPID  = eplan.EPID)
                                WHERE eventandeplanli nk.EPID = %s"""
                                val = (result[i][0],)
                                cursor.execute(sql, val)
                                result2 = cursor.fetchall()

                                list_of_events = ""
                                for k in range(len(result2)):
                                    for l in range(len(result2[k])):
                                        if k == (len(result2) - 1) or len(result2) == 1:
                                            list_of_events += result2[k][l]
                                        else:
                                            list_of_events += result2[k][l] + ", "
                                formatter.add_row(
                                    [result[i][0], result[i][1], list_of_events]
                                )
                            print(formatter)
                            formatter.clear()
                            valid = True
                        else:
                            print("Invalid  Choice. Try Again.")
                            valid = False

                elif sort == "NO":
                    sorter = False
                else:
                    print("Invalid  Input. Try Again.")
                    sorter = True
            return [True, result]

    def __complete_task(self):
        # query to fetch all the task ids for the selected  user
        sql = """SELECT  task.TID
        FROM ((task INNER JOIN userandtasklink  on userandtasklink.TID  = task.TID)
        INNER JOIN user on userandtasklink.UID  = user.UID)
        WHERE user.UID = %s"""
        val = (self.current_user_id,)
        cursor.execute(sql, val)
        result = cursor.fetchall()

        if not result:  # condition  for no existing  tasks
            print("You haven't created any tasks.")
        else:
            exists = []
            exit_loop = False
            while not exit_loop:
                exit_loop = True
                print("Options:  ")
                print("1) Search for a Task")
                print("2) Show All Tasks")
                choice = 0
                valid = False
                while not valid:
                    try:
                        choice = int(input("Enter your choice: "))
                        valid = True
                    except ValueError:
                        print("Invalid  Input. Try Again.")
                        valid = False
                if choice == 1:
                    exists = self.__search_task()
                elif choice == 2:
                    exists = self.__show_tasks()
                else:
                    print("Invalid  Input. Try Again.")
                    exit_loop = False
            if exists[0]:
                desired_task_id = 0
                valid_id = False
                while not valid_id:
                    valid = False
                    while not valid:
                        try:
                            desired_task_id = int(
                                input(
                                    "Enter the ID of the Task who's completion  you would like to change: "
                                )
                            )
                            valid = True
                        except ValueError:
                            print("Invalid  Input. Try Again.")
                            valid = False
                    for (
                        x
                    ) in (
                        result
                    ):  # loop to check if inputted  id is part of existing  ids
                        if desired_task_id in x:
                            valid_id = True

                    if valid_id:
                        sql = "SELECT Completed  FROM task WHERE TID = %s"
                        val = (desired_task_id,)
                        cursor.execute(sql, val)
                        current_completion = cursor.fetchall()

                        if current_completion[0][0] == 1:
                            new_completion = 0
                        else:
                            new_completion = 1

                        # query to update task with new completion
                        sql = "UPDATE task SET Completed  = %s WHERE TID = %s"
                        val = (new_completion, desired_task_id)
                        cursor.execute(sql, val)
                        db.commit()
                    else:
                        print("Invalid  Task ID. Try Again.")

    def __search_event(self):  # function  to search for an event
        exit_loop = False
        while not exit_loop:
            print("Search Options:  ")
            print("1) By Name")
            print("2) By Date")
            valid = False
            choice = 0
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice < 1 or choice > 2:
                print("Invalid  Input. Try Again.")
                exit_loop = False
            else:
                exit_loop = True
        if choice == 1:  # searching  for event by name
            event_name = input("Enter the name of the event that you are looking for: ")
            while not self.__error_checker("Blank", event_name):
                event_name = input("You entered a blank. Try again: ")

            # query to select the event ids of the events with the searched  name
            sql = """SELECT  event.EID
            FROM (event INNER JOIN userandeventlink  on event.EID  = userandeventlink.EID)
            WHERE userandeventlink.UID  = %s AND event.EName  = %s"""
            val = (
                self.current_user_id,
                event_name,
            )
            cursor.execute(sql, val)
        elif choice == 2:  # searching  by date
            event_date = input(
                "Enter the date of the event(s)  that you are looking for (format:  YYYY-MM-DD): "
            )
            # checking  the format of the date
            while not self.__error_checker("Date", event_date):
                print("Invalid  Format. Try Again.")
                event_date = input(
                    "Enter the date of the event(s)  that you are looking for (format:  YYYY-MM-DD): "
                )

            # query to select the event ids of the events with the searched  date
            sql = """SELECT  event.EID
            FROM (event INNER JOIN userandeventlink  on event.EID  = userandeventlink.EID)
            WHERE userandeventlink.UID  = %s AND event.ES Date = %s"""
            val = (
                self.current_user_id,
                event_date,
            )
            cursor.execute(sql, val)
        else:
            print("Invalid  Option.")

        if choice == 1 or choice == 2:
            event_ids = (
                cursor.fetchall()
            )  # fetching  the searched  values from the database

            if len(event_ids) >= 1:
                print("List of events: ")
                formatter = prettytable.PrettyTable()
                formatter.field_names = [
                    "ID",
                    "Name",
                    "Start Date",
                    "End Date",
                    "Start Time",
                    "End Time",
                    "All Day",
                    "Busy",
                    "Notes",
                ]
                formatter.align["Name"] = "l"
                formatter.align["Notes"] = "l"

                for x in event_ids:
                    for y in x:
                        sql = "SELECT EID, EName, ESDate, EEDate, ESTime, EETime, AllDay, Busy, Notes FROM event WHERE EID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        result = cursor.fetchall()
                        for i in range(len(result)):
                            formatter.add_row(
                                [
                                    result[i][0],
                                    result[i][1],
                                    result[i][2],
                                    result[i][3],
                                    result[i][4],
                                    result[i][5],
                                    ("Yes" if result[i][6] == 1 else "No"),
                                    ("Yes" if result[i][7] == 1 else "No"),
                                    result[i][8],
                                ]
                            )
                print(formatter)
                formatter.clear()
                return [True, event_ids]
            else:
                print("No events found.")
                return [False, event_ids]

    def __search_task(self):  # function  to search for a a task
        exit_loop = False
        while not exit_loop:
            print("Search Options:  ")
            print("1) By Name")
            print("2) By Date")
            valid = False
            choice = 0
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice < 1 or choice > 2:
                print("Invalid  Input. Try Again.")
                exit_loop = False
            else:
                exit_loop = True

        if choice == 1:  # searching  for task by name
            task_name = input("Enter the name of the task that you are looking for: ")
            while task_name.strip() == "":
                task_name = input("You entered a blank. Try again: ")

            sql = """SELECT  task.TID
            FROM (task INNER JOIN userandtasklink  on task.TID  = userandtasklink.TID)
            WHERE userandtasklink.UID  = %s AND task.TName  = %s"""
            val = (
                self.current_user_id,
                task_name,
            )
            cursor.execute(sql, val)
        elif choice == 2:  # searching  for task by date
            task_date = input(
                "Enter the date of the task(s) that you are looking for (format:  YYYY-MM-DD): "
            )
            # checking  the format of the date
            while not self.__error_checker("Date", task_date):
                print("Invalid  Format. Try Again.")
                task_date = input(
                    "Enter the date of the task(s) that you are looking for (format:  YYYY-MM-DD): "
                )

            sql = """SELECT  task.TID FROM (task INNER JOIN userandtasklink  on task.TID  = userandtasklink.TID)
            WHERE userandtasklink.UID  = %s AND task.TDate  = %s"""
            val = (
                self.current_user_id,
                task_date,
            )
            cursor.execute(sql, val)
        else:
            print("Invalid  Option.")

        if choice == 1 or choice == 2:
            task_ids = (
                cursor.fetchall()
            )  # fetching  the results of the query from the database

            if len(task_ids) >= 1:
                print("List of tasks: ")
                formatter = prettytable.PrettyTable()
                formatter.field_names = [
                    "ID",
                    "Name",
                    "Date",
                    "Priority",
                    "Completed",
                    "Notes",
                ]
                formatter.align["Name"] = "l"
                formatter.align["Notes"] = "l"

                for x in task_ids:
                    sql = "SELECT TID, TName, TDate, Priority,  Completed,  Notes FROM task WHERE TID = %s"
                    val = x
                    cursor.execute(sql, val)
                    result = cursor.fetchall()
                    for i in range(len(result)):
                        formatter.add_row(
                            [
                                result[i][0],
                                result[i][1],
                                result[i][2],
                                (
                                    "None"
                                    if result[i][3] == 0
                                    else (
                                        "Low"
                                        if result[i][3] == 1
                                        else ("Med" if result[i][3] == 2 else "High")
                                    )
                                ),
                                ("Yes" if result[i][4] == 1 else "No"),
                                result[i][5],
                            ]
                        )
                print(formatter)
                formatter.clear()
                return [True, task_ids]
            else:
                print("No tasks found.")
                return [False, task_ids]

    def __search_event_plan(self):  # function  to search for event plans
        event_plan_name = input(
            "Enter the name of the event plan that you are looking for: "
        )
        while not self.__error_checker("Blank", event_plan_name):
            event_plan_name = input("You entered a blank. Try again: ")

        sql = """SELECT  eplan.EPID
        FROM (eplan INNER JOIN userandeplanlink  on eplan.EPID  = userandeplanlink.EPID)
        WHERE userandeplanlink.UID  = %s AND eplan.EPName  = %s"""
        val = (
            self.current_user_id,
            event_plan_name,
        )
        cursor.execute(sql, val)
        event_plan_ids = cursor.fetchall()

        if len(event_plan_ids) >= 1:
            print("List of Event Plans: ")
            formatter = prettytable.PrettyTable()
            formatter.field_names = ["ID", "Name", "Events"]
            formatter.align["Name"] = "l"
            formatter.align["Events"] = "l"
            for x in event_plan_ids:
                for y in x:
                    sql = "SELECT EPID, EPName, EPRepeat  FROM eplan WHERE EPID = %s"
                    val = (y,)
                    cursor.execute(sql, val)
                    result = cursor.fetchall()

                    for i in range(len(result)):
                        sql = """SELECT  event.EName
                        FROM ((event INNER JOIN eventandeplanlink  on eventandeplanlink.EID  = event.EID)
                        INNER JOIN eplan on eventandeplanlink.EPID  = eplan.EPID)
                        WHERE eventandeplanlink.EPID  = %s"""
                        val = (result[i][0],)
                        cursor.execute(sql, val)
                        result2 = cursor.fetchall()

                        list_of_events = ""
                        for k in range(len(result2)):
                            for l in range(len(result2[k])):
                                if k == (len(result2) - 1) or len(result2) == 1:
                                    list_of_events += result2[k][l]
                                else:
                                    list_of_events += result2[k][l] + ", "
                        formatter.add_row([result[i][0], result[i][1], list_of_events])
            print(formatter)
            formatter.clear()
            return [True, event_plan_ids]
        else:
            print("No event plans found.")
            return [False, event_plan_ids]

    def __edit_event(self):
        exists = []
        exit_loop = False
        while not exit_loop:
            exit_loop = True
            print("Options:  ")
            print("1) Search for an Event")
            print("2) Show All Events")
            choice = 0
            valid = False
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice == 1:
                exists = self.__search_event()
            elif choice == 2:
                exists = self.__show_events()
            else:
                print("Invalid  Input. Try Again.")
                exit_loop = False

        if exists[0]:
            desired_event_id = 0
            valid = False
            while not valid:
                try:
                    desired_event_id = int(
                        input("Enter the ID of the event you would like to edit: ")
                    )
                    for i in range(len(exists[1])):
                        if (desired_event_id) == exists[1][i][0]:
                            valid = True
                            break
                        else:
                            valid = False
                    if valid == False:
                        print("Invalid  ID. Try Again.")
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False

            try:
                sql = "SELECT AllDay FROM event WHERE EID = %s"
                val = (desired_event_id,)
                cursor.execute(sql, val)
                all_day = int(cursor.fetchall()[0][0])
            except IndexError:
                all_day = -1

            exit_loop = False
            while not exit_loop:
                print("Option:  ")
                print("1) Name")
                print("2) All Day")
                print("3) Busy")
                print("4) Notes")
                print("5) Repeat")
                if (
                    all_day == 0
                ):  # changes menu output based on whether all day is true or false
                    print("6) Start Date")
                    print("7) End Date")
                    print("8) Start Time")
                    print("9) End Time")
                    print("10) Exit")
                else:
                    print("6) Date")
                    print("7) Exit")
                choice = 0
                valid = False
                while not valid:
                    try:
                        choice = int(input("Enter your choice: "))
                        valid = True
                    except ValueError:
                        print("Invalid  Input. Try Again.")
                        valid = False

                if (
                    all_day == 1
                ):  # conditional  statements  to ensure correct output based on the input
                    if choice == 6:
                        choice = 10
                    elif choice == 7:
                        choice = 11
                elif all_day == 0 and choice == 10:
                    choice = 11

                if choice == 1:  # changing  name
                    name = input("Please a new name for the event: ")
                    while not self.__error_checker("Blank", name):
                        name = input("You entered a blank. Try again: ")

                    self.event_obj.set_name(desired_event_id, name)
                elif choice == 2:  # changing  all day property
                    all_day = (input("Is the event an All Day event (Y/N): ")).upper()
                    while self.__error_checker("Bool", all_day) == "Invalid":
                        print("Invalid  Input. Try Again")
                        all_day = (input("Is the event an All Day event (Y/N)")).upper()

                    all_day = self.__error_checker("Bool", all_day)
                    self.event_obj.set_all_day(desired_event_id, int(all_day))
                elif choice == 3:  # changing  busy property
                    busy = (input("Will you be busy during the event (Y/N): ")).upper()
                    while self.__error_checker("Bool", busy) == "Invalid":
                        print("Invalid  Input. Try Again")
                        busy = (
                            input("Will you be busy during the event (Y/N)")
                        ).upper()

                    busy = self.__error_checker("Bool", busy) == "Invalid"
                    self.event_obj.set_busy(desired_event_id, int(busy))
                elif choice == 4:  # changing  notes regarding  the event
                    print("Add notes (1000 character  limit): ")
                    notes = input("")
                    while not self.__error_checker("Notes", notes):
                        print("Character  limit exceeded.  Try Again: ")
                        notes = input("")

                    self.event_obj.set_notes(desired_event_id, notes)
                elif choice == 5:  # changing  repeat cycle for the event
                    event_repeat = input(
                        "Enter a new repeat cycle (None, Daily, Weekly, Monthly,  Yearly):  "
                    ).upper()
                    while not self.__error_checker("Repeat", event_repeat):
                        print("Invalid  Input. Try Again.")
                        event_repeat = input(
                            "Enter a repeat cycle again (None, Daily, Weekly, Monthly,  Yearly):  "
                        ).upper()

                    self.event_obj.set_repeat(desired_event_id, event_repeat)
                # following  elif statements  only be executed  if the all day condition  is set to false
                elif choice == 6:  # changing  start date
                    new_start_date = input(
                        "Enter a new Start Date for the event (YYYY-MM-DD): "
                    )
                    while not self.__error_checker("Date", new_start_date):
                        print("Invalid  Format. Try Again.")
                        new_start_date = input(
                            "Enter the start date again (YYYY-MM-DD): "
                        )

                    self.event_obj.set_start_date(desired_event_id, new_start_date)
                elif choice == 7:  # changing  end date
                    new_end_date = input(
                        "Enter a new End Date for the event (YYYY-MM-DD): "
                    )
                    while not self.__error_checker("Date", new_end_date):
                        print("Invalid  Format. Try Again.")
                        new_end_date = input("Enter the end date again (YYYY-MM-DD): ")

                    self.event_obj.set_end_date(desired_event_id, new_end_date)
                elif choice == 8:  # changing  the start time
                    new_start_time = input(
                        "Enter a new Start Time for the event (HH:MM:SS):  "
                    )
                    while not self.__error_checker("Time", new_start_time):
                        print("Invalid  Format. Try Again.")
                        new_start_time = input(
                            "Enter the start time for the event (HH:mm:ss):  "
                        )

                    self.event_obj.set_start_time(desired_event_id, new_start_time)
                elif choice == 9:  # changing  the end time
                    new_end_time = input(
                        "Enter a new End Time for the event (HH:MM:SS):  "
                    )
                    while not self.__error_checker("Time", new_end_time):
                        print("Invalid Format. Try Again.")
                        new_end_time = input(
                            "Enter the end time for the event (HH:mm:ss):  "
                        )

                    self.event_obj.set_end_time(desired_event_id, new_end_time)
                elif choice == 10:
                    # changing  the date for event (provided  that the all day condition  is set to true)
                    date = input("Enter a new date for the event (YYYY-DD-MM): ")
                    while not self.__error_checker("Date", date):
                        print("Invalid  Format. Try Again.")
                        date = input("Enter the date again (YYYY-MM-DD): ")

                    self.event_obj.set_start_date(desired_event_id, date)
                    self.event_obj.set_end_date(desired_event_id, date)
                elif choice == 11:
                    exit_loop = True
                else:
                    print("Invalid  Input. Try Again.")
                    exit_loop = False

    def __edit_task(self):
        exists = []
        exit_loop = False
        while not exit_loop:
            exit_loop = True
            print("Options:  ")
            print("1) Search for a Task")
            print("2) Show All Tasks")
            choice = 0
            valid = False
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice == 1:
                exists = self.__search_task()
            elif choice == 2:
                exists = self.__show_tasks()
            else:
                print("Invalid  Input. Try Again.")
                exit_loop = False

        if exists[0]:
            desired_task_id = 0
            valid = False
            while not valid:
                try:
                    desired_task_id = int(
                        input("Enter the ID of the task you would like to edit: ")
                    )
                    for i in range(len(exists[1])):
                        if (desired_task_id) == exists[1][i][0]:
                            valid = True
                            break
                        else:
                            valid = False
                    if valid == False:
                        print("Invalid  ID. Try Again.")
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False

            exit_loop = False
            while not exit_loop:
                print("Option: ")
                print("1) Name")
                print("2) Date")
                print("3) Priority  Level")
                print("4) Notes")
                print("5) Repeat")
                print("6) Completion")
                print("7) Exit")
                choice = 0
                valid = False
                while not valid:
                    try:
                        choice = int(input("Enter your choice: "))
                        valid = True
                    except ValueError:
                        print("Invalid  Input. Try Again.")
                        valid = False

                if choice == 1:
                    name = input("Please enter a new name for the task: ")
                    while not self.__error_checker("Blank", name):
                        name = input("You entered a blank. Try again: ")

                    self.task_obj.set_name(desired_task_id, name)
                elif choice == 2:
                    date = input("Enter a new date for the event (YYYY-DD-MM): ")
                    while not self.__error_checker("Date", date):
                        print("Invalid  Format. Try Again.")
                        date = input("Enter the date again (YYYY-MM-DD): ")

                    self.task_obj.set_date(desired_task_id, date)
                elif choice == 3:
                    priority = input(
                        "Enter a new priority  of the task (0-lowest, 1, 2, 3-highest):  "
                    )
                    valid = False
                    while not valid:
                        if priority in ["0", "1", "2", "3"]:
                            valid = True
                        else:
                            valid = False
                            print("Invalid  Input. Try Again.")
                            priority = input(
                                "Enter the priority  of the task again (0-lowest, 1, 2, 3-highest):  "
                            )

                    self.task_obj.set_priority(desired_task_id, int(priority))
                elif choice == 4:
                    print("Add notes (1000 character  limit): ")
                    notes = input("")
                    while not self.__error_checker("Notes", notes):
                        print("Character  limit exceeded.  Try Again: ")
                        notes = input("")

                    self.task_obj.set_notes(desired_task_id, notes)
                elif choice == 5:
                    task_repeat = input(
                        "Enter a new repeat cycle (None, Daily, Weekly, Monthly,  Yearly):  "
                    ).upper()
                    while not self.__error_checker("Repeat", task_repeat):
                        print("Invalid  Input. Try Again.")
                        task_repeat = input(
                            "Enter repeat cycle again (None, Daily, Weekly, Monthly,  Yearly):  "
                        ).upper()

                    self.task_obj.set_repeat(desired_task_id, task_repeat)
                elif choice == 6:
                    new_completion = (
                        input("Have you completed  this task (Y/N): ")
                    ).upper()
                    while self.__error_checker("Bool", new_completion) == "Invalid":
                        print("Invalid  Input. Try Again")
                        new_completion = (
                            input("Have you completed  this task (Y/N): ")
                        ).upper()

                    new_completion = self.__error_checker("Bool", new_completion)

                    sql = "UPDATE task SET Completed  = %s WHERE TID = %s"
                    val = (int(new_completion), desired_task_id)
                    cursor.execute(sql, val)
                    db.commit()
                elif choice == 7:
                    exit_loop = True
                else:
                    print("Invalid  Input. Try Again.")
                    exit_loop = False

    def __edit_event_plan(self):
        exists = []
        exit_loop = False
        while not exit_loop:
            exit_loop = True
            print("Options:  ")
            print("1) Search for an Event Plan")
            print("2) Show All Event Plans")
            choice = 0
            valid = False
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice == 1:
                exists = self.__search_event_plan()
            elif choice == 2:
                exists = self.__show_event_plans()
            else:
                print("Invalid  Input. Try Again.")
                exit_loop = False

        if exists[0]:
            desired_event_plan_id = 0
            valid = False
            while not valid:
                try:
                    desired_event_plan_id = int(
                        input("Enter the ID of the event plan you would like to edit: ")
                    )
                    for i in range(len(exists[1])):
                        if (desired_event_plan_id) == exists[1][i][0]:
                            valid = True
                            break
                        else:
                            valid = False
                    if valid == False:
                        print("Invalid  ID. Try Again.")
                except ValueError:
                    print("Invalid Input. Try Again.")
                    valid = False

            exit_loop = False
            while not exit_loop:
                print("Option:  ")
                print("1) Name")
                print("2) Repeat")
                print("3) Events")
                print("4) Exit")
                choice = 0
                valid = False
                while not valid:
                    try:
                        choice = int(input("Enter your choice: "))
                        valid = True
                    except ValueError:
                        print("Invalid  Input. Try Again.")
                        valid = False

                if choice == 1:
                    name = input("Please enter the name of the event: ")
                    while not self.__error_checker("Blank", name):
                        name = input("You entered a blank. Try again: ")

                    self.event_plan_object.set_name(desired_event_plan_id, name)
                elif choice == 2:
                    event_plan_repeat = input(
                        "Enter a new repeat cycle (None, Daily, Weekly, Monthly,  Yearly):  "
                    ).upper()
                    while not self.__error_checker("Repeat", event_plan_repeat):
                        print("Invalid  Input. Try Again.")
                        event_plan_repeat = input(
                            "Enter repeat cycle again (None, Daily, Weekly, Monthly,  Yearly):  "
                        ).upper()

                    self.event_plan_object.set_repeat(
                        desired_event_plan_id, event_plan_repeat
                    )
                elif choice == 3:
                    print("Options:  ")
                    print("1) Remove an Event from the Plan")
                    print("2) Add an Event to the Plan")
                    choice_1 = int(input("Enter your choice: "))

                    if choice_1 == 1:
                        sql = """SELECT  event.EID,  event.EName
                        FROM ((event INNER JOIN eventandeplanlink  on event.EID  = eventandeplanlink.EID)
                        INNER JOIN eplan on eplan.EPID  = eventandeplanlink.EPID)
                        WHERE eventandeplanlink.EPID  = %s"""
                        val = (desired_event_plan_id,)
                        cursor.execute(sql, val)
                        result = cursor.fetchall()

                        print("List of Events in the selected  Plan: ")
                        formatter = prettytable.PrettyTable()
                        formatter.field_names = ["ID", "Name"]
                        formatter.align["Name"] = "l"
                        for i in range(len(result)):
                            formatter.add_row([result[i][0], result[i][1]])
                        print(formatter)
                        formatter.clear()
                        print()

                        remove_event = int(
                            input(
                                "Enter the ID of the event you would like to remove: "
                            )
                        )

                        sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                        val = (remove_event,)
                        cursor.execute(sql, val)
                        db.commit()
                    elif choice_1 == 2:
                        sql = """SELECT  event.EID,  event.EName
                        FROM (event INNER JOIN userandeventlink  on event.EID  = userandeventlink.EID)
                        WHERE userandeventlink.UID  = %s AND event.EID  NOT IN (SELECT event.EID
                        FROM ((event INNER JOIN eventandeplanlink  on event.EID = eventandeplanlink.EID)
                        INNER JOIN eplan on eplan.EPID  = eventandeplanlink.EPID)
                        WHERE eventandeplanlink.EPID  = %s)"""
                        val = (
                            self.current_user_id,
                            desired_event_plan_id,
                        )
                        cursor.execute(sql, val)
                        result = cursor.fetchall()

                        print("List of Events not in the selected Plan: ")
                        formatter = prettytable.PrettyTable()
                        formatter.field_names = ["ID", "Name"]
                        formatter.align["Name"] = "l"
                        for i in range(len(result)):
                            formatter.add_row([result[i][0], result[i][1]])
                        print(formatter)
                        formatter.clear()
                        print()

                        add_event = int(
                            input("Enter the ID of the event you would like to add: ")
                        )

                        sql = (
                            "INSERT INTO eventandeplanlink  (EPID, EID) VALUES (%s, %s)"
                        )
                        val = (desired_event_plan_id, add_event)
                        cursor.execute(sql, val)
                        db.commit()
                elif choice == 4:
                    exit_loop = True
                else:
                    print("Invalid  Input. Try Again.")
                    exit_loop = False

    def __delete_event(self):
        exists = []
        exit_loop = False
        while not exit_loop:
            exit_loop = True
            print("Options:  ")
            print("1) Search for an Event")
            print("2) Show All Events")
            choice = 0
            valid = False
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice == 1:
                exists = self.__search_event()
            elif choice == 2:
                exists = self.__show_events()
            else:
                print("Invalid  Input. Try Again.")
                exit_loop = False

        if exists[0]:
            desired_event_id = 0
            valid = False
            while not valid:
                try:
                    desired_event_id = int(
                        input("Enter the ID of the event you would like to delete: ")
                    )
                    for i in range(len(exists[1])):
                        if (desired_event_id) == exists[1][i][0]:
                            valid = True
                            break
                        else:
                            valid = False
                    if valid == False:
                        print("Invalid  ID. Try Again.")
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False

            valid = False
            while not valid:
                print(
                    "Would you like to delete all repeats of this event as well? (Yes/No)"
                )
                confirmation = input().upper()
                if confirmation == "YES" or confirmation == "Y":
                    sql = "SELECT ERepeatID  FROM event WHERE EID = %s"
                    val = (desired_event_id,)
                    cursor.execute(sql, val)
                    desired_repeat_id = cursor.fetchall()

                    sql = "SELECT EID FROM event WHERE ERepeatID  = %s"
                    val = (desired_repeat_id[0][0],)
                    cursor.execute(sql, val)
                    desired_event_ids = cursor.fetchall()

                    for x in desired_event_ids:
                        for y in x:
                            sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM userandeventlink  WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM event WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                    print("Events deleted.  ")
                    valid = True
                elif confirmation == "No" or confirmation == "N":
                    sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                    val = (desired_event_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    sql = "DELETE FROM userandeventlink  WHERE EID = %s"
                    val = (desired_event_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    sql = "DELETE FROM event WHERE EID = %s"
                    val = (desired_event_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    print("Event deleted.  ")
                    valid = True
                else:
                    print("Invalid  Input. Try Again.")
                    valid = False

    def __delete_task(self):
        exists = []
        exit_loop = False
        while not exit_loop:
            exit_loop = True
            print("Options:  ")
            print("1) Search for a Task")
            print("2) Show All Tasks")
            choice = 0
            valid = False
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice == 1:
                exists = self.__search_task()
            elif choice == 2:
                exists = self.__show_tasks()
            else:
                print("Invalid  Input. Try Again.")
                exit_loop = False

        if exists[0]:
            desired_task_id = 0
            valid = False
            while not valid:
                try:
                    desired_task_id = int(
                        input("Enter the ID of the task you would like to delete: ")
                    )
                    for i in range(len(exists[1])):
                        if (desired_task_id) == exists[1][i][0]:
                            valid = True
                            break
                        else:
                            valid = False
                    if valid == False:
                        print("Invalid  ID. Try Again.")
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            valid = False
            while not valid:
                print(
                    "Would you like to delete all repeats of this task as well? (Yes/No)"
                )
                confirmation = input().upper()
                if confirmation == "YES" or confirmation == "Y":
                    sql = "SELECT TRepeatID  FROM task WHERE TID = %s"
                    val = (desired_task_id,)
                    cursor.execute(sql, val)
                    desired_repeat_id = cursor.fetchall()

                    sql = "SELECT TID FROM task WHERE TRepeatID  = %s"
                    val = (desired_repeat_id[0][0],)
                    cursor.execute(sql, val)
                    desired_task_ids = cursor.fetchall()

                    for x in desired_task_ids:
                        for y in x:
                            sql = "DELETE FROM userandtasklink  WHERE TID = %s"
                            val = (desired_task_id,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM task WHERE TID = %s"
                            val = (desired_task_id,)
                            cursor.execute(sql, val)
                            db.commit()

                    print("Tasks deleted.")
                    valid = True
                elif confirmation == "NO" or confirmation == "N":
                    sql = "DELETE FROM userandtasklink  WHERE TID = %s"
                    val = (desired_task_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    sql = "DELETE FROM task WHERE TID = %s"
                    val = (desired_task_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    print("Task deleted.  ")
                    valid = True
                else:
                    print("Invalid  Input. Try Again.")
                    valid = False

    def __delete_event_plan(self):
        exists = []
        exit_loop = False
        while not exit_loop:
            exit_loop = True
            print("Options:  ")
            print("1) Search for an Event Plan")
            print("2) Show All Event Plans")
            choice = 0
            valid = False
            while not valid:
                try:
                    choice = int(input("Enter your choice: "))
                    valid = True
                except ValueError:
                    print("Invalid  Input. Try Again.")
                    valid = False
            if choice == 1:
                exists = self.__search_event_plan()
            elif choice == 2:
                exists = self.__show_event_plans()
            else:
                print("Invalid  Input. Try Again.")
                exit_loop = False

        if exists[0]:
            desired_event_plan_id = 0
            valid = False
            while not valid:
                try:
                    desired_event_plan_id = int(
                        input(
                            "Enter the ID of the event plan you would like to delete: "
                        )
                    )
                    for i in range(len(exists[1])):
                        if (desired_event_plan_id) == exists[1][i][0]:
                            valid = True
                            break
                        else:
                            valid = False
                    if valid == False:
                        print("Invalid  ID. Try Again.")
                except ValueError:
                    print("Invalid Input. Try Again.")
                    valid = False
            valid = False
            while not valid:
                choice = (
                    input("Would you like to delete all related events as well (Y/N): ")
                ).upper()
                if choice in ("Y", "YES", "N", "NO"):
                    valid_2 = False
                    while not valid_2 and (choice == "YES" or choice == "Y"):
                        print(
                            "Would you like to delete all the repeats of these events as well? (Yes/No) "
                        )
                        confirmation = (input()).upper()
                        if choice in ("Y", "YES", "N", "NO"):
                            valid_2 = True
                        else:
                            print("Invalid  Input. Try Again.")
                            valid_2 = False
                    valid = True
                else:
                    print("Invalid  Input. Try Again.")
                    valid = False
            valid = False
            while not valid:
                print(
                    "Would you like to delete all repeats of this event plan as well? (Yes/No)  "
                )
                event_plan_confirmation = input().upper()
                if event_plan_confirmation == "YES" or event_plan_confirmation == "Y":
                    sql = "SELECT EPRepeatID  FROM eplan WHERE EPID = %s"
                    val = (desired_event_plan_id,)
                    cursor.execute(sql, val)
                    desired_repeat_id = cursor.fetchall()

                    sql = "SELECT EPID FROM eplan WHERE EPRepeatID  = %s"
                    val = (desired_repeat_id[0][0],)
                    cursor.execute(sql, val)
                    desired_event_plan_ids = cursor.fetchall()

                    for x in desired_event_plan_ids:
                        for y in x:
                            if choice == "Y" or choice == "YES":
                                sql = (
                                    "SELECT EID FROM eventandeplanlink  WHERE EPID = %s"
                                )
                                val = (y,)
                                cursor.execute(sql, val)
                                event_id_list = cursor.fetchall()

                                if confirmation == "YES" or confirmation == "Y":
                                    for x in event_id_list:
                                        for y in x:
                                            sql = "SELECT ERepeatID  FROM event WHERE EID = %s"
                                            val = (y,)
                                            cursor.execute(sql, val)
                                            desired_repeat_id = cursor.fetchall()

                                            sql = "SELECT EID FROM event WHERE ERepeatID  = %s"
                                            val = (desired_repeat_id[0][0],)
                                            cursor.execute(sql, val)
                                            desired_event_ids = cursor.fetchall()

                                            for i in desired_event_ids:
                                                for j in i:
                                                    sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                                                    val = (j,)
                                                    cursor.execute(sql, val)
                                                    db.commit()

                                                    sql = "DELETE FROM userandeventlink  WHERE EID= %s"
                                                    val = (j,)
                                                    cursor.execute(sql, val)
                                                    db.commit()

                                                    sql = "DELETE FROM event WHERE EID = %s"
                                                    val = (j,)
                                                    cursor.execute(sql, val)
                                                    db.commit()
                                elif confirmation == "No" or confirmation == "N":
                                    for x in event_id_list:
                                        for y in x:
                                            sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                                            val = (y,)
                                            cursor.execute(sql, val)
                                            db.commit()

                                            sql = "DELETE FROM userandevent link WHERE EID = %s"
                                            val = (y,)
                                            cursor.execute(sql, val)
                                            db.commit()

                                            sql = "DELETE FROM event WHERE EID = %s"
                                            val = (y,)
                                            cursor.execute(sql, val)
                                            db.commit()

                            sql = "DELETE FROM userandeplanlink  WHERE EPID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM eventandeplanlink  WHERE EPID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM eplan WHERE EPID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                    print("Event Plans deleted.  ")
                    valid = True
                elif event_plan_confirmation == "NO" or event_plan_confirmation == "N":
                    if choice == "Y" or choice == "YES":
                        sql = "SELECT EID FROM eventandeplanlink  WHERE EPID = %s"
                        val = (desired_event_plan_id,)
                        cursor.execute(sql, val)
                        event_id_list = cursor.fetchall()

                        if confirmation == "YES" or confirmation == "Y":
                            for x in event_id_list:
                                for y in x:
                                    sql = "SELECT ERepeatID  FROM event WHERE EID = %s"
                                    val = (y,)
                                    cursor.execute(sql, val)
                                    desired_repeat_id = cursor.fetchall()

                                    sql = "SELECT EID FROM event WHERE ERepeatID  = %s"
                                    val = (desired_repeat_id[0][0],)
                                    cursor.execute(sql, val)
                                    desired_event_ids = cursor.fetchall()

                                    for i in desired_event_ids:
                                        for j in i:
                                            sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                                            val = (j,)
                                            cursor.execute(sql, val)
                                            db.commit()

                                            sql = "DELETE FROM userandeventlink  WHERE EID = %s"
                                            val = (j,)
                                            cursor.execute(sql, val)
                                            db.commit()

                                            sql = "DELETE FROM event WHERE EID = %s"
                                            val = (j,)
                                            cursor.execute(sql, val)
                                            db.commit()
                        elif confirmation == "NO" or confirmation == "N":
                            for x in event_id_list:
                                for y in x:
                                    sql = (
                                        "DELETE FROM eventandeplanlink  WHERE EID = %s"
                                    )
                                    val = (y,)
                                    cursor.execute(sql, val)
                                    db.commit()

                                    sql = "DELETE FROM userandeventlink  WHERE EID = %s"
                                    val = (y,)
                                    cursor.execute(sql, val)
                                    db.commit()

                                    sql = "DELETE FROM event WHERE EID = %s"
                                    val = (y,)
                                    cursor.execute(sql, val)
                                    db.commit()

                    sql = "DELETE FROM userandeplanlink  WHERE EPID = %s"
                    val = (desired_event_plan_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    sql = "DELETE FROM eventandeplanlink  WHERE EPID = %s"
                    val = (desired_event_plan_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    sql = "DELETE FROM eplan WHERE EPID = %s"
                    val = (desired_event_plan_id,)
                    cursor.execute(sql, val)
                    db.commit()

                    print("Event Plan deleted.  ")
                    valid = True
                else:
                    print("Invalid  Input. Try Again.")
                    valid = False

    def __delete_all_data(self):
        confirmation = (
            input("Are you sure you would like to delete all data (Y/N): ")
        ).upper()
        if confirmation == "Y" or confirmation == "YES":
            pswd_confirm = input("Enter password  for confirmation:  ")
            if self.user_obj.check_password(pswd_confirm, self.current_user_id):
                sql = "SELECT TID FROM userandtasklink  WHERE UID = %s"
                val = (self.current_user_id,)
                cursor.execute(sql, val)
                task_id_list = cursor.fetchall()

                for x in task_id_list:
                    for y in x:
                        sql = "DELETE FROM userandtasklink  WHERE TID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                        sql = "DELETE FROM task WHERE TID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                sql = "SELECT EID FROM userandeventlink  WHERE UID = %s"
                val = (self.current_user_id,)
                cursor.execute(sql, val)
                event_id_list = cursor.fetchall()

                for x in event_id_list:
                    for y in x:
                        sql = "DELETE FROM userandeventlink  WHERE EID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                        sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                        sql = "DELETE FROM event WHERE EID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                sql = "SELECT EPID FROM userandeplanlink  WHERE UID = %s"
                val = (self.current_user_id,)
                cursor.execute(sql, val)
                event_plan_id_list = cursor.fetchall()

                for x in event_plan_id_list:
                    for y in x:
                        sql = "DELETE FROM userandeplanlink  WHERE EPID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                        sql = "DELETE FROM eplan WHERE EPID = %s"
                        val = (y,)
                        cursor.execute(sql, val)
                        db.commit()

                sql = "ALTER TABLE event AUTO_INCREMENT  = 1"
                cursor.execute(sql)
                db.commit()

                sql = "ALTER TABLE task AUTO_INCREMENT  = 1"
                cursor.execute(sql)
                db.commit()

                sql = "ALTER TABLE eplan AUTO_INCREMENT  = 1"
                cursor.execute(sql)
                db.commit()
            else:
                print("Data not deleted.")
        else:
            print("Data not deleted.")

    def __delete_user(self):
        if self.__login():
            confirmation = (
                input("Are you sure you want to delete your user (Y/N): ")
            ).upper()

            if confirmation == "Y" or confirmation == "YES":
                password = input("Enter password  for confirmation:  ")
                if self.user_obj.check_password(password, self.current_user_id):
                    sql = "SELECT TID FROM userandtasklink  WHERE UID = %s"
                    val = (self.current_user_id,)
                    cursor.execute(sql, val)
                    task_id_list = cursor.fetchall()

                    for x in task_id_list:
                        for y in x:
                            sql = "DELETE FROM userandtasklink  WHERE TID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM task WHERE TID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                    sql = "SELECT EID FROM userandeventlink  WHERE UID = %s"
                    val = (self.current_user_id,)
                    cursor.execute(sql, val)
                    event_id_list = cursor.fetchall()

                    for x in event_id_list:
                        for y in x:
                            sql = "DELETE FROM userandeventlink  WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM eventandeplanlink  WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM event WHERE EID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                    sql = "SELECT EPID FROM userandeplanlink  WHERE UID = %s"
                    val = (self.current_user_id,)
                    cursor.execute(sql, val)
                    event_plan_id_list = cursor.fetchall()

                    for x in event_plan_id_list:
                        for y in x:
                            sql = "DELETE FROM userandeplanlink  WHERE EPID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                            sql = "DELETE FROM eplan WHERE EPID = %s"
                            val = (y,)
                            cursor.execute(sql, val)
                            db.commit()

                    sql = "DELETE FROM user WHERE UID = %s"
                    val = (self.current_user_id,)
                    cursor.execute(sql, val)
                    db.commit()
                else:
                    print("Data not deleted.")
            else:
                print("Data not deleted.")

    @staticmethod
    def __error_checker(issue, val_1, val_2=None):
        # function  that is responsible  for input format and error checking
        if val_2 is None:
            if issue == "Date":
                # checking  whether the format of a string input meets the required  date format

                check_format = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                # list that checks each format requirement

                if len(val_1) == 10:
                    # checking  whether the length of the string is the required  size

                    counter = 0  # counter to iterate an shift the index of the check_format  list
                    for x in val_1:
                        if val_1.index(x) in [0, 1, 2, 3, 5, 6, 8, 9]:
                            # indices of values that should be digits

                            if x.isdigit():
                                # condition  to check if value is a digit

                                check_format[counter] = 1
                            else:
                                check_format[counter] = 0
                        # indices of values that should be hyphens
                        elif val_1.index(x) in [4, 7]:
                            if x == "-":
                                check_format[counter] = 1
                            else:
                                check_format[counter] = 0
                        counter += 1
                    if (
                        check_format[0] == 1
                        and check_format[1] == 1
                        and check_format[2] == 1
                        and check_format[3] == 1
                    ):
                        # algorithm  to check whether the entered year is a leap year
                        year = (
                            (int(val_1[0]) * 1000)
                            + (int(val_1[1]) * 100)
                            + (int(val_1[2]) * 10)
                            + (int(val_1[3]))
                        )
                        if year % 4 == 0:
                            if year % 100 == 0:
                                if year % 400 == 0:
                                    leap_year = True
                                else:
                                    leap_year = False
                            else:
                                leap_year = True
                        else:
                            leap_year = False
                        if check_format[5] == 1 and check_format[6] == 1:
                            month = (int(val_1[5]) * 10) + int(val_1[6])
                            if 1 <= month <= 12:
                                # checking  whether the month value is in the right range

                                check_format[10] = 1
                                if check_format[8] == 1 and check_format[9] == 1:
                                    day = (int(val_1[8]) * 10) + int(val_1[9])
                                    # checking  if day is within limits for the corresponding  month
                                    if month in [1, 3, 5, 7, 8, 10, 12]:
                                        # Jan, March, May, July, August, October,  Dec

                                        if 1 <= day <= 31:
                                            check_format[11] = 1
                                        else:
                                            check_format[11] = 0
                                    elif month in [4, 6, 9, 11]:
                                        # April, June, September,  November

                                        if 1 <= day <= 30:
                                            check_format[11] = 1
                                        else:
                                            check_format[11] = 0
                                    elif month == 2:  # February
                                        # factoring  in leap years for february

                                        if leap_year:
                                            if 1 <= day <= 29:  # leap year
                                                check_format[11] = 1
                                            else:
                                                check_format[11] = 0
                                        else:
                                            if 1 <= day <= 28:  # non-leap year
                                                check_format[11] = 1
                                            else:
                                                check_format[11] = 0
                            else:
                                check_format[10] = 0
                                check_format[11] = 0
                        else:
                            check_format[10] = 0
                            check_format[11] = 0
                    else:
                        check_format[10] = 0
                        check_format[11] = 0
                else:
                    check_format = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                if 0 in check_format:
                    # condition  to return whether the accepted date meets all format requirements
                    return False
                else:
                    return True
            elif issue == "Blank":  # checking  whether an accepted  string is blank
                if val_1.strip() == "":
                    return False
                else:
                    return True
            elif issue == "Bool":
                # checking  whether a string input is yes or no and respectively  assigning  1 or 0
                if val_1 == "Y" or val_1 == "YES":
                    return "1"
                elif val_1 == "N" or val_1 == "No":
                    return "0"
                else:
                    return "Invalid"
            elif issue == "Notes":
                # checking  whether an accepted  string is more than 1000 characters  long
                if len(val_1) > 1000:
                    return False
                else:
                    return True
            elif issue == "Repeat":
                # checking  whether string input corresponds  to a valid repeat cycle
                if val_1 in ["NONE", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"]:
                    return True
                else:
                    return False
            elif issue == "Time":
                # checking  whether the format of the string input meets the required  time format

                check_format = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                # list to mark of all format points for the time value

                if len(val_1) == 8:  # checking  the length of the accepted  value
                    counter = 0
                    for x in val_1:
                        if val_1.index(x) in [0, 1, 3, 4, 6, 8]:
                            # indices of the hour, minute, and second values

                            if (
                                x.isdigit()
                            ):  # checking  if they are all numerical  values
                                check_format[counter] = 1
                            else:
                                check_format[counter] = 0

                        elif x == ":":  # checking  if the separators  are colons
                            check_format[counter] = 1
                        else:
                            check_format[counter] = 0

                        counter += 1
                    if check_format[0] == 1 and check_format[1] == 1:
                        hour = (int(val_1[0]) * 10) + int(val_1[1])
                        if (
                            0 <= hour <= 23
                        ):  # checking  if the hour value is within a 24 hour range
                            check_format[8] = 1
                        else:
                            check_format[8] = 0

                    if check_format[3] == 1 and check_format[4] == 1:
                        minute = (int(val_1[3]) * 10) + int(val_1[4])
                        if 0 <= minute <= 59:
                            # checking  whether the minute value is within a 60 minute range
                            check_format[9] = 1
                        else:
                            check_format[9] = 0

                    if check_format[6] == 1 and check_format[8] == 1:
                        second = (int(val_1[6]) * 10) + int(val_1[7])
                        if 0 <= second <= 59:
                            # checking  whether the second value is within a 60 second range
                            check_format[10] = 1
                        else:
                            check_format[10] = 0
                else:
                    check_format = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                if (
                    0 in check_format
                ):  # returning  whether all formatting  conditions  have been met
                    return False
                else:
                    return True
            elif (
                issue == "Completion"
            ):  # checking  whether a string input is either a 1 or a 0
                if val_1.isdigit():
                    if int(val_1) == 0 or int(val_1) == 1:
                        return True
                    else:
                        return False

                else:
                    return False
        else:
            if issue == "Overlap  Date":
                year_1 = (
                    (int(val_1[0]) * 1000)
                    + (int(val_1[1]) * 100)
                    + (int(val_1[2]) * 10)
                    + int(val_1[3])
                )
                year_2 = (
                    (int(val_2[0]) * 1000)
                    + (int(val_2[1]) * 100)
                    + (int(val_2[2]) * 10)
                    + int(val_2[3])
                )
                if year_2 < year_1:
                    return True

                month_1 = (int(val_1[5]) * 10) + int(val_1[6])
                month_2 = (int(val_2[5]) * 10) + int(val_2[6])
                if year_2 == year_1:
                    if month_2 < month_1:
                        return True

                day_1 = (int(val_1[8]) * 10) + int(val_1[9])
                day_2 = (int(val_2[8]) * 10) + int(val_2[9])
                if year_2 == year_1:
                    if month_2 == month_1:
                        if day_2 < day_1:
                            return True

                return False
            elif issue == "Overlap  Time":
                hour_1 = (int(val_1[0]) * 10) + int(val_1[1])
                hour_2 = (int(val_2[0]) * 10) + int(val_2[1])
                if hour_2 < hour_1:
                    return True

                minute_1 = (int(val_1[3]) * 10) + int(val_1[4])
                minute_2 = (int(val_2[3]) * 10) + int(val_2[4])
                if hour_2 == hour_1:
                    if minute_2 < minute_1:
                        return True

                second_1 = (int(val_1[6]) * 10) + int(val_1[7])
                second_2 = (int(val_2[6]) * 10) + int(val_2[7])
                if hour_2 == hour_1:
                    if minute_2 == minute_1:
                        if second_2 < second_1:
                            return True

                return False


calendar_obj = Calendar()
calendar_obj.main_menu()
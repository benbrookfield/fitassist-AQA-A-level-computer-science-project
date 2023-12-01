from tkinter import * #import tkinter to make GUI
from tkinter import ttk #import ttk tkinter library to get extra features
from tkinter import messagebox #import messageboxes module to create messageboxes so users can be infromed about errors
import datetime #import datetime module to find current date and time
import sqlite3 #import sqlite3 so database can be acessed and queried
from datetime import timedelta #import timedelta so I can subtract days from todays date



#user class, allows object to be made holding all of a users detials, which can be retrieved and modified. This stops me having to query the database every time I want user information
class User: #create User class to store info about users
  def __init__(self, id, firstname, lastname, weight, height, gender, yearborn, monthborn, dayborn, password, target_intake, exercise_level, calories_eaten): #initialise class and set attributes

    #set all attributes equal to different variables
    self.__id = id
    self.__firstname = firstname
    self.__lastname = lastname
    self.__weight = weight
    self.__height = height
    self.__gender = gender
    self.__yearborn = yearborn
    self.__monthborn = monthborn
    self.__dayborn = dayborn
    self.__password = password
    self.__target_intake = target_intake
    self.__exercise_level = exercise_level
    self.__calories_eaten = calories_eaten

  def get_id(self): #create function to return user's ID
    return self.__id
        
  def get_firstname(self): #create function to return user's first name
    return self.__firstname

  def get_lastname(self): #create function to return user's last name
    return self.__lastname

  def get_weight(self): #create function to return user's weight
    return self.__weight

  def get_height(self): #create function to return user's height
    return self.__height

  def get_gender(self): #create function to return user's gender
    return self.__gender

  def get_yearborn(self): #create function to return the year a user was born
    return self.__yearborn

  def get_monthborn(self): #create function to return the month a user was born
    return self.__monthborn

  def get_dayborn(self): #create function to return the day a user was born
    return self.__dayborn

  def get_age(self): #create function to return user's age
    return self.__age

  def get_password(self): #create function to return user's password
    return self.__password

  def get_target_intake(self): #create function to return user's target intake
    return self.__target_intake

  def get_exercise_level(self): #create function to return user's exercise level
    return self.__exercise_level

  def set_id(self, id): #create function to set user's ID
    self.__id = id
        
  def set_firstname(self, firstname): #create function to set user's first name
    self.__firstname = firstname

  def set_lastname(self, lastname): #create function to set user's last name
    self.__lastname = lastname

  def set_weight(self, weight): #create function to set user's weight
    self.__weight = weight

  def set_height(self, height): #create function to set user's height
    self.__height = height

  def set_password(self, password): #create function to set user's password
    self.__password = password 

  def set_gender(self, gender): #create function to set user's gender
    self.__gender = gender

  def set_dayborn(self, dayborn): #create function to set user's day born
    self.__dayborn = dayborn

  def set_monthborn(self, monthborn): #create function to set user's month born
    self.__monthborn = monthborn

  def set_yearborn(self, yearborn): #create function to set user's year born
    self.__yearborn = yearborn

  def set_age(self, age): #create function to set user's age
    self.__age = age
      
  def set_target_intake(self, target_intake): #create function to set user's target calorie intake
    self.__target_intake = target_intake

  def set_exercise_level(self, exercise_level): #create function to set user's exercise level
    self.__exercise_level = exercise_level

user_logged_in = User(0,"","",0,0, "", 0, 0, 0, "", 0, 0, 0) #create user_logged_in object to store details of user logged in, all attributes are currently set to 0 or " " as no user is logged in at the start of the program



database_connection = sqlite3.connect('fitness_assistant.db') #connect database to code
database_cursor = database_connection.cursor()

#create iid variables which automatically goes up every time something is added to treeview, so that things can be added.
iidnumb = 0
iidnumb2 = 0 
iidnumb3 = 0
iidnumb4 = 0

def hash(password):
  unhashed_password = "" #create empty hashed password variable to put hashed password into
  for letter in password:
    unhashed_password = unhashed_password + str(ord(letter)) #go through every letter in password and turn it into unicode value, append this value to the unshahed_password string
    
  password_int = int(unhashed_password) #turn password into an integer so that I can use mod function on it
  hashed_password = str(password_int % 118147) #mod value by prime number, remainder is the hash value
  return hashed_password




#login window
def login():
  login_window = Tk() #create login window
  login_window.title("Login") #set window title
  login_window.geometry("300x100") #set window dimensions
  login_window.configure(bg="white") #set window background

  #create "login" label so user knows they are in login page
  title_label = Label(login_window, text="Login", bg="white")
  title_label.grid(row=0, column=0, padx=30, columnspan=2)

  #create user ID entry
  user_label = Label(login_window, text="User ID:", bg="white")
  user_label.grid(row=1, column=0, padx=30)
  user_entry = Entry(login_window, width=15)
  user_entry.grid(row=1, column=1)

  #create password entry
  password_label = Label(login_window, text="Password:", bg="white", )
  password_label.grid(row=2, column=0, padx=30)
  password_entry = Entry(login_window, width=15, show="*")
  password_entry.grid(row=2, column=1)

  #create button to submit user ID and password
  submit_button = Button(login_window, text="Submit", command=lambda: login_submit(login_window, user_entry.get(), password_entry.get()))
  submit_button.grid(row=3, column=1)

  #create button to create a new account
  new_user_button = Button(login_window, text="New User", command=lambda: newuser_submit(login_window))
  new_user_button.grid(row=3, column=0)

  login_window.mainloop()

#create account window
def newuser_submit(login_window):
  login_window.destroy() #close login window
  newuser_window = Tk() #create window
  newuser_window.title("Create Account") #set window title
  newuser_window.geometry("380x215") #set window dimensions
  newuser_window.configure(bg="white") #set window background

  newuser_label = Label(newuser_window, text="New User", bg="white")
  newuser_label.grid(row=0, column=0, columnspan=4, padx=50)

  #create password
  password_label = Label(newuser_window, text="New Password:", bg="white")
  password_label.grid(row=1, column=0, padx=30)
  password_entry = Entry(newuser_window, width=27)
  password_entry.grid(row=1, column=1, columnspan=3)

  #enter first name
  firstname_label = Label(newuser_window, text="First Name:", bg="white")
  firstname_label.grid(row=2, column=0, padx=30)
  firstname_entry = Entry(newuser_window, width=27)
  firstname_entry.grid(row=2, column=1, columnspan=3)

  #enter last name
  lastname_label = Label(newuser_window, text="Last Name:", bg="white")
  lastname_label.grid(row=3, column=0, padx=30)
  lastname_entry = Entry(newuser_window, width=27)
  lastname_entry.grid(row=3, column=1, columnspan=3)

  #enter gender
  gender_label = Label(newuser_window, text="Gender:", bg="white")
  gender_label.grid(row=4, column=0)
  genders = ["Male", "Female"] #set values for gender dropdown
  gender_entry = ttk.Combobox(newuser_window, values=genders, width=26, state="readonly") #make combobo readoonly so only "male" or "female" can be entered
  gender_entry.grid(row=4, column=1, columnspan=3)

  #enter date of birth
  dob_label = Label(newuser_window, text="Date of Birth:", bg="white")
  dob_label.grid(row=5, column=0, padx=30)

  #year, month, and day born must be entered individually
  dob_year_entry = Entry(newuser_window, width=8)
  dob_month_entry = Entry(newuser_window, width=8)
  dob_day_entry = Entry(newuser_window, width =8)
  dob_year_entry.grid(row=5, column=3)
  dob_month_entry.grid(row=5, column=2)
  dob_day_entry.grid(row=5, column=1)
          
  #enter height
  height_label = Label(newuser_window, text="Height (cm):", bg="white")
  height_label.grid(row=7, column=0, padx=30)
  height_entry = Entry(newuser_window, width=27)
  height_entry.grid(row=7, column=1, columnspan=3)

  #enter weight
  weight_label = Label(newuser_window, text="weight (kg):", bg="white")
  weight_label.grid(row=8, column=0, padx=30)
  weight_entry = Entry(newuser_window, width=27)
  weight_entry.grid(row=8, column=1, columnspan=3)

  #enter exercise level
  exercise_level_label = Label(newuser_window, text="Exercise level:", bg="white")
  exercise_level_label.grid(row=9, column=0, padx=30)
  exercise_levels = ["couch potato", "moderately active (1hr daily)", "vigorously active (2 hours per day)", "extremely active (>2 hours per day)"] #set values for activity level dropdown
  exercise_level_entry = ttk.Combobox(newuser_window, values=exercise_levels, width=26, state="readonly") #dropdown to select activity level
  exercise_level_entry.grid(row=9, column=1, columnspan=3)

  #button to submit details adn create and account
  submitaccount_button = Button(newuser_window, text="Submit", command=lambda:createaccount (newuser_window, password_entry.get(), firstname_entry.get(), lastname_entry.get(), gender_entry.get(), dob_day_entry.get(), dob_month_entry.get(), dob_year_entry.get(), height_entry.get(), weight_entry.get(), exercise_level_entry.get()))
  submitaccount_button.grid(row=10,column=0, columnspan=4)


#calculate the users age from date of birth
def calculate_age():
    #turn year, month and day born into integers so they can be used in aequation to find age
    yearborn = int(user_logged_in.get_yearborn())
    monthborn = int(user_logged_in.get_monthborn())
    dayborn = int(user_logged_in.get_dayborn())
    birthDate = datetime.datetime(yearborn, monthborn, dayborn) #combine day, month and day born to make one date
    today = datetime.datetime.now() #user datetime module to get todays date
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) #subtract birth date from current date to find users age
    user_logged_in.set_age(age) #add age to user_logged_in object
    return(age)


#check a date entered by user is real
def check_date_is_real(day, month, year):
  if day.isnumeric() and month.isnumeric() and year.isnumeric(): #checks values entered are numbers

    #make day, month, and year variables integers, so that functions such as > can be used on them
    day = int(day)
    month = int(month)
    year = int(year)
    
    if month > 12 or month == 0: #checks if month is larger than twelve, returns false if is is
      return False
            
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: #checks if month entered has 31 days
      if day <= 31 and day >= 1: #checks day entered is 31 or less
        return True
      else: #if month has more than 31 or less than 1 days, return false
        return False

    if month == 4 or month == 6 or month == 9 or month == 11: #checks if month is one with 30 days
      if day <= 30 and day >= 1: #if month is one with 30 days, checks day is less than or equal to 30
        return True
      else: #if month has more than 30 or less than 1 days, return false
        return False

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): #calculates wether or not year given is a leap year
      if day <= 29 and day >= 1: #if year is a leap year, checks if Feruary has 29 or less days
        return True
      else: #if month has more than 29 or less than 1 days, return false
        return False
    else:
      if day <= 28 and day >= 1: #if year isn't a leap year, checks if Febrary has 28 or less days
        return True
      else: #if month has more than 28 or less than 1 days, return false
        return False
              
  else: #if vlaues given are non numeric, return false
    return False


#enter deatils of a new user into database
def createaccount(newuser_window, password, firstname, lastname, gender, dayborn, monthborn, yearborn, height, weight, exerciselvl):

  #turn exercise level into an integer so it can go in the database
  if exerciselvl == "couch potato":
    exerciselvl = 1
  elif exerciselvl == "moderately active (1hr daily)":
    exerciselvl = 2
  elif exerciselvl == "vigorously active (2 hours per day)":
    exerciselvl = 3
  elif exerciselvl == "extremely active (>2 hours per day)":
    exerciselvl = 4
  else:
    messagebox.showerror(title="Error", message="Please enter a valid exercise level") #if exercise level given is not one of 4 options, show error
        
  #check data has been entered into all entries
  if password == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter a password")
    return None
        
  elif firstname == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your first name")
    return None
        
  elif lastname == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your last name")
    return None
        
  elif gender == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please select your gender")
    return None
        
  elif dayborn == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your date of birth")
    return None
        
  elif monthborn == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your date of birth")
    return None
        
  elif yearborn == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your date of birth")
    return None
        
  #check date of birth entered is an actual, real date
  elif check_date_is_real(dayborn, monthborn, yearborn) == False:
    messagebox.showerror(title="Error", message="Please enter a valid date of birth (dd/mm/yyyy)")
    return None
          
  elif height == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your height")
    return None
        
  #check height is a integer
  elif height.isdigit() == False:
    messagebox.showerror(title="Error", message="Please enter a valid height")
    return None
        
  elif weight == "": #check data has been entered
    messagebox.showerror(title="Error", message="Please enter your weight")
    return None
        
  #check weight is an integer
  elif weight.isnumeric() == False:
    messagebox.showerror(title="Error", message="Please enter a valid weight")
    return None
        
  else:
    with database_connection: #make connection to database
      sql_statement = "INSERT INTO TblUsers (firstname, lastname, gender, weight, height, yearborn, monthborn, dayborn, password, exerciselvl) VALUES ('%s', '%s', '%s', %s, %s, %s, %s, %s, '%s', %s)" % (firstname, lastname, gender, weight, height, yearborn, monthborn, dayborn, hash(password), exerciselvl) #insert data into new record in TblUsers (password is hashed)
      database_cursor.execute(sql_statement) #execute statment
      database_connection.commit() #commit changes to database

      sql_statement_2 = "SELECT MAX(userID) FROM TblUsers" #find most recent user ID entered into table (from the account that has just been created) so it can be entered into user_logged_in object
      database_cursor.execute(sql_statement_2)
      matching_users = database_cursor.fetchall()

    #insert details entered for account creation into user_logged_in object
    user_logged_in.set_id(matching_users[0][0])
    user_logged_in.set_firstname(firstname)
    user_logged_in.set_lastname(lastname)
    user_logged_in.set_weight(weight)
    user_logged_in.set_height(height)
    user_logged_in.set_password(password)
    user_logged_in.set_gender(gender)
    user_logged_in.set_yearborn(yearborn)
    user_logged_in.set_monthborn(monthborn)
    user_logged_in.set_dayborn(dayborn)
    user_logged_in.set_exercise_level(exerciselvl)
          
    calorie_target_page() #load calorie target page so user can choose calorie intake target
    newuser_window.destroy() #close new user window


#create calorie target page
def calorie_target_page():

  #set physical activity ratir based on activity level of user so maintenacne calories can be calculated
  if user_logged_in.get_exercise_level() == 1:
    physical_activity_ratio = 1.55
  elif user_logged_in.get_exercise_level() == 2:
    physical_activity_ratio = 1.85
  elif user_logged_in.get_exercise_level() == 3:
    physical_activity_ratio = 2.2
  elif user_logged_in.get_exercise_level() == 4:
    physical_activity_ratio = 2.4
        
  maintenance_cals = ((10 * int(user_logged_in.get_weight())) + (6.25 * int(user_logged_in.get_height())) - (5 * int(calculate_age()))) * int(physical_activity_ratio) #calculate maintenance calorie intake

  #subtract 166 from maintenance calorie intake if user is female
  if user_logged_in.get_gender() == "Female":
    maintenance_cals = maintenance_cals - 166

  #create different intake targets for different weight gain/loss goals
  rapidgaincals = int(round(maintenance_cals + 500))
  mildgaincals = int(round(maintenance_cals + 250))
  mildlosscals = int(round(maintenance_cals - 250))
  rapidlosscals = int(round(maintenance_cals - 500))
  maintenance_cals = int(round(maintenance_cals))
        
        
  #create window
  calorie_target_window = Tk() #create window for calorie target page
  calorie_target_window.title("User ID: " + str(user_logged_in.get_id())) #set title for window
  calorie_target_window.geometry("365x100") #set dimensions of window
  calorie_target_window.configure(bg="white") #set background of window

  choose_cals = Label(calorie_target_window, height = 1, width = 21, text = "Select target calorie intake", bg="white", font = ("Imperial", 15))
  choose_cals.grid(column=0, row=0, columnspan=5)


  #place buttons and labels on screen for user to select different calorie intakes
  rapid_gain_label = Label(calorie_target_window, text = '''+0.5kg 
  per month''', bg="white")
  rapid_gain_label.grid(column=0, row=1)
  rapid_gain_button = Button(calorie_target_window, height=1, width=4, text=rapidgaincals, command=lambda:inputcalstarget(rapidgaincals, calorie_target_window))
  rapid_gain_button.grid(column=0, row=2)

  mild_gain_label = Label(calorie_target_window, text = '''+0.25kg 
  per month''', bg="white")
  mild_gain_label.grid(column=1, row=1)
  mild_gain_button = Button(calorie_target_window, height=1, width=4, text = mildgaincals, command=lambda:inputcalstarget(mildgaincals, calorie_target_window))
  mild_gain_button.grid(column=1, row=2)

  maintain_label = Label(calorie_target_window, text = '''maintain 
  weight''', bg="white")
  maintain_label.grid(column=2, row=1)
  maintain_button = Button(calorie_target_window, height=1, width=4, text = maintenance_cals, command=lambda:inputcalstarget(maintenance_cals, calorie_target_window))
  maintain_button.grid(column=2, row=2)

  mild_loss_label = Label(calorie_target_window, text = '''-0.25kg 
  per month''', bg="white")
  mild_loss_label.grid(column=3, row=1)
  mild_loss_button = Button(calorie_target_window, height=1, width=4, text = mildlosscals, command=lambda:inputcalstarget(mildlosscals, calorie_target_window))
  mild_loss_button.grid(column=3, row=2)

  rapid_loss_label = Label(calorie_target_window, text = '''-0.5kg 
  per month''', bg="white")
  rapid_loss_label.grid(column=4, row=1)
  rapid_loss_button = Button(calorie_target_window, height=1, width=4, text = rapidlosscals, command=lambda:inputcalstarget(rapidloscals, calorie_target_window))
  rapid_loss_button.grid(column=4, row=2)


#enter calories target to database
def inputcalstarget(calories, calorie_target_window):
  with database_connection:
          
    
    user_id = user_logged_in.get_id()
    print(calories)
    print(user_id)
    print(type(calories))
    print(type(user_id))
    sql_statement = "UPDATE TblUsers SET targetintake = %s WHERE userID = %s" % (calories, user_id) #insert target calories into user record
    database_cursor.execute(sql_statement)
    database_connection.commit() #commit changes
  user_logged_in.set_target_intake(calories) #add target intake to user_logged_in object
  calorie_target_window.destroy() #destory calorie target window as it is no longer needed
  nutrition_and_workout_page() #load nutrition page as calorie target has been chosen









  
#submit login details, check database to see if they are valid, pull user info from databse and put into user_logged_in object, and continue to nutrition page
def login_submit(login_window, userID, password):

  if userID == "": #check userID has been entered
      messagebox.showerror(title="Error", message="Please enter a user ID")
        
  if userID.isnumeric():
    if userID == "": #check userID has been entered
      messagebox.showerror(title="Error", message="Please enter a user ID")
    elif password == "": #check password has been entered
      messagebox.showerror(title="Error", message="Please enter a password")
    else:
      with database_connection:
        sql_statement = "SELECT * FROM TblUsers WHERE userID = %s AND Password = '%s'" % (userID, hash(password)) #select record from TblUsers with mathcing username and password (password is hashed)
        database_cursor.execute(sql_statement)
        matching_users = database_cursor.fetchall()
      if len(matching_users) == 1: #check there is only 1 record with a matching userID and password
        #take all data from matching results in databse and add to user_logged_in object
        user_logged_in.set_id(matching_users[0][0])
        user_logged_in.set_firstname(matching_users[0][1])
        user_logged_in.set_lastname(matching_users[0][2])
        user_logged_in.set_weight(matching_users[0][3])
        user_logged_in.set_height(matching_users[0][4])
        user_logged_in.set_password(matching_users[0][5])
        user_logged_in.set_gender(matching_users[0][6])
        user_logged_in.set_yearborn(matching_users[0][7])
        user_logged_in.set_monthborn(matching_users[0][8])
        user_logged_in.set_dayborn(matching_users[0][9])
        user_logged_in.set_target_intake(matching_users[0][11])
        user_logged_in.set_exercise_level(matching_users[0][12])
        sql_statement = "UPDATE TblUsers SET age = %s WHERE userID = %s" % (calculate_age(), user_logged_in.get_id()) #recalculate and update age of user incase they have gotten a year older
        database_cursor.execute(sql_statement)
        database_connection.commit()
        login_window.destroy() #close login window as login process is now complete
        nutrition_and_workout_page() #open nutrition page
      else:
        messagebox.showerror(title="Error", message="Username or password is incorrect") #if credentials entered do not match to and databse records, ask the user to reenter username and/or password
  else:
    messagebox.showerror(title="Error", message="User ID must be a number.") #show error message is user ID given is not a number

#this subroutine logs the user out, and resets all user_logged_in values
def logout(main_window):

  #clear all attrivutes in user_logged_in and set them to 0
  user_logged_in.set_id(0)
  user_logged_in.set_firstname("")
  user_logged_in.set_lastname("")
  user_logged_in.set_weight(0)
  user_logged_in.set_height(0)
  user_logged_in.set_password("")
  user_logged_in.set_gender("")
  user_logged_in.set_yearborn(0)
  user_logged_in.set_monthborn(0)
  user_logged_in.set_dayborn(0)
  user_logged_in.set_target_intake(0)
  user_logged_in.set_exercise_level(0)

  main_window.destroy() #close main window
  login() #open login window
  
#create main window with nutrition and workout page in
def nutrition_and_workout_page():
  #make window
  main_window = Tk()
  main_window.title("User ID: " + str(user_logged_in.get_id())) #display the users User ID in the window title
  main_window.geometry("365x690")

  logout_button = Button(main_window, width = 3, height =1, text = "Log out", command=lambda: logout(main_window))
  logout_button.grid(column=0, row=0)
        
  #add notebook to make different tabs
  notebook = ttk.Notebook(main_window)
  notebook.grid(column=0, row=1)
  
  #nutrition tab
  nutrition = Frame(notebook, width=1280, height=705, bg="white")
  nutrition.pack(fill="both", expand=1)
 
  #workout training tab
  workout = Frame(notebook, width=1280, height=705, bg="white")
  workout.pack(expand=1)

  #add tabs to top of screen
  notebook.add(nutrition, text="Nutrition Tracker")
  notebook.add(workout, text="Workout Tracker")

  #load nutrition page in the nutrition tab in the notebook
  nutrition_page(nutrition)

  #load workout page in the workout tab in the notebook
  workout_page(workout)

  main_window.mainloop()


#create nutrition page
def nutrition_page(nutrition):
  #make calories consumed title
  calorie_intake = Label(nutrition, height = 1, width=20, text="Calories Consumed:", bg="white", font=("Imperial", 20))
  calorie_intake.grid(row=0, column=0, pady=20)

  #make counter for calories consumed
  calorie_intake_counter = Label(nutrition, height = 1, width=10, text="", bg="white", font=("Imperial", 30))
        
  #make  calories consumed progress bar
  calorie_intake_counter.grid(row=1, column=0)
  calorie_intake_progress_bar = ttk.Progressbar(nutrition, orient=HORIZONTAL, length = 250, mode="determinate")
  calorie_intake_progress_bar.grid(row=3, column=0)

  #display calorie intake target
  target_label = Button(nutrition, height = 1, width= 13, bg="white", font=("Imperial", 20), command=lambda: calorie_target_page())
  target_label.grid(row=4, column=0)

  #make the treeview for calories consumed
  meal_record = ttk.Treeview(nutrition, height=5)
  meal_record["columns"] =  ("#1", "#2", "#3")
  
  meal_record.column("#0", anchor=CENTER, stretch=NO, width=0)
  meal_record.heading("#0", text = "")
  
  meal_record.column("#1", anchor=CENTER, stretch=NO, width=100)
  meal_record.heading("#1", text = "Meal")
        
  meal_record.column("#2", anchor=E, stretch=NO, width=50)
  meal_record.heading("#2", text="Time")
        
  meal_record.column("#3", anchor=CENTER, stretch=NO, width=100)
  meal_record.heading("#3", text="Calories")
  meal_record.grid(row=5, column=0, pady=10)

  #add all meals eaten today in database to meals treeview
  with database_connection:
    global iidnumb2 #bring iidnumb2 into function, so it can be used and updated when adding to treeview
    todays_date = datetime.datetime.now() #find todays date
    today_formatted_as_string = todays_date.strftime("%Y-%m-%d") #format todays date as a string
    
    sql_statement = "SELECT targetintake, Mealdesc, Timeeaten, Calories FROM TblUsers, TblMeals WHERE TblUsers.userID = TblMeals.userID AND TblUsers.userID = %s AND dateeaten = '%s'" % (user_logged_in.get_id(), today_formatted_as_string) #sql statment to find the details of all meals eaten today by current user, and their calorie target
    database_cursor.execute(sql_statement) #execute sql command
    matching_results = database_cursor.fetchall() #set matching_users variable equal to result of SQL query
    if len(matching_results) == 0: #check if there are any reuslts of the above SQL query
      target_label.config(text = "Target: " + str(user_logged_in.get_target_intake()) + "kcal") #set the text on target_label equal to the users target calorie intake
    else:
      target_label.config(text = "Target: " + str(matching_results[0][0]) + "kcal") #set the text on target_label equal to the users target calorie intake

    #this loop inputs all meals into treeview
    for x in range (len(matching_results)):
      meal_record.insert(parent="", index="end", iid = iidnumb2, text="parent", values=(matching_results[x][1], matching_results[x][2], matching_results[x][3])) #insert meals eaten today into treeview
      iidnumb2 = iidnumb2 + 1 #update iid number so things can be added to treeview in future
    sql_statement = "SELECT SUM(calories) FROM TblMeals WHERE dateeaten = '%s' AND userID = %s" % (today_formatted_as_string, user_logged_in.get_id()) #SQL statement to find the sum of all calories eaten today
    database_cursor.execute(sql_statement) #execute SQL statement
    total_calories = database_cursor.fetchall() #set total_calories variable equal to result of SQL statement

    #if the user has not inputted any meals today, set counter to 0
    if total_calories[0][0] == "None":
      total_calories = 0
    calorie_intake_counter.config(text=total_calories) #add total calories to total calorie counter
        
        
  addmealf = Frame(nutrition, bg="white") #create frame to put add meals menu in
  addmealf.grid(row=6, column=0)

  addm = Label(addmealf, text="Add a Meal", bg="white") #create a label to show where to enter a meal into database and treeview
  addm.grid(row=0, column=0, columnspan=4)

  addmeal = Label(addmealf, text="Meal", bg="white") #create label to show where to enter meal description
  addmeal.grid(row=1, column=0, padx=30)
  mealbox = Entry(addmealf, width=15) #create an entry to enter meal description
  mealbox.grid(row=2, column=0)

  addtime = Label(addmealf, text="Time", bg="white") #create a label to show where to enter the time a meal was eaten
  addtime.grid(row=1, column=1, padx=38, columnspan=2)

  minutes = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"] #set values for minutes
  hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"] #set values for hours

  hourselect = ttk.Combobox(addmealf, values=hours, width=3) #create dropdown to enter what hour a meal was eaten
  hourselect.current(0) #set default value in hourselect dropdown to the first data in the aray, "00"
  hourselect.grid(row=2, column=1)
  minuteselect = ttk.Combobox(addmealf, values=minutes, width=3) #create dropdown to enter what minute a meal was eaten
  minuteselect.current(0) #set default value in minuteselect dropdown to the first data in the aray, "00"
  minuteselect.grid(row=2, column=2)

  addcals = Label(addmealf, text="Calories", bg="white") #create a label to show users where calories are entered
  addcals.grid(row=1, column=3, padx=30) #place add calories label in screen
  calseatenbox = Entry(addmealf, width=15) #create entry to add how many calories were in a meal
  calseatenbox.grid(row=2, column=3) #place calseaten entry on screen

  add_data = Button(addmealf, text="Add", command=lambda: add_meal(calorie_intake_progress_bar, meal_record, mealbox, calseatenbox, hourselect, minuteselect, calorie_intake_counter)) #create button to add data to treeview & database
  add_data.grid(row=3, column=1, columnspan=2, pady=5) #place add data button on screen

      
  #create calorie defecit/surplus bar chart
  bar_chart_frame = Frame(nutrition, bg="white")
  bar_chart_frame.grid(row=7, column=0)

  #call bar chart function to plot the chart
  bar_chart(bar_chart_frame)




 ####################    WORKOUT PAGE   ####################
def workout_page(workout):
  #create treeview to enter and show workouts
  workout_record = ttk.Treeview(workout, height=10)
  workout_record["columns"] =  ("#1", "#2", "#3", "#4", "#5")
  
  workout_record.column("#0", anchor=CENTER, stretch=NO, width=0)
  workout_record.heading("#0", text = "")
  
  workout_record.column("#1", anchor=CENTER, stretch=NO, width=100)
  workout_record.heading("#1", text = "Exercise")
        
  workout_record.column("#2", anchor=E, stretch=NO, width=50)
  workout_record.heading("#2", text="Sets")
        
  workout_record.column("#3", anchor=CENTER, stretch=NO, width=50)
  workout_record.heading("#3", text="Reps")

  workout_record.column("#4", anchor=CENTER, stretch=NO, width=55)
  workout_record.heading("#4", text="Weight")

  workout_record.column("#5", anchor=CENTER, stretch=NO, width=100)
  workout_record.heading("#5", text="Comments")
  workout_record.grid(row=0, column=0, pady=10, columnspan=5) #place treeview on screen

  with database_connection:
    global iidnumb #import iidnumb so that data can be added to the treeview in the correct spot
    todays_date = datetime.datetime.now() #create todays_date variable equal to todays date using datetime module
    today_formatted_as_string = todays_date.strftime("%Y-%m-%d") #format todays_date into string
    
    sql_statement = "SELECT * FROM TblWorkout WHERE date = '%s' AND userID = %s" % (today_formatted_as_string, user_logged_in.get_id()) #sql statment to find all exercises done today by current user
    database_cursor.execute(sql_statement) #execute SQL statement
    matching_results = database_cursor.fetchall() #set matching_results variable equal to result of SQL query
    for x in range (len(matching_results)): #create for loop so that all exercises are added to treeview
      workout_record.insert(parent="", index="end", iid = iidnumb, text="parent", values=(matching_results[x][3], matching_results[x][4], matching_results[x][5], matching_results[x][6], matching_results[x][7])) #insert exercises performed today into treeview
      iidnumb = iidnumb + 1 #update iid number so things can be added to treeview in future

  enter_exercise_label = Label(workout, text="Add an exercise:", bg="white") #make label telling user to enter exercise
  enter_exercise_label.grid(row=1, column=0, columnspan=5)
  
  add_exercise = Label(workout, text="Exercise", bg="white") #create label to show where to enter exercise
  add_exercise.grid(row=2, column=0, padx=1)
  exercise_box = Entry(workout, width=10) #create an entry to enter exercise
  exercise_box.grid(row=3, column=0)

  add_sets = Label(workout, text="Sets", bg="white") #create label to show where to enter sets
  add_sets.grid(row=2, column=1, padx=1)
  sets_box = Entry(workout, width=5) #create an entry to enter sets performed
  sets_box.grid(row=3, column=1)

  add_reps = Label(workout, text="Reps", bg="white") #create label to show where to enter reps
  add_reps.grid(row=2, column=2, padx=1)
  reps_box = Entry(workout, width=5) #create an entry to enter reps
  reps_box.grid(row=3, column=2)

  add_weight = Label(workout, text="Weight", bg="white") #create label to show where to enter weight
  add_weight.grid(row=2, column=3, padx=1)
  weight_box = Entry(workout, width=5) #create an entry to enter weight
  weight_box.grid(row=3, column=3)

  add_comments = Label(workout, text="Comments", bg="white") #create label to show where to enter any comments about workout
  add_comments.grid(row=2, column=4, padx=1)
  comments_box = Entry(workout, width=10) #create an entry to enter any comments about wokout
  comments_box.grid(row=3, column=4)

  add_workout = Button(workout, text="Add", command=lambda: enter_workout(workout_record, exercise_box, sets_box, reps_box, weight_box, comments_box)) #create button to add info in entries to treeview and database
  add_workout.grid(row=4, column=0, columnspan=5, pady=10)


  find_workout_label = Label(workout, text="Find a workout:", bg="white") #create label to show users where they can search for a workout
  find_workout_label.grid(row=5, column=0, columnspan=5)

  day_label = Label(workout, text="Day", bg="white") #add label to show where to enter day
  day_label.grid(row=6, column=1)
  month_label = Label(workout, text="Month", bg="white") #add label to show where to enter month
  month_label.grid(row=6, column=2)
  year_label = Label(workout, text="year", bg="white") #add label to show where to enter year
  year_label.grid(row=6, column=3)
        
  find_workout_day = Entry(workout, width = 5) #make entry box for day
  find_workout_day.grid(row=7, column=1)

  find_workout_month = Entry(workout, width = 5) #make entry box for month
  find_workout_month.grid(row=7, column=2)

  find_workout_year = Entry(workout, width = 5) #make entry box for year
  find_workout_year.grid(row=7, column=3)

  find_workout_button = Button(workout, text="Search", command=lambda: find_workout(old_workout_record, find_workout_day, find_workout_month, find_workout_year)) #create buton to find workout from date entered by user
  find_workout_button.grid(row=7, column=4)


  #create treeview to show past workouts
  old_workout_record = ttk.Treeview(workout, height=10)
  old_workout_record["columns"] =  ("#1", "#2", "#3", "#4", "#5")
  
  old_workout_record.column("#0", anchor=CENTER, stretch=NO, width=0)
  old_workout_record.heading("#0", text = "")
  
  old_workout_record.column("#1", anchor=CENTER, stretch=NO, width=100)
  old_workout_record.heading("#1", text = "Exercise")
        
  old_workout_record.column("#2", anchor=CENTER, stretch=NO, width=50)
  old_workout_record.heading("#2", text="Sets")
        
  old_workout_record.column("#3", anchor=CENTER, stretch=NO, width=50)
  old_workout_record.heading("#3", text="Reps")

  old_workout_record.column("#4", anchor=CENTER, stretch=NO, width=55)
  old_workout_record.heading("#4", text="Weight")

  old_workout_record.column("#5", anchor=CENTER, stretch=NO, width=100)
  old_workout_record.heading("#5", text="Comments")
  old_workout_record.grid(row=8, column=0, pady=10, columnspan=5) #place treeview on screen
  





#give the option to add a meal
def add_meal(calorie_intake_progress_bar, meal_record, mealbox, calseatenbox, hourselect, minuteselect, calorie_intake_counter):
  global iidnumb2 #bring iidnumb2 into subroutine so that the correct one can be used when adding to treeview

  #check time netered are numbers, not letters. Show error if there are any letters
  if hourselect.get().isnumeric() == False or minuteselect.get().isnumeric() == False:
    messagebox.showerror(title="Error", message="Make sure both hours and minutes are numbers")
    return None
        
  if calseatenbox.get() == "": #check calories box is not empty
    messagebox.showerror(title="Error", message="Please enter calories")
    return None #if box is empty, show error

  if calseatenbox.get().isnumeric(): #check if calories eaten is a number
    meal_record.insert(parent="", index="end", iid = iidnumb2, text="parent", values=(mealbox.get(), hourselect.get() + ":" + minuteselect.get(), calseatenbox.get())) #insert meal into treeview
    iidnumb2 = iidnumb2 + 1 #updte iid so future items can be added to treeview

    time_eaten = hourselect.get() + ":" + minuteselect.get() #add hour and minuted comboboxes to make time
    todays_date = datetime.datetime.now()
    today_formatted_as_string = todays_date.strftime("%Y-%m-%d") #calculate todays date using datetime module
    with database_connection: #make connection to database
      sql_statement = "INSERT INTO TblMeals (UserID, Mealdesc, Dateeaten, Timeeaten, Calories) VALUES (%s, '%s', '%s', '%s', %s)" % (user_logged_in.get_id(), mealbox.get(), today_formatted_as_string, time_eaten, calseatenbox.get()) #insert meal into TblMeals
      database_cursor.execute(sql_statement) #executes the query
      database_connection.commit() #commits the changes to the database
      sql_statement = "SELECT SUM(calories) FROM TblMeals WHERE dateeaten = '%s' AND userID = %s" % (today_formatted_as_string, user_logged_in.get_id()) #select the total calories eaten today
      database_cursor.execute(sql_statement) #executes the query
      total_calories = database_cursor.fetchall() #sets result of query equal to total_calories
      calorie_intake_counter.config(text=total_calories) #add calories to total calorie counter

    #update progress bar
    calorie_intake_progress_bar['value'] = int((int(total_calories[0][0]) / user_logged_in.get_target_intake()) * 100) #update progress abr to be filled in by the percentage of the users calorie target that they have eaten

    #clear boxes
    mealbox.delete(0, END)
    calseatenbox.delete(0, END)

  else:
    messagebox.showerror(title="Error", message="Calories consumed must be a whole number") #make user reenter calories if it is not a number

    #clear calories box as it was entered incorrectly
    calseatenbox.delete(0, END)
        

def find_meal_page():
  find_meal_window = Tk() #create find_meal_window
  find_meal_window.title("User ID: " + str(user_logged_in.get_id())) #display the users User ID in the window title
  find_meal_window.geometry("252x210") #set window size
  find_meal_window.config(bg="white") #set window backgorund to white


  #make the treeview for meals
  old_meal_record = ttk.Treeview(find_meal_window, height=5)
  old_meal_record["columns"] =  ("#1", "#2", "#3")
  
  old_meal_record.column("#0", anchor=CENTER, stretch=NO, width=0)
  old_meal_record.heading("#0", text = "")
  
  old_meal_record.column("#1", anchor=CENTER, stretch=NO, width=100)
  old_meal_record.heading("#1", text = "Meal")
        
  old_meal_record.column("#2", anchor=E, stretch=NO, width=50)
  old_meal_record.heading("#2", text="Time")
        
  old_meal_record.column("#3", anchor=CENTER, stretch=NO, width=100)
  old_meal_record.heading("#3", text="Calories")
  old_meal_record.grid(row=0, column=0, columnspan=3)

  #create label to show where users can enter a date to find meals eaten on that day
  find_meal_label = Label(find_meal_window, text="Find all meals eaten in a day:", bg="white")
  find_meal_label.grid(row=1, column=0, columnspan=3)

  day_label = Label(find_meal_window, text="Day", bg="white") #add label to show where to enter day
  day_label.grid(row=2, column=0)
  month_label = Label(find_meal_window, text="Month", bg="white") #add label to show where to enter month
  month_label.grid(row=2, column=1)
  year_label = Label(find_meal_window, text="year", bg="white") #add label to show where to enter year
  year_label.grid(row=2, column=2)
        
  find_meal_day = Entry(find_meal_window, width = 5) #make entry box for day
  find_meal_day.grid(row=3, column=0)

  find_meal_month = Entry(find_meal_window, width = 5) #make entry box for month
  find_meal_month.grid(row=3, column=1)

  find_meal_year = Entry(find_meal_window, width = 5) #make entry box for year
  find_meal_year.grid(row=3, column=2)

  find_meal_button = Button(find_meal_window, text="Search", command=lambda: find_meal(old_meal_record, find_meal_day, find_meal_month, find_meal_year)) #create buton to find meals from date entered by user
  find_meal_button.grid(row=4, column=1)

def find_meal(old_meal_record, find_meal_day, find_meal_month, find_meal_year):
  global iidnumb4 #import iidnumb4 so it can be user to add to treeview

  #set month and day equal to those entered by the user
  month = find_meal_month.get()
  day = find_meal_day.get()
        
  if len(day) == 1:
    day = "0" + day #adds 0 to start of day if only 1 digit is entered so that it can be found in database
          
  if len(month) == 1:
    month = "0" + month #adds 0 to start of month if only 1 digit is entered so that it can be found in database
          
  if check_date_is_real(day, month, find_meal_year.get()): #check date entered is a real date
    date = str(find_meal_year.get() + "-" + month + "-" + day) #combine values entered into 1 date string, so that it can be used to search the database

    with database_connection: #create connection to database
      sql_statement = "SELECT * FROM TblMeals WHERE UserID = %s AND Dateeaten = '%s'" % (user_logged_in.get_id(), date) #select all data from TblUsers where userID and date match those entered
      database_cursor.execute(sql_statement) #executes query
      matching_meals = database_cursor.fetchall() #sets results of query as matching_exercises variable
          
    if len(matching_meals) == 0: #checks if there are any reults at all, and returns error box if there are none
      messagebox.showerror(title="Error", message="No meals found on this date")
    else:
      #sort reulsts by sets before displaying
      matching_meals = sort(matching_meals, 4)
      matching_meals.reverse() #reverse order of matching exercises so exercises with most sets appear at the top
      for x in range (len(matching_meals)): #create for loop so that all exercises are added to treeview
        old_meal_record.insert(parent="", index="end", iid = iidnumb4, text="parent", values=(matching_meals[x][2], matching_meals[x][4], matching_meals[x][5])) #insert exercises performed today into treeview
        iidnumb4 = iidnumb4 + 1 #update iid number so things can be added to treeview in future

  else:
    messagebox.showerror(title="Error", message="Please enter a valid date") #if date is not real, tell user to enter a valid date
        

#give option to add workout
def enter_workout(workout_record, exercise_box, sets_box, reps_box, weight_box, comments_box):
  global iidnumb #import iidnumn so the correct iid can be used to insert data into treeview

  #make sure an exercise name has been entered
  if exercise_box.get() == "":
    messagebox.showerror(title="Error", message="Enter exercise name")
    return None #if no exercise name is entered, end subroutine

  #make sure weight has been entered
  if weight_box.get() == "":
    messagebox.showerror(title="Error", message="Enter weight")
    return None #if no weight is entered, end subroutine

  #check sets box is not empty
  if sets_box.get() == "":
    messagebox.showerror(title="Error", message="Enter sets performed")
    return None #if no sets are entered, end subroutine

  #check reps box is not empty
  if reps_box.get() == "":
    messagebox.showerror(title="Error", message="Enter reps performed")
    return None #if no reps are entered, end subroutine
        
  if sets_box.get().isnumeric() and reps_box.get().isnumeric(): #check sets and reps entered by user are numeric values
        
    todays_date = datetime.datetime.now() #calculate todays date using datetime module
    today_formatted_as_string = todays_date.strftime("%Y-%m-%d") #calculate todays date using datetime module
        
    workout_record.insert(parent="", index="end", iid = iidnumb, text="parent", values=(exercise_box.get(), sets_box.get(), reps_box.get(), weight_box.get(), comments_box.get())) #insert data into treeview
    iidnumb = iidnumb + 1 #add 1 to iidnumb so that data can be added to next slot in future

    #add information to TblWorkout in database
    with database_connection: #make connection to database
      sql_statement = "INSERT INTO TblWorkout (UserID, date, exercise, sets, reps, weight, comments) VALUES (%s, '%s', '%s', %s, %s, '%s', '%s')" % (user_logged_in.get_id(), today_formatted_as_string, exercise_box.get(), sets_box.get(), reps_box.get(), weight_box.get(), comments_box.get()) #insert workout into TblWorkout
      database_cursor.execute(sql_statement) #executes the query
      database_connection.commit() #commits the changes to the database
        
    #clear entry boxes
    exercise_box.delete(0, END)
    sets_box.delete(0, END)
    reps_box.delete(0, END)
    weight_box.delete(0, END)
    comments_box.delete(0, END)

  else:
    messagebox.showerror(title="Error", message="Make sure sets and reps are numbers!") #show error box is sets and reps entered by user are non numeric


#find a wokrout from a date entered  by the user
def find_workout(old_workout_record, find_workout_day, find_workout_month, find_workout_year):
  global iidnumb3 #import iidnumb3 so it can be user to add to treeview

  #set month and day variables equal to those entered by the user
  month = find_workout_month.get()
  day = find_workout_day.get()
        
  if len(day) == 1:
    day = "0" + day #adds 0 to start of day if only 1 digit is entered so that it will match the dates in the database, which all have 2 digit months and days
          
  if len(month) == 1:
    month = "0" + month #adds 0 to start of month if only 1 digit is entered so that it will match the dates in the database, which all have 2 digit months and days
          
  if check_date_is_real(day, month, find_workout_year.get()): #check date entered is a real date
    date = str(find_workout_year.get() + "-" + month + "-" + day) #combine values entered into 1 date string, so that it can be used to search the database

    with database_connection: #create connection to database
      sql_statement = "SELECT * FROM TblWorkout WHERE userID = %s AND date = '%s'" % (user_logged_in.get_id(), date) #select all data from TblUsers where userID and date match those entered
      database_cursor.execute(sql_statement) #executes query
      matching_exercises = database_cursor.fetchall() #sets results of query as matching_exercises variable
          
    if len(matching_exercises) == 0: #checks if there are any reults at all, and returns error box if there are none
      messagebox.showerror(title="Error", message="No workout found on this date")
    else:
      #sort reulsts by sets before displaying
      matching_exercises = sort(matching_exercises, 4)
      matching_exercises.reverse() #reverse order of matching exercise so exercises with most sets appear at the top
      for x in range (len(matching_exercises)): #create for loop so that all exercises are added to treeview
        old_workout_record.insert(parent="", index="end", iid = iidnumb3, text="parent", values=(matching_exercises[x][3], matching_exercises[x][4], matching_exercises[x][5], matching_exercises[x][6], matching_exercises[x][7])) #insert exercises performed today into treeview
        iidnumb3 = iidnumb3 + 1 #update iid number so things can be added to treeview in future

  else:
    messagebox.showerror(title="Error", message="Please enter a valid date") #if date is not real, tell user to enter a valid date


#Draw bar chart to show calorie intake
def bar_chart(bar_chart_frame):
  today = datetime.datetime.now() #set "today" variable equal to todays date
        
  #create label to show that line represents calorie maintenance level
  maintenance_label = Label(bar_chart_frame, text = """



maintenance
calories""", bg="white") #create label for central maintenacne calories axis on bar chart
  maintenance_label.grid(row=0, column=0)

  find_meal_button = Button(bar_chart_frame, text = """search
meals""", command=lambda: find_meal_page()) #create button to open find meals window
  find_meal_button.grid(row=1, column=0)
        
  bar_chart_canvas = Canvas(bar_chart_frame, width=270, height=203, bg="white") #create canvas to draw bar chart onto
  bar_chart_canvas.grid(row=0, column=1, rowspan=2) #place bar chart on screen

  

  bar_width = 45 #set width of bars
  x_position = 17 #set x position, where the first bar will be placed

  for x in range (1, 6): #make loop repeat 5 times, so it covers the last 5 days
    day = today - timedelta(days=x)#set day variable equal to todays date minus x days
    day = str(day.strftime("%Y-%m-%d")) #make the date a string, I have formatted the daye backwards (yy-mm-dd) as this is how it appears in the database
    with database_connection: #make connection to database
      sql_statement = "SELECT SUM(calories) FROM TblMeals WHERE dateeaten = '%s' AND userID = %s" % (day, user_logged_in.get_id()) #this sql statement finds the total calories eaten on day x
      database_cursor.execute(sql_statement) #execute sql statement
      result = database_cursor.fetchall() #set result of query equal to "result" variable
          
    if result[0][0] == None: #check if no calories have been recorded on this day
      bar_chart_canvas.create_text(x_position, 87, text= """              No meals
              recorded""", fill = "black", font = "Helvetica 6") #if no meals are foud in the database, put text in the slot saying no meals have been recorded on this day
            
    elif int(str(result[0][0])) >= user_logged_in.get_target_intake(): #check if result is bigger than maintenacne calories
      bar_chart_canvas.create_rectangle(x_position, 100, x_position + bar_width, 100 - ((int(result[0][0]) - user_logged_in.get_target_intake()) / 10), fill = "grey") #create bar above axis showing calorie surplus
      bar_chart_canvas.create_text(x_position, 108, text= "              +" + str(int(result[0][0]) - user_logged_in.get_target_intake()) + "kcal", fill = "black", font = "Helvetica 6") #place text below the bar to show the exact calorie surplus
          
    else:
      bar_chart_canvas.create_rectangle(x_position, 100 - ((int(result[0][0]) - user_logged_in.get_target_intake()) / 10), x_position + bar_width, 100, fill = "grey") #if they have not eaten more than their maintenacne calories, put bar below axis to show calorie deficit
      bar_chart_canvas.create_text(x_position, 92, text= "              -" + str(user_logged_in.get_target_intake() - int(result[0][0])) + "kcal", fill = "black", font = "Helvetica 6") #place text above bar to show the exact calorie deficit

    x_position += 50 #add 55 to x position so bars are well spaced out

  bar_chart_canvas.create_line(0, 100, 270, 100, width = 3) #create axis for 0/maintenance calories








#sort workouts found from query by sets performed from highest to lowest
def sort(data, sets):
    if len(data) <= 1: #check array is larger than 1 index, if it is no sorting has to be done
      return data #return list if there is 1 or less items in it
    
    midpoint = len(data) // 2 #create midpoint to split array in 2
    left_array = data[:midpoint] #create 2 different arrays from left and right halves of list
    right_array = data[midpoint:]

    #merge sort both the left and right arrays
    left_sorted = sort(left_array, sets)
    right_sorted = sort(right_array, sets)

    return merge(left_sorted, right_sorted, sets) #return the merged version of the 2 arrays

#this subroutine carries out the merge part of a merge sort
def merge(left_array, right_array, sets):
  result = [] #create empty array for result of merge
  left_index, right_index = 0, 0 #create values for the index in each list that is being compared

  while left_index < len(left_array) and right_index < len(right_array): #check indexes are not larger than their lists, if they are the whole list has been compared
          
    #check which number is larger
    if left_array[left_index][sets] <= right_array[right_index][sets]:
      result.append(left_array[left_index]) #add left number to result array first if it is smaller
      left_index = left_index + 1 #add 1 to left index so that the next number will be comapred
    else:
      result.append(right_array[right_index]) #add right number to result array first if it is smaller
      right_index = right_index + 1 #add 1 to right index so that the next number will be comapred

  #add the last item in either list to result list
  result += left_array[left_index:]
  result += right_array[right_index:]

  return result #return merged list




login() #call login page
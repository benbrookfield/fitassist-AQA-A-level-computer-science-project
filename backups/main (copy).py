from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import re

user_logged_in = -1

class User:
  def __init__(self, firstname, lastname, weight, height, date_of_birth, password):
    self.__firstname = firstname
    self.__lastname = lastname
    self.__weight = weight
    self.__height = height
    self.__date_of_birth = date_of_birth
    self.__password = password

  def get_firstname(self):
    return self.__firstname

  def get_lastname(self):
    return self.__lastname

  def get_weight(self):
    return self.__weight

  def get_height(self):
    return self.__height

  def get_date_of_birth(self):
    return self.__date_of_birth

  def get_password(self):
    return self.__password

  def set_firstname(self, firstname):
    self.__firstname = firstname

  def set_lastname(self, lastname):
    self.__lastname = lastname

  def set_weight(self, weight):
    self.__weight = weight

  def set_height(self, height):
    self.__height = height

  def set_date_of_birth(self, date_of_birth):
    self.__date_of_birth = date_of_birth

  def set_password(self, password):
    self.__password = password 

class Meal:
  def __init__(self, meal, calories):
    self.__meal = meal
    self.__calories = calories

  def get_meal(self):
    return self.__meal

  def get_calories(self):
    return self.__calories

  def set_meal(self, meal):
    self.__meal = meal

  def set_calories(self, calories):
    self.__calories = calories

class Exercise:
  def __init__(self, description, exerciselvl, time, calsburned):
    self.__description = description
    self.__exerciselvl = exerciselvl
    self.__time = time
    self.__calsburned = calsburned

  def get_description(self):
    return self.__meal

  def get_exerciselvl(self):
    return self.__exerciselvl

  def get_exerciselvl(self):
    return self.__time

  def get_calsburned(self):
    return self.__calsburned

  def set_description(self, description):
    self.__description = description

database_connection = sqlite3.connect('fitness_assistant.db')
database_cursor = database_connection.cursor()

iidnumb = 0
iidnumb2 = 0

calories_consumed = 0

def login():
  login_window = Tk()
  login_window.title("Fitness assistant")
  login_window.geometry("300x100")

  title_label = Label(login_window, text="Login", bg="white")
  title_label.grid(row=0, column=0, padx=30, columnspan=2)
        
  user_label = Label(login_window, text="User ID:", bg="white")
  user_label.grid(row=1, column=0, padx=30)
  user_entry = Entry(login_window, width=15)
  user_entry.grid(row=1, column=1)

  password_label = Label(login_window, text="Password:", bg="white", )
  password_label.grid(row=2, column=0, padx=30)
  password_entry = Entry(login_window, width=15, show="*")
  password_entry.grid(row=2, column=1)
        
  submit_button = Button(login_window, text="Submit", command=lambda: login_submit(login_window, user_entry.get(), password_entry.get()))
  submit_button.grid(row=3, column=1)

  new_user_button = Button(login_window, text="New User", command=lambda: newuser_submit())
  new_user_button.grid(row=3, column=0)

  login_window.mainloop()

def newuser_submit():
  newuser_window = Tk()
  newuser_window.title("Fitness assistant")
  newuser_window.geometry("300x180")

  newuser_label = Label(newuser_window, text="New User", bg="white")
  newuser_label.grid(row=0, column=0, columnspan=2, padx=50)

  #create password
  password_label = Label(newuser_window, text="New Password:", bg="white")
  password_label.grid(row=1, column=0, padx=30)
  password_entry = Entry(newuser_window, width=15)
  password_entry.grid(row=1, column=1)

  #enter first name
  firstname_label = Label(newuser_window, text="First Name:", bg="white")
  firstname_label.grid(row=2, column=0, padx=30)
  firstname_entry = Entry(newuser_window, width=15)
  firstname_entry.grid(row=2, column=1)

  #enter last name
  lastname_label = Label(newuser_window, text="Last Name:", bg="white")
  lastname_label.grid(row=3, column=0, padx=30)
  lastname_entry = Entry(newuser_window, width=15)
  lastname_entry.grid(row=3, column=1)

  #enter date of birth
  dob_label = Label(newuser_window, text="Date of Birth:", bg="white")
  dob_label.grid(row=4, column=0, padx=30)
  dob_entry = Entry(newuser_window, width=15)
  dob_entry.grid(row=4, column=1)

  #enter height
  height_label = Label(newuser_window, text="Height (cm):", bg="white")
  height_label.grid(row=5, column=0, padx=30)
  height_entry = Entry(newuser_window, width=15)
  height_entry.grid(row=5, column=1)

  #enter weight
  weight_label = Label(newuser_window, text="weight (kg):", bg="white")
  weight_label.grid(row=6, column=0, padx=30)
  weight_entry = Entry(newuser_window, width=15)
  weight_entry.grid(row=6, column=1)

  submitaccount_button = Button(newuser_window, text="Submit", command=lambda:createaccount (newuser_window, password_entry.get(), firstname_entry.get(), lastname_entry.get(), dob_entry.get(), height_entry.get(), weight_entry.get()))
  submitaccount_button.grid(row=7,column=0, columnspan=2)

def createaccount(newuser_window, password, firstname, lastname, dob, height, weight):
  illegal_character_found = False
  for each_character in weight:
    if (each_character.isdigit() == False) and (each_character != "."):
      print(each_character)
      print("illegal")
      illegal_character_found = True
  if password == "":
    messagebox.showerror(title="Error", message="Please enter a password")
  elif firstname == "":
    messagebox.showerror(title="Error", message="Please enter your first name")
  elif lastname == "":
    messagebox.showerror(title="Error", message="Please enter your last name")
  elif dob == "":
    messagebox.showerror(title="Error", message="Please enter your date of birth")
  elif height == "":
    messagebox.showerror(title="Error", message="Please enter your height")
  elif height.isdigit() == False:
    messagebox.showerror(title="Error", message="Please enter a valid height")
  elif weight == "":
    messagebox.showerror(title="Error", message="Please enter your weight")
  elif illegal_character_found == True:
    messagebox.showerror(title="Error", message="Please enter a valid weight")
  else:
    with database_connection:
      sql_statement = "INSERT INTO TblUsers (First_Name, Last_Name, Weight, Height, Date_Of_Birth, Password) VALUES ('%s', '%s', %s, %s, '%s', '%s')" % (firstname, lastname, weight, height, dob, password)
      database_cursor.execute(sql_statement)
      database_connection.commit()
    nutrition_page()

def login_submit(login_window, userID, password):
  global user_logged_in
  print(userID, password)
  if userID == "":
    messagebox.showerror(title="Error", message="Please enter a user ID")
  elif password == "":
    messagebox.showerror(title="Error", message="Please enter a password")
  else:
    with database_connection:
      sql_statement = "SELECT * FROM TblUsers WHERE User_ID = '%s' AND Password = '%s'" % (userID, password)
      database_cursor.execute(sql_statement)
      matching_users = database_cursor.fetchall()
    if len(matching_users) == 1:
      user_logged_in = userID
      login_window.destroy()
      nutrition_page()
    else:
      messagebox.showerror(title="Error", message="Username or password is incorrect")


#    
#    
  
        
def nutrition_page():
  #make window
  window = Tk()
  window.title("Fitness assistant")
  window.geometry("365x649")

  #add notebook to make different tabs
  notebook = ttk.Notebook(window)
  notebook.grid(column=0, row=0)
  #nutrition tab
  nutrition = Frame(notebook, width=1280, height=705, bg="white")
  nutrition.pack(fill="both", expand=1)
  #weight tab
  weight = Frame(notebook, width=1280, height=705, bg="white")
  weight.pack(expand=1)
  #resistance training tab
  strength_training = Frame(notebook, width=1280, height=705, bg="white")
  strength_training.pack(expand=1)

  #add tabs to top of screen
  notebook.add(nutrition, text="Nutrition Tracker")
  notebook.add(weight, text="Weight Tracker")
  notebook.add(strength_training, text="Resistance Training")

  #make calories consumed title
  calorie_intake = Label(nutrition, height = 1, width=20, text="Calories Consumed:", bg="white", font=("Imperial", 20))
  calorie_intake.grid(row=0, column=0, pady=20)
  calorie_intake_counter = Label(nutrition, height = 1, width=10, text=calories_consumed, bg="white", font=("Imperial", 30))
  #make  calories consumed progress bar
  calorie_intake_counter.grid(row=1, column=0)
  calorie_intake_progress_bar = ttk.Progressbar(nutrition, orient=HORIZONTAL, length = 250, mode="determinate")
  calorie_intake_progress_bar.grid(row=3, column=0)

  target_label = Label(nutrition, height = 1, width= 20, text="Target: xxx", bg="white", font=("Imperial", 20))
  target_label.grid(row=4, column=0)

  #make the treeview for calories consumed
  meal_record = ttk.Treeview(nutrition, height=5)
  meal_record["columns"] =  ("#1", "#2", "#3", "#4")
  meal_record.column("#0", anchor=CENTER, stretch=NO, width=0)
  meal_record.heading("#0", text = "")
  meal_record.column("#1", anchor=CENTER, stretch=NO, width=100)
  meal_record.heading("#1", text = "Meal")
  meal_record.column("#2", anchor=E, stretch=NO, width=50)
  meal_record.column("#3", anchor=W, stretch=NO, width=50)
  meal_record.heading("#2", text="Time")
  meal_record.column("#4", anchor=CENTER, stretch=NO, width=100)
  meal_record.heading("#4", text="Calories")
  meal_record.grid(row=5, column=0, pady=10)

  addmealf = Frame(nutrition, bg="white")
  addmealf.grid(row=6, column=0)

  addm = Label(addmealf, text="Add a Meal", bg="white")
  addm.grid(row=0, column=0, columnspan=4)

  addmeal = Label(addmealf, text="Meal", bg="white")
  addmeal.grid(row=1, column=0, padx=30)
  mealbox = Entry(addmealf, width=15)
  mealbox.grid(row=2, column=0)

  addtime = Label(addmealf, text="Time", bg="white")
  addtime.grid(row=1, column=1, padx=38, columnspan=2)

  minutes = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
  hours = ["00   :", "01   :", "02   :", "03   :", "04   :", "05   :", "06   :", "07   :", "08   :", "09   :", "10   :", "11   :", "12   :", "13   :", "14   :", "15   :", "16   :", "17   :", "18   :", "19   :", "20   :", "21   :", "22   :", "23   :"]

  hourselect = ttk.Combobox(addmealf, values=hours, width=3)
  hourselect.current(0)
  hourselect.grid(row=2, column=1)
  minuteselect = ttk.Combobox(addmealf, values=minutes, width=3)
  minuteselect.current(0)
  minuteselect.grid(row=2, column=2)

  addcals = Label(addmealf, text="Calories", bg="white")
  addcals.grid(row=1, column=3, padx=30)
  calseatenbox = Entry(addmealf, width=15)
  calseatenbox.grid(row=2, column=3)

  add_data = Button(addmealf, text="Add", command=lambda: add_meal(meal_record, mealbox, calseatenbox, hourselect, minuteselect))
  add_data.grid(row=3, column=1, columnspan=2, pady=5)

  ''' 
  net_calorie_intake = Label(nutrition, height = 1, width=27, text="Net Calorie Intake:", bg="white", font=("Imperial", 30))
  net_calorie_intake.grid(row=0, column=3, pady=20)
  net_calorie_intake_counter = Label(nutrition, height = 1, width=1, text="0", bg="white", font=("Imperial", 50))
  net_calorie_intake_counter.grid(row=1, column=3, rowspan=2)
  net_calorie_intake_progress_bar = ttk.Progressbar(nutrition, orient=HORIZONTAL, length = 350, mode="determinate")
  net_calorie_intake_progress_bar.grid(row=3, column=3)

  
  calories_burned = Label(nutrition, height = 1, width=20, text="Calories Burned:", bg="white", font=("Imperial", 20))
  calories_burned.grid(row=0, column=4, pady=20)
  calories_burned_counter = Label(nutrition, height = 1, width=10, text="0", bg="white", font=("Imperial", 30))
  calories_burned_counter.grid(row=1, column=4)
  calories_burned_progress_bar = ttk.Progressbar(nutrition, orient=HORIZONTAL, length = 250, mode="determinate")
  calories_burned_progress_bar.grid(row=3, column=4)

  #make the treeview for calories burned
  cardio_record = ttk.Treeview(nutrition, height=5)
  cardio_record["columns"] =  ("#1", "#2", "#3", "#4")
  cardio_record.column("#0", anchor=CENTER, stretch=NO, width=0)
  cardio_record.heading("#0", text="")
  cardio_record.column("#1", anchor=CENTER, stretch=NO, width=100)
  cardio_record.heading("#1", text="Description")
  cardio_record.column("#2", anchor=CENTER, stretch=NO, width=69)
  cardio_record.heading("#2", text = "Exercise lvl")
  cardio_record.column("#3", anchor=CENTER, stretch=NO, width=71)
  cardio_record.heading("#3", text="Time (mins)")
  cardio_record.column("#4", anchor=CENTER, stretch=NO, width=58)
  cardio_record.heading("#4", text="Calories")
  cardio_record.grid(row=4, column=4, pady=10)

  addexercisef = Frame(nutrition, bg="white")
  addexercisef.grid(row=5, column=4)

  addm = Label(addexercisef, text="Add an Exercise Session", bg="white")
  addm.grid(row=0, column=0, columnspan=4)

  adddesc = Label(addexercisef, text="Description", bg="white")
  adddesc.grid(row=1, column=0, padx=22)
  descbox = Entry(addexercisef, width=15)
  descbox.grid(row=2, column=0)

  addlvl = Label(addexercisef, text="Exercise lvl", bg="white")
  addlvl.grid(row=1, column=1, padx=22)
  lvlbox = Entry(addexercisef, width=15)
  lvlbox.grid(row=2, column=1)

  addtime = Label(addexercisef, text="Time", bg="white")
  addtime.grid(row=1, column=2)
  timeselect = Entry(addexercisef, width=15)
  timeselect.grid(row=2, column=2)

  add_data2 = Button(addexercisef, text="Add", command=add_exercise)
  add_data2.grid(row=3, column=0, columnspan=4)
  '''
  window.mainloop()

#give the option to add a meal
def add_meal(meal_record, mealbox, calseatenbox, hourselect, minuteselect):
  global UserID
  global calories_consumed
  global iidnumb2
  if calseatenbox.get().isdigit() == False:
    messagebox.showerror(title="Error", message="Calories consumed must be a whole number")
  else:
    meal_record.insert(parent="", index="end", iid = iidnumb2, text="parent", values=(mealbox.get(), hourselect.get(), minuteselect.get(), calseatenbox.get()))
  iidnumb2 = iidnumb2 + 1
  calories_consumed = calories_consumed + int(calseatenbox.get())
  #clear boxes
  mealbox.delete(0, END)
  calseatenbox.delete(0, END)

  with database_connection:
    sql_statement = "INSERT INTO TblMeals (UserID, MealID, Mealdesc, Dateeaten, Timeeaten, Calories) VALUES (%s, %s, '%s', '%s', '%s', %s)" % ()
    database_cursor.execute(sql_statement)
    database_connection.commit()  
 

#give option to add exercise session
def add_exercise():
  global iidnumb
  cardio_record.insert(parent="", index="end", iid = iidnumb, text="parent", values=(descbox.get(), lvlbox.get(), timeselect.get()))
  iidnumb = iidnumb + 1

  #clear boxes
  descbox.delete(0, END)
  lvlbox.delete(0, END)
  minuteselect.delete(0, END) 

login()
#nutrition_page()
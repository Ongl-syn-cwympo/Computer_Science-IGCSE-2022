# ~ Computer Science EXAM Code ~
# Pre-release material - 0478/21/22 MAY/JUNE
# Python code 
# 2022 Exam code ~ Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo


# Within this piece of code, I use .append quite frequently - This is a short desctiprion.
# Append in Pyhton takes a single argument, which is the item you want to add to the list.

# ~ TASK 1 ~
from datetime import datetime, date 

# Variables and declarations 
Full_name = list()
Date_of_Joining = list()
Sponsor = list()
Fee_Paid = list()
Volunter_Choice = list()
Volunter_Area = list()
VolunterYes = bool
VolunterNo = bool
Messages = list()
People_Sponsored = list()

count = 0

while input("Would you like to add a user?") == "Yes": # No break with th while loop, so that more people can be asked and more data can be stored
  
  # First Name ~ Entered by user
  print("Please enter your first name")
  F_name = input()
  
  # Second Name ~ Entered by user
  print("Please enter your second name")
  S_name = input()
  
  # Combines both the first and second name 
  Full_name.append(F_name + " " + S_name)
  
  # True or false ~ Volunrer = yes or no
  print("Would you like to be a volunter?")
  Volunter_Choice.append(input("""Choose 1: To be a volunter Choose  (Type in True, 1 or Yes) 2: To not be a volunter (Type in False, 2 or No)"""))
  
  # Stating what is False and True ~ To do with while loops
  VolunterYes = True 
  VolunterNo = False
  
  if Volunter_Choice[count] == "True" or Volunter_Choice[count] == "1" or Volunter_Choice[count] == "Yes":
     print("Nice choice")
     
  
  else:
    print("Bad choice ~ Leave at once")
    sys.exit(exit_code) # Terminates the program, due to error/invalid enrty code
     
    

  # Selection of area for user ~ 3 options 
  print("What area would you like to be in?")
  Volunter_Area.append(int(input("""Choose 1: Pier enterance gate Choose 2: Gift shop Choose 3: Painting and decorating""")))
  
  while Volunter_Area[count]<1 or Volunter_Area[count]>3:
      Volunter_Area[count] = ("Enter 1,2 or 3 ~ Any other numb is invalid")
      if Volunter_Area[count] == 1:
        print("You have chosen Pier enterance gate")
      if Volunter_Area[count] == 2:
        print("You have chosen Gift shop")
      if Volunter_Area[count] == 3:
        print("You have chosen Painting and decorating")
      else:
        print("Invalid ~ Unable to execute")
        sys.exit(exit_code) # Terminates the program, due to error/invalid enrty code
      break
  
  # User enters date ~ Program outputs inputed value in the from of yy/mm/dd 
  # Program uses real time ~ If date entered is over or under 1 year, it outputs you as expired
  print("Enter the date you joined")
  date_entry = input()
  Year, Month, Day = map(int, date_entry.split("/"))
  Date_of_Joining.append(datetime(Year, Month, Day,0,0))
  print Date_of_Joining[count]
      
  Time_Since_Joined = datetime.now()-Date_of_Joining[count]
  if Time_Since_Joined.total_seconds()/(365.25*24*60*60) >= 1:
    print("You have expired :(")
      
# ~ Explination of line 71:
# date_entry.split("/") - splits the string date_entry into a list at every "/", so 2021/03/21 gets turned into a list with elements ["2021", "03", "21"]
# map(int, date_entry.split("/")) - the map() function will loop through every element in the list provided as the second parameter and run the function provided in the first parameter (https://www.geeksforgeeks.org/python-map-function/). In this case the "int" is a builtin function which will convert every element into an integer from the string. So in the end ["2021", "03", "21"] will turn into [2021, 03, 21] (only the types of the values changed from string to int).
# Year, Month, Day = map(int, date_entry.split("/")) - finally, it will asign the first element of the array provided by the map() function into the Year variable, the second into the Month variable and the third into the Day variable. So you will end up with the Year holding the value 2021, Month with 3 and Day with 21.

# ~ Explination of line 75:
# datetime.now() - the current date and time in a single object
# datetime.now()-Date_of_Joining[count] - get the difference between the dates of now and the date that was gotten from the user before. The [count] part is there because Date_of_Joining is an array, meaning it has multiple elements and by adding [count] you specify what element in the array you want to use. The variable count should therefore represent the index of the current user.
# Time_Since_Joined = datetime.now()-Date_of_Joining[count] - store the difference between these two dates into a variable. In this case it does not have to be an array since this value does not need to be
# stored for every user but will be used just this once.

# ~ Explination of line 76 (where the numbers are multiplied):
# Time_Since_Joined.total_seconds() - this will give back the difference between the two dates calculated on line 7 in seconds
# Time_Since_Joined.total_seconds()/(365.25*24*60*60) - the difference in seconds divided by the amount of seconds in a year (365.25*24*60*60 = 31557600 aka how many seconds are in a year)
# if  Time_Since_Joined.total_seconds()/(365.25*24*60*60) >= 1: - if the difference in two dates is greater than 1 year, then do the thing inside this if statement 

# - What's a parameter? -
# In computer programming, a parameter or a formal argument is a special kind of variable used in a subroutine to refer to one of the pieces of data provided as input to the subroutine.

      
  # Fee section
  print("Did you pay the 75$ fee? Yes or No")
  
  if input() == "Yes":
    print("Good!")
    Fee_Paid.append(True)
    
  else:
    print("Very bad! / Invalid entry")
    Fee_Paid.append(False)
   
# ~ TASK 2 ~
while input("Do you want to see the info?") == "Yes": # No break with th while loop, so that more people can be asked and more data can be stored
  
  # Membership data ~ Outputting stats
  print("What stats of the members would you like to look at?")
  print("1. Members who have been chosen to be volunters")
  print("2. Members who want to work at the pier")
  print("3. Members who want to work at the gift shop")
  print("4. Members who want to work at the decorating area")
  print("5. Members whose membership has expired")
  print("6. Members who have not not paid the fee")
  
  # A series of if statments for the users selection ~ Displays the data for chosen num
  selection = int(input())
  if selection == 1:
    for i in range(0,len(Volunter_Choice)):
      if Volunter_Choice[i] == "True" or Volunter_Choice[i] == "1" or Volunter_Choice[i] == "Yes":
        print Full_name[i] 
        
  if selection == 2:
    for i in range(0,len(Volunter_Area)):
      if Volunter_Area[i] == 1:
        print Full_name[i] 
        
  if selection == 3:
    for i in range(0,len(Volunter_Area)):
      if Volunter_Area[i] == 2:
        print Full_name[i] 
        
  if selection == 4:
    for i in range(0,len(Volunter_Area)):
      if Volunter_Area[i] == 3:
        print Full_name[i] 
        
  if selection == 5:
    for i in range(0,len(Date_of_Joining)):
      Time_Since_Joined = datetime.now()-Date_of_Joining[i]
      if Time_Since_Joined.total_seconds()/(365.25*24*60*60) >= 1:
        print Full_name[i] 
        
  if selection == 6:
    for i in range(0,len(Fee_Paid)):
      if Fee_Paid[i] == False:
        print Full_name[i] 
      
# Extended task for TASK 1 ~ Wooden plank sponsorship 
# TASK 3 ~ Output user's who sponsored and their short message on their brass plaque & withdraws the 200$
while input("Would you like to sponsor a wooden plank?") == "Yes": # No break with th while loop, so that more people can be asked and more data can be stored
  print("Re-Enter your name")
  People_Sponsored.append(input())
  print("What short message would you like on your plaque?")
  Message = input()
  if input("Confirm this message" + Message) == "Yes":
    Messages.append(Message)
    print People_Sponsored[-1] + ":" + Message # -1 means the last element 
    print("200$ has been withrawn from your bank account for the sponsor, we thank you <3")
  else:
    print("Have a nice day <3")
    
# </summary of Task 1> #

# - System that enables the people to become a member of Friends of Seaview Per -
# Allows user to enter first & second name, question about becoming a volunteer and identifying what area to work in  
# The date of joining and whether or not they have paid the fee of 75$

# </summary of Task 2> #

# - System that uses the membership data -
# A list of first and last names of members are outputed in any of the categories:
# Members who have chosen to work as volunteers
# Volunteers who would like to work at the Pier enterance
# Volunteers who would like to work at the gift shop
# Volunteers who would like to work at the painting and decorating
# Members whose membership has expired
# Members who have not paid the 75$ fee

# </summary of Task 3> #

# - Sponsoring a wooden plank - 
# Names of indaviduals and their short messages to be writen on their plaque
# An output that displays the name and message + A confimation message
# The data is stored and sponsor is charged 200$

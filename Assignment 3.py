import datetime  
print('''Assignment 3. Write Python script to display 
      a. Current date and time, 
      b. Current year. 
      c. Month of year. 
      d. Week mumber of the year. 
      e. Weekend of the week, 
      f. Day of year, 
      g. Day of the month  
      h. Day of the week. ''') 
print("\n")
print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of the year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Which day of the week: ", datetime.date.today().strftime("%w"))
print("Day of the year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of the week: ", datetime.date.today().strftime("%A"))

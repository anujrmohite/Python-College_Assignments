#Write a program that has a class TIME. Enter the time when a user started an online: test and completed the test. 
#Subtract the two-time values and display the duration in which the test was completed. 
#Throw exceptions whenever need arises (like invalid data, or if start time is greater than completion time).

class testDuration:
    startingTimeInHr=0
    StartingTimeInMIn=0
    ###################
    EndingTimeInHr=0
    EndingTimeInMIn=0
    
    def durationCalc(self):
        try:
            startingTimeInHr=int (input("\n*Accepted Time format 00:00 to 24:00*\nPlease Specify Starting Time(Hr):->>>"))
            if(startingTimeInHr > 23 or startingTimeInHr < 00):
                print("Please Specify correct Time format")
                exit(0)
            
        except ValueError:
            print("Please Specify Accepted input only!")
        
        try:
            StartingTimeInMIn = int(input("Please Specify Starting Time(Min):->>>"))
            if(StartingTimeInMIn > 60 or StartingTimeInMIn < 00):
                print("Please Specify Time in Min")
                exit(0)
        except ValueError:
            print("Please Specify Accepted input only!")

        #######################
        #######################
        #######################
        try:
            EndingTimeInHr=int (input("\n`````````\nPlease Specify Ending Time(Hr):->>>"))
            if(EndingTimeInHr > 23 or startingTimeInHr < 00):
                print("Please Specify correct Time format")
                exit(0)
            
        except ValueError:
            print("Please Specify Accepted input only!")
        
        try:
            EndingTimeInMIn = int(input("Please Specify Starting Time(Min):->>>"))
            if(StartingTimeInMIn > 60 or StartingTimeInMIn < 00):
                print("Please Specify Time in Min")
                exit(0)
        except ValueError:
            print("Please Specify Accepted input only!")

    
        StartingTime = startingTimeInHr * 60 + StartingTimeInMIn
        EndingTime = EndingTimeInHr * 60 + EndingTimeInMIn
        if(StartingTime > EndingTime):
            print("Please Specify Correct Ending Time!")
            exit(0)
        worked_h = int((EndingTime - StartingTime)/60)
        worked_m = (EndingTime - StartingTime)%60
        print("Test Duration>>> {0}:{1}".format(worked_h,worked_m))
new =testDuration()
new.durationCalc()
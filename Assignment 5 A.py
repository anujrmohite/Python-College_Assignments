from tkinter import E
import numpy as np
x = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
y = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

print("first matrix Elements:")
x[0,0] = int(input("For 00: "))
x[0,1] = int(input("For 01: "))
x[0,2] = int(input("For 02: "))

x[1,0] = int(input("For 10: "))
x[1,1] = int(input("For 11: "))
x[1,2] = int(input("For 12: "))

x[2,0] = int(input("For 20: "))
x[2,1] = int(input("For 21: "))
x[2,2] = int(input("For 22: "))

print("Second matrix Elements:")
y[0,0] = int(input("For 00: "))
y[0,1] = int(input("For 01: "))
y[0,2] = int(input("For 02: "))

y[1,0] = int(input("For 10: "))
y[1,1] = int(input("For 11: "))
y[1,2] = int(input("For 12: "))

y[2,0] = int(input("For 20: "))
y[2,1] = int(input("For 21: "))
y[2,2] = int(input("For 22: "))

while True: 
    print("\n\n\nChoose Your Options\n")
    print ("1) Addition")
    print("2) Subtraction")
    print("3) Division")
    print("4) Multiplication ")
    print("5) Transpose")
    print("6) Exit")
    print("9) View")
    cho = int(input("Choice: "))
    if(cho == 1):
        print ("Addition: ")
        print (np.add(x,y))
    elif(cho == 2):
        print ("Subtraction: ")
        print (np.subtract(x,y))
    elif(cho == 3):
        print ("Division : ")
        print (np.divide(x,y))
    elif(cho == 4):
        print ("Multiplication")
        print (np.multiply(x,y))
    elif(cho == 5):
        print ("transpose : ")
        print (x.T)
        print(y.T)
    elif(cho == 9):
        print(x)
        print(y)
    elif(cho == 6):
        break;
    else:
        print("Invalid Choice! ")

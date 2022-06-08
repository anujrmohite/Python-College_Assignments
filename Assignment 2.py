class BankAccount():
	def __init__(self, User_Name, AC_NO, AC_Type, balance):
		self.User_Name = User_Name
		self.AC_NO = AC_NO
		self.AC_Type = AC_Type
		self.balance = balance

	def deposite(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance > 0 and self.balance >= amount:
			self.balance -= amount
		else:
			print("Not Enough Balance To Withdraw")

	def showBalance(self):
		print("\
		User_Name : {} \n \
		Account Type : {} \n \
		Account Number : {} \n \
		Balance : {} \n \
		".format(
			self.User_Name,
			self.AC_Type,
			self.AC_NO,
			self.balance
			)
		)

accounts = {}

flag = 0
while flag != 3:
	print("\nWELCOME!\nBanking System Project\nRPPOP Assignment 2\nby MIS: 142103002\n***************\nchoose the right option below:\n\n1.Sign up")
	print("2.Sign in")
	print("3.Exit:)\n\n***************\n")
	flag = int(input("Enter option here-> "))
	if flag == 1:
			AC_NO = int(input("Please Enter 12 digit A/C No : "))
			accounts[AC_NO] = BankAccount(input("User_Name : "),AC_NO,input("AC_Type : "), int(input("Balance : ")))
	elif flag == 2:
		print("1. Deposite")
		print("2. Withdraw")
		print("3. Balance Inquiry")
		print("4. Return;")
		flag = int(input("... "))

		if flag == 1:
			accounts[int(input("AC_Number : "))].deposite(int(input("deposite : ")))
		elif flag == 2:
			accounts[int(input("AC_Number : "))].withdraw(int(input("withdraw : ")))
		elif flag == 3:
			accounts[int(input("AC_Number : "))].showBalance()
			flag = 4
		elif flag == 4:
			pass
		else:
			print("Invalid")

	elif flag != 3:
		print("Invalid")

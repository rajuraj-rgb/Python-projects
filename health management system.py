# Health Management System
def getdate():
           import datetime
           return datetime.datetime.now()
 
print('HEALTH MANAGEMENT SYSTEM')

directory = "/storage/emulated/0/Python app/"

username = input("Enter your name: ")

filepath = directory + username + '_food'
filepath1 = directory + username + '_exercise'

with open(filepath, 'w+') as fp:
	pass
with open(filepath1, 'w+') as fp:
	pass

print("Do you want to log your data or retrieve your data ?")

user_choice = int(input("Press 1 to log your data and 2 to retrieve your data: "))

def log(username):
	print('What you want to log: Exercise or food')
	user_choice1 = int(input('Press 1 for food and 2 for exercise: '))
	if user_choice == 1:
		value = input('Enter exercise name: ')
		with open(filepath, 'a') as op:
			op.write(str([str(getdate())]) + ': ' + value + '\n')
		print('Successfully written')
	elif user_choice == 2:
		value = input('Enter food item: ')
		with open(filepath, 'a') as op:
			op.write(str([str(getdate())]) +  ':' + value + '\n')
		print('Successfully written')

def retrieve(username):
	print('Which file do you want to retrieve ?')
	user_choice2 = int(input('Enter 1 for food list and enter 2 for exercise list: '))
	if user choice == 1:
		with open(filepath) as op:
			for i in op:
				print(i, end = '')
	elif user_choice == 2:
		with open(filepath1) as op:
			for i in op:
				print(i, end = '')
	else:
		print('Invalid input !!')

if user_choice == 1:
	log(username)
elif user_choice == 2:
	retrieve(username)
else:
	print('Invalid input !!')

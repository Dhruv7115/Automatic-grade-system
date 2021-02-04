'''When a student scores 80 and above, award an A+

When A student score from 75 - 79, award an A

When A student scores from  70 – 74 , award an B+

When A student scores from  65 – 69 , award an B

When A student scores from  60 – 64 , award an C+

When A student scores from  55 – 59 , award an C

When A student scores from  50 – 54 , award an D+

When A student scores from  40 – 49 , award an D

When A student scores below 40, award an F'''

print('''WELCOME TO DHRUV'S AUTOMATIC GRADE SYSTEM''')
print('''1. Enter 1 to start the program
2. Enter 2 to exit the program''')
choice = int(input('Enter your choice here:-' ))
if choice==1:
	pass
if choice==2:
		exit()
name = input("Enter student name>>> ")

score = input('Enter student score>>> ')

int_score = int(score)

if int_score >= 80:
	print(name + ' is awarded an A+')
	
elif int_score >= 75 and int_score <=79:
	print(name + ' is awarded an A')
	
elif int_score >= 70 and int_score <=74:
	print(name + ' is awarded a B+')
	
elif int_score >= 65 and int_score <= 69:
	print(name + ' is awarded a B')
	
elif int_score >= 60 and int_score <= 64:
	print(name + ' is awarded a C+')
	
elif int_score >= 55 and int_score <=59:
	print(name + ' is awarded a C')
	
elif int_score >= 50 and int_score <=54:
	print(name + ' is awarded a D+')
	
elif int_score >= 40 and int_score <=49:
	print(name + ' is awarded a D')
	
elif int_score < 40:
	print(name + ' is awarded an F')
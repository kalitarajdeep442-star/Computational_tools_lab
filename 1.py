#Factorial
n = int(input("Enter a number: "))

factorial = 1
for i in range(1,n+1):
	factorial *= i
print("Factorial =" , factorial)

#To check prime
num = int(input("Enter another number to check prime: "))

if num<2:
	print(num, "is not a prime number")
else:
	prime = True
	for i in range(2,int(num ** 0.5)+1):
		if num%i == 0:
			prime = False
			break
	if prime:
		print(num,"is a prime number")
	else:
		print(num,"is not a prime number")

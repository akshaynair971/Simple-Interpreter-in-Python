import sys
def main():
	#input taken from user as list
	problem=[
		str(x) for x in input().split()
		]
	n=len(problem)
	#print(n)
	
	#Storing values from last index of list
	num1=(problem[n-2])
	num2=(problem[n-1])
	
	#finding keywords from list
	operation=["add","sub","mult","div"]
	if (add in problem for add in operation):
		add(num1,num2)
	elif(sub  in problem for add in operation):
		sub(num1,num2)
	elif(mult in problem for add in operation):
		mult(num1,num2)
	elif(div  in problem for add in operation):
		div(num1,num2)
		
		
		
def add(num1,num2):
	print(int(num1)+int(num2))
def sub(num1,num2):
	print(int(num1)-int(num2))
def mult(num1,num2):
	print(int(num1)*int(num2))
def div(num1,num2):
	print(int(num1)/int(num2))
main()

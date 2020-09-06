def fact(num):
	if num == 0:
		return print(1)
	else:	
		result = num
		for i in range(1,num):
			result = result * (num-i)
	
	return print(int(result))	

	
fact(5)

# If input is 5
# Output will be 120

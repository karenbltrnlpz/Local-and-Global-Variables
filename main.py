def get_name():

	name = input("What is your name?")
	return name

# print(name) variable is out of scope

def count_to_three():

	num = 1 
	while num <= 3:
		print(num)
		num += 1
	# if there is no return statement, the loop will return none

# print(count_to_three())


def greater_than_10(nums):
	"""
	this function takes an argument nums which is a list of integers and returns a list having any numbers from the argument list that are greater than 10
	"""
	
	nums_greater_than_10 = []
	for num in nums:
		if num > 10:
			nums_greater_than_10.append(num)

	return nums_greater_than_10

# print(greater_than_10([1, 2, 11, 23, 59, 67]))

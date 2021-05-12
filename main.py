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

def get_funny_sentence(name, place):
	""" function takes two string arguments one is the name of a person and the other is a place. With these the function returns a funny sentence as a string with the arguments being used somewhere in the funny sentence
	"""

	funny_sentence = f"Yesterday, {name} was able to get a unicorn hotdog at the {place} state fair."

	return funny_sentence

# print(get_funny_sentence("Mayha", "Trimont"))

def common_words_list(words1, words2):
	"""this function takes two lists containing strings as arguments and returns a list of the common words found in those lists"""

	common_words = []

	for word in words1:
		if word in words2:
			common_words.append(word)

	return common_words

# print(common_words_list(["apple", "bananas", "pajamas", "monkeys", "master splinter", "rats"], ["jeans", "bananas", "pajamas", "monkeys", "plums", "bats"]))

def find_divisible_nums(num1, num2, num3):
	"""function taking three integer arguments and returns a list of numbers from 1 to 100 (inclusive) containing only the numbers that are evenly divisible by at least one of the arguments"""

	
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

	num = 1
	multiples_list = []

	while num <= 100:
		if (num % num1 == 0) or (num % num2 == 0) or (num % num3 == 0):
			multiples_list.append(num)

		num += 1
		
	return multiples_list

# print(find_divisible_nums(31, 37, 39))

def ans():
	return "The answer is 42"

# print(ans())

name = 'Brighticorn'
fav_color = 'sparkle'

def sh_fav_clr(person, fav_color):
	print(f"{person} likes {fav_color}")
	return "Sucess"


# res = sh_fav_clr(name, fav_color)
# print(res)

#increasing a score function



def increase_score(score, points):
	""" Returns the new score total """

	score = score + points
	print(score)

	return score

# score = 0
# score = increase_score(score, 5)
# print(score)

"""LOCAL SCOPE: any variable that is inside the function body including the function parameters. Remember that these variables can only be referenced inside the function. 

OUTER SCOPE: any variable defined outside of functions are globally available. These variables can be used anywhere throughout the file."""
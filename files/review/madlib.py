# def weekend(s):
# 	if s == 'Saturday' or s == 'Sunday':
# 		return True
# 	return False

# print weekend('Monday')
# print weekend('Saturday')

# def countdown(n):
# 	i = 1
# 	for i in range(i, n+1):
# 		print n
# 		n = n - 1
# 	print 'Blast off'


# def countdown(x):
#     while x > 0:
#         print x
#         x = x-1
#     print "Blastoff!"


# print countdown(3)
#  madian the middle number 
# def bigger(a, b):
# 	if a > b:
# 		return a
# 	return b

# def biggest(a, b, c):
# 	return bigger(a, bigger(b, c))

# def madian(a, b, c):
# 	big = biggest(a, b, c)
# 	if big == a:
# 		return bigger(b, c)
# 	if big == b:
# 		return bigger(a, c)
# 	if big == c:
# 		return bigger(a, b)
# print madian(1,1, 3)

# def bigger(a,b):
# 	if a > b:
# 		return a
# 	return b

# def biggest(a, b, c):
# 	return bigger(a, bigger(b, c))

# def madian(a, b, c):
# 	big = biggest(a, b, c)
# 	if big == a:
# 		return bigger(b, c)
# 	if big == b:
# 		return bigger(a, c)
# 	if big == c:
# 		return bigger(a, b)

# print madian(1,1, 3)





from random import randint

def random_noun():
	random_number = randint(0, 1)
	if random_number == 0:
		return 'sofa'
	else:
		return 'llama'

# print random_noun()

def random_verb():
	random_number = randint(0, 1)
	if random_number == 0:
		return 'run'
	else:
		return  'kayak'

# print random_verb()

def word_transformer(word):
	if word == 'NOUN':
		return random_noun()
	elif word == 'VERB':
		return random_verb()
	else:
		return word[0]

# print word_transformer('VERB')

# def process_madlib(madlib):
# 	processed = ""
# 	index = 0
# 	box_length = 4
# 	while index < len(madlib):
# 		frame = madlib[index:index+box_length]
# 		to_add = word_transformer(frame)
# 		processed += to_add
# 		if len(to_add) == 1:
# 			index += 1
# 		else:
# 			index += 4
# 	return processed

def process_madlib(madlib):
	processed = ""
	index = 0
	box_length = 4
	while index < len(madlib):
		frame = madlib[index:index+box_length]
		add_to = word_transformer(frame)
		processed += add_to
		if len(add_to) == 1:
			index += 1
		else:
			index += 4
	return processed
    

test_string_1 = "This is a good NOUN to use when you VERB your food"
print process_madlib(test_string_1)
	


# def product_list(s):
# 	totol = 1
# 	for i in s:
# 		totol = totol * i
# 	return totol

# print product_list([1, 2, 3])


# def greatest(s):
# 	big = 0
# 	for i in s:
# 		if i > big:
# 			big = i
# 	return big
# print greatest([1, 22, 322])


#  madlib game 

# def word_in_pos(word, parts_of_speech):
# 	for pos in parts_of_speech:
# 		if pos in word:
# 			return pos
# 	return None
test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
# parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

# print word_in_pos(test_cases[0], parts_of_speech)
user_input = raw_input("enter ur name !")
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]
test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
	for pos in parts_of_speech:
		if pos in word:
			return pos
	return None


def play_game(ml_string, parts_of_speech):
	replaced = []
	ml_string = ml_string.split()
	for word in ml_string:
		replacement = word_in_pos(word, parts_of_speech)
		if replacement != None:
			word = word.replace(replacement, user_input)
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return replaced

    

print play_game(test_string, parts_of_speech)

# print word_in_pos(test_cases[3], parts_of_speech)
















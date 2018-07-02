# print 7*7*24*60
# minutes = minutes + 1
# seconds = minutes * 60
# print seconds
# Variables 

# age = 40
# days_in_year = 365.25
#the 200 is the days till my birth
# print age * days_in_year + 200
# Sting 

# s = "udacity"
# print (s+s)[-1]

# s = "audacity"
# print 'U' + s[2:]

# example = "Wow! Python is great! Don't you think?"
# first = example.find('!')
# second = example.find('!', first + 1)
# new_string = example[:first] + example[first+1:second] + example[second+1:]
# print new_string # oops, I should probably replace the !s with periods
# print new_string

# text = """Wow this is a fairly long body of text. Quite a few characters too.
# I wonder if the string.find method could help find where NOUN is located.
# That way, I could go out and VERB with my friends rather than counting characters
# all day long!"""
# noun_position = text.find("NOUN")
# print noun_position
# verb_position = text.find("VERB")
# print verb_position

# def double2(x):
# 	print  2 * x
# 	return 2 * x
# double2(2)

# def is_friend(z):
# 	if(z[:1] == 'd' or z[:1] == 'n'):
# 		return True
# 	return False
# print is_friend("e")

# def biggest(a,b,c):
#     if (a >= b )and (a>=c):
#        return a
#     elif (b>= a) and (b>= c):
#        return b
#     else: 
#        return c

# i = 0
# while i != 10:
#     i = i + 1
#     print i

# i = 1
# while i != 10:
#     i = i + 2
#     print i

# def positive_num(x):
# 	i = 1
# 	while(i <= x):
# 		print i 
# 		i = i + 1
# positive_num(3)

# def remove(somestring, sub):
#     """Return somestring with sub removed."""
#     location = somestring.find(sub)
#     if location == -1:
#     	return somestring
#     length = len(sub)
#     part_before = somestring[:location]
#     part_after = somestring[location + length:]
#     return part_before + part_after

# # 
# # Don't change these test cases!
# print remove('audacity', 'a')
# print remove('pythonic', 'ic')
# print remove('substring institution', 'string in')
# print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
# print remove('doomy', 'dooming')  # and this should print "doomy"


# blastoff
# def countdown(x):
# 	while x > 0:
# 		print x
# 		x = x -1
# 	print "blastoff!"

# print countdown(3)
# def bigger(a, b):
# 	if a > b:
# 		return a
# 	else: 
# 		return b
# # print bigger(12, 4)

# def biggest(a, b, c):
# 	return bigger(a, bigger(b, c))

# # print biggest(12, 3, 55)

# def median(a, b, c):
# 	big = biggest(a, b, c)
# 	if big == a:
# 		return bigger(b, c)
# 	if big == b :
# 		return bigger(a, c)
# 	else:
# 		return bigger(a, b)

# print median(1,3,4)



# from random import randint

# def random_noun():
#     num = randint(0, 1)
#     if num == 0:
#     	return "sofa"
#     else :
#     	return "llama"
  
# print random_noun()
# from random import randint

# def random_verb():
# 	rn_verb = randint(0, 1)
# 	if rn_verb == 0:
# 		return "run"
# 	else :
# 		return "kayak"

# print random_verb()


# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

# from random import randint

# def random_verb():
#     random_num = randint(0, 1)
#     if random_num == 0:
#         return "run"
#     else:
#         return "kayak"
        
# def random_noun():
#     random_num = randint(0,1)
#     if random_num == 0:
#         return "sofa"
#     else:
#         return "llama"

# def word_transformer(word):
#     if word == "NOUN":
#         return random_noun()
#     elif word == "VERB":
#         return random_verb()
#     else:
#         return word[0]
        
# def process_madlib(madlib):
#     processed = ""
#     # your code here
#     index = 0
#     box_leng = 4
#     while index < len(madlib):
#         frame = madlib[index: index + box_leng]
#         to_add = word_transformer(frame)
#         processed += to_add
#         if len(to_add) == 1:
#             index +=1
#         else :
#             index += 4
#     return processed
        
        
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    
# test_string_1 = "This is a good NOUN to use when you VERB your food"
# test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
# print process_madlib(test_string_1)
# print process_madlib(test_string_2)

# lists 
# days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# def how_many_days(month_number):
# 	return days_in_month[month_number-1]
	

# print how_many_days(1)

# p =[1,2]
# q = [3,4]
# p.append(q)
# print len(p)

# def all(p):
# 	i = 0
# 	while i<len(p):
# 		print p[i]
# 		i = i + 1
# print all([1, 2, 3])

# def all(p):
# 	for i in p:
# 		print i
# 		i = i +1

# print all([1, 2, 3])

# def sum_list(p):
# 	sum = 0
# 	for n in p:
# 		sum = sum + n
# 	return sum


# def measure_udacity(s):
# 	count = 0
# 	for i in s:
# 		if s[0] == 'U':
# 			count = count  + 1
# 	return count
				 

# print measure_udacity(['U', 'Udap'])

# def find_element(s, val):
# 	if val in s:
# 		return s.index(val)
# 	return -1


# print find_element([1,2], 2)
# **************************************************************


# def isLeapYear(year):
#     if (year % 4!=0):
#         return False
#     elif (year % 100 !=0):
#         return True
#     elif (year % 400 !=0):
#         return False
#     else:
#         return True
        
# def total_days_in_year(year):
#     if isLeapYear(year) == True:
#         return 366
#     else:
#         return 365
        
# def days_in_month (year, month):
#     month-=1
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if isLeapYear(year) == True and month ==1:
#         return 29
#     return days[month]

# def days_to_end_year(year,month,day):
#     days = 0
#     days += (days_in_month(year,month) - (day-1))
#     while(month < 12):
#         days += days_in_month(year, (month+1))
#         month+=1
#     return days

# def days_from_start_year(year,month,day):  
#     days = day-1
#     start_month = 1
#     while(start_month < month):
#         days += days_in_month(year, start_month)
#         start_month += 1
#     return days
    
    

# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
   
#     ##
#     # Your code here.
#     ##
#     start_date = day1
#     end_date = day2
    
#     start_month = month1
#     end_month = month2
    
#     start_year = year1
#     end_year = year2
#     total_days = 0
    
#     if(start_year == end_year):
#         sum_days = (days_from_start_year(start_year,start_month,start_date) + days_to_end_year(end_year,end_month,end_date))
#         total_days=  total_days_in_year(start_year) - sum_days
#     else:
#         day_to_year = days_to_end_year(start_year,start_month,start_date)
#         day_from_start = days_from_start_year(end_year,end_month,end_date)
#         total_days = day_to_year + day_from_start
        
#         elapse_year = (end_year - start_year)
#         i = 1
#         while(i < elapse_year):
#             total_days += total_days_in_year(start_year+i)
#             i+=1
    
#     return total_days

# # Test routine

# def test():
#     test_cases = [((2012,1,1,2012,2,28), 58), 
#                   ((2012,1,1,2012,3,1), 60),
#                   ((2011,6,30,2012,6,30), 366),
#                   ((2011,1,1,2012,8,8), 585 ),
#                   ((1900,1,1,1999,12,31), 36523)]
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print "Test with data:", args, "failed"
#         else:
#             print "Test case passed!"

# #test()

# print daysBetweenDates(2012, 6, 29, 2013, 6, 31)


# *********************************************************


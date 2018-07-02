# import random


# random_list = []
# list_length = 20

# while len(random_list) < list_length:
# 	random_list.append(random.randint(0, 10))

# index = 0
# count = 0

# while index < len(random_list):
# 	if random_list[index] == 9:
# 		count += 1
# 	index += 1

# print random_list
# print count



# count_list = [0] * 11

# while index < len(random_list):
# 	number = random_list[index]
# 	count_list[number] += 1
# 	index += 1

# print count_list
# print sum(count_list)




# **********************
# print '"""'
# print "number | occurance"
# print "0      "+"|"+"*"
# print "1      "+"|"+"**"
# print "2      "+"|"+"***"
# print "3      "+"|"+"****"
# print "4      "+"|"+"*****"
# print "5      "+"|"+"******"
import random 

random_list = []
list_length = 20

while len(random_list) < list_length:
	random_list.append(random.randint(0, 10))

index = 0
count = 0
count_list = [0] * 11

while index < len(random_list):
	number = random_list[index]
	count_list[number] += 1
	index += 1



# print "number | occurance"
# i = 0
# while i < 11:
# 	print " "*(6-len(str(i))) + str(i) +str(" | ")+str(count_list[i])
# 	i += 1

# print "Udacity! "*10

print "number | occurance"
i = 0
while i < 11:
	print " "*(6-len(str(i)))+str(i)+str(" | ")+(count_list[i])*"*"
	i +=1

	

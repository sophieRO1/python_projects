# days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# def how_many_days(month_number):
# 	return days_in_month[month_number-1]

# fruits = [['apple', 3], ['banana', 4], ['peach', 6]]
# print fruits[1][0]

# countries = [['China','Beijing',1350],
#              ['India','Delhi',1210],
#              ['Romania','Bucharest',21],
#              ['United States','Washington',307]]

# print countries[1][1]

# countries = [['China','Beijing',1350],
#              ['India','Delhi',1210],
#              ['Romania','Bucharest',21],
#              ['United States','Washington',307]]

# print countries[0][2] / countries[2][2]
# s = 'Hello'
# s[0] == 'Y'
# print s

# p = ['h', 'e', 'l', 'l', 'o']
# q = p
# p[0] = 'Y'
# print p
# print q
# spy = [0, 0, 7]
# agent = spy
# spy[2] = agent[2] + 1
# print spy

# def replace_spy(s):
# 	s[2] = s[2] + 1
# 	return s
	
	
# print replace_spy([1, 2, 3])

# ***************
# s1 = [1, 2, 3]
# s2 = [4,5, 6]
# s1 = s1 + s2
# print s1
# s1 = s1.append(s2)
# print s1

# print [0, 1] + [2, 3]
# print [0, 1].append([2, 3])
# print len([1, [2, 4], 4])

# p = [1, 2]
# p.append(3)
# p = p + [4, 5]
# print len(p)

# p = [1, 2]
# q = [3, 4]
# p.append(q)
# print len(p)

# p = [1, 2, 3]
# i = 0
# while i < len(p):
# 	print p[i]
# 	i = i + 1

# for i in range(1, len(p)+1):
# 	print i

# def sum_list(s):
# 	sum = 0
# 	for n in s:
# 		sum = sum + n
# 	return sum

# print sum_list([1, 2, 1])


def measure_udacity(s):
	count = 0
	for e in s:
		if e[0] == 'U':
			count = count + 1
	return count 

print measure_udacity(['Udacity', 'kay'])






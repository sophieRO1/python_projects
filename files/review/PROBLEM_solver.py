# leap year

def isLeapYear(year):
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	return False
		
# print isLeapYear(2018)

def daysInMonth(year, month):
	if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
		return 31
	else:
		if month == 2:
			if isLeapYear(year):
				return 29
			else:
				return 28
		return 30
		
		

print daysInMonth(2019, 8)
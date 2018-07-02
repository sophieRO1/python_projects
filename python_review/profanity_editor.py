import urllib
def read_file():
	quotes = open('C:\\Users\\sophie\\Desktop\\python_review\\profanity\\my_quotes.txt')
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q'+text_to_check)
	output = connection.read()
	print(output)
	if "false" in output:
		print("hurry up,  check the text .. it contains a bad word ")
	elif  "true" in output:
		print("chill out .. the text is clear ")
	else:
		print("nothing to see ")
	connection.close()
read_file()
import urllib.request

#open the file and read it 
def read_file():
	love_quotes = open("C:\\Users\Bonjour\\Desktop\\python_review\\movie_quotes.txt")
	contents_of_file = love_quotes.read()
	#print (contents_of_file)
	love_quotes.close()
	check_profanity(contents_of_file)
#check profanity
def check_profanity(text_to_check):
	connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q"+text_to_check)
	output = connection.read()
	print(output)
	connection.close()

read_file()

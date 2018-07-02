import urllib

def read_text():
	quotes = open('C:\Users\Bonjour\Desktop\python\movie_quotes.txt')
	file_content = quotes.read()
	print file_content
	quotes.close()
	check_profanity(file_content)


	# check profanity

def check_profanity(text_to_check):
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check)
    output = connection.read()
    print output
    connection.close()
    		










read_text()
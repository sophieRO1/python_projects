import urllib

def read_text():
	# open the file and read it

	quotes = open("C:\\Users\\sophie\\Desktop\\review\\quotes.txt")
	file_contents = quotes.read()
	print file_contents
	quotes.close()
	check_profanity(file_contents)

	# check for profanity word
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +text_to_check)
	output = connection.read()
	print output
	connection.close()
	if output == 'false':
		print 'yay .. there is no curse or bad word in the document,, u can send it '
	elif output == 'true':
		print 'oh no!!!.. there is a bad word .. hurry up check the document '
	else :
		print 'i dont know,i couldnt scan the document properly.'

read_text()
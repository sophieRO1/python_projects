import urllib 
def read_text():
    quotes = open('C:\Users\Bonjour\Desktop\python\movie_quotes.txt')

    file_content = quotes.read()
    print file_content
    quotes.close()

    check_profanity(file_content)

    # check for profanity words

def check_profanity(content_to_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+content_to_check)
    output = connection.read()
    print output
    connection.close()

    if "true" in output:
        print 'u shuld check the file'
    elif "false" in output:

        print 'no curse words '
    else:
        print 'couldnt scan the file properly'




read_text()
    

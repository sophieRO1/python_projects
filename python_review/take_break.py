import webbrowser
import time 


break_count = 0
total_breaks = 3

while break_count < total_breaks:
	
	print 'the program  is running at: '+time.ctime()
	time.sleep(10)  # time in seconds 
	#link of ur fav. music to chill out 
	webbrowser.open('https://www.youtube.com/watch?v=x77TwJNObog&list=PLpNRl2qutbCTXZNyBlFzRgL9QzM0Pkbaw&t=0s&index=3')
	break_count = break_count + 1


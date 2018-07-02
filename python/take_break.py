import time 
import webbrowser



break_count = 0
total_breaks = 3

while break_count < total_breaks:
	print 'the current time is '+time.ctime()
	time.sleep(2)
	webbrowser.open('https://www.youtube.com/watch?v=x77TwJNObog&index=2&t=0s&list=PLpNRl2qutbCTXZNyBlFzRgL9QzM0Pkbaw')
	break_count = break_count + 1
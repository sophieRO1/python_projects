import webbrowser
import time


total_breaks = 3
break_count = 0

print 'this program is starting at '+ time.ctime()
while break_count < total_breaks:
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=3wPKa21zKrQ&t=481s&list=PLpNRl2qutbCTXZNyBlFzRgL9QzM0Pkbaw&index=7")
	break_count = break_count + 1
   


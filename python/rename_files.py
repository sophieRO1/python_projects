import os 
import time

def rename_files():
	# get the files from the folder 
	file_list = os.listdir(r'C:\Users\Bonjour\Desktop\my_prank')
	saved_path = os.getcwd()
	print saved_path
	os.chdir(r'C:\Users\Bonjour\Desktop\my_prank')

	# rename fles 
	for file_name in file_list:
		print 'program starts at '+time.ctime()
		os.rename(file_name, file_name.translate(None, '0123456789'))
		os.chdir(r'C:\Users\Bonjour\Desktop\my_prank')
		





rename_files()








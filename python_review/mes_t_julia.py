import os


def rename_files():
	# get the file name from file folder
	file_list = os.listdir(r'C:\Users\Bonjour\Desktop\python_review\Nother_Secret_meSSAGE')  
	#print (file_list)
	saved_path = os.getcwd()
	print (saved_path)
	os.chdir(r'C:\Users\Bonjour\Desktop\python_review\Nother_Secret_meSSAGE')

	# rename files 
	for file_name in file_list:
		print ('old file : ' + file_name)
		print ('new file : ' + file_name.translate(None, "1234567890"))
		os.rename(file_name, file_name.translate(None, "1234567890"))
	os.chdir(saved_path)

rename_files()
import os

def rename_files():
	#get the file name from the folder
	file_list = os.listdir(r"C:\Users\sophie\Desktop\review\sm_word")
	# print file_list
	saved_path = os.getcwd()
	# print saved_path
	os.chdir(r"C:\Users\sophie\Desktop\review\sm_word")

	# for each filename , rename it 
	for file_name in file_list:
		print 'old  name is :'+ file_name
		print 'new name is :'+ file_name.translate(None, "1234567890")
		os.rename(file_name, file_name.translate(None, "1234567890"))
	os.chdir(saved_path)

rename_files()

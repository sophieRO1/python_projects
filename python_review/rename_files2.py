import os

def rename_files():
	#  get file list
	file_list = os.listdir(r'C:\Users\sophie\Desktop\python_review\S_MESSAGE_FILEs')
	# print(file_list)
	saved_path = os.getcwd()
	# print(saved_path)
	os.chdir(r'C:\Users\sophie\Desktop\python_review\S_MESSAGE_FILEs')

#     #  rename files
    for file_name in file_list:

    	print('old files' + file_name)
    	print('new files' +  file_name.translate(None, "1234567890"))
    # 	os.rename(file_name, file_name.translate(None, "1234567890"))
    # os.chdir(saved_path)

rename_files()


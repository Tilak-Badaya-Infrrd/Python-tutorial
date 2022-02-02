import os

os.chdir('/home/tilakbadaya/Desktop/Python Tutorials')

for f in os.listdir():
    file_name , file_ext = os.path.splitext(f)
    
    file_name = file_name.strip()
    
    #os.rename(f,file_name)
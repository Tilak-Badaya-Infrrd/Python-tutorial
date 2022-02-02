import os
from datetime import datetime

print(dir(os))
print("")
print(os.getcwd())
os.chdir('/home/tilakbadaya/Desktop')
print(os.getcwd())
print(os.listdir())
os.mkdir('Demo3')
os.rmdir('Demo3')


print("")
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print()
for dirpath, dirnames, filenames in os.walk('/home/tilakbadaya/Desktop'):
    print('Current Path:' ,dirpath)
    print('Directories' ,dirnames)
    print('Files:' , filenames)
    print()
      
    

print(os.environ.get('home'))
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/dewc'))
print(os.path.isfile('/tmp/dewc'))
print(os.path.splitext('/tmp/test.txt'))




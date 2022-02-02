

try:
    f = open('test.txt')
    # var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist.')
except Exception:
    print('Sorry. Something went wrong.')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally")
    
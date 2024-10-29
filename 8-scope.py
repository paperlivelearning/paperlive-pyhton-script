x = 300

def myfunc():
  x = 200
  print("Local to function : ", x)

myfunc()

print("Global value : ", x)
x = 300

def myfunc():
  global x
  x = 200
  print("Local value : ", x)

myfunc()

print("Global valus : ", x)
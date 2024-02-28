print("Welcome, This is a calculator")

x = int(input("First number: "))
y = int(input("Second number: "))
z = input("Arithmetic operation in words: ")

if z == "add":
  print("solution is ", x+y)
elif z == "subtract":
  print("solution is ", x-y)
elif z == "multiply":
  print("solution is ", x*y)
elif z == "divide":
  print("solution is ", x/y)
else:
  print("error, try again")

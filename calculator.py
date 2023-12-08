a = float(input ("Enter the first number: "))
operator= input ("Enter the opertar: ")
b = float(input ("Enter the second number: "))

if operator == "+":
  print(a, "+", b, "=",a+b)
elif operator == "-":
  print(a, "-", b, "=", a-b)
elif operator == "*":
  print(a, "*", "=", a*b)
elif operator == "/":
  print(a, "/", "=", a/b)
else:
  print("\nPlease enter a valid operator! :)")

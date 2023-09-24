def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2
while True:
    print("selected operation")
    print("1.add")
    print("2.sub")
    print("3.multiply")
    print("4.divide")
if choice == "1":
    print("result:", add(num1,num2))
  elif choice == "2":
    print("result:", subtract( num1 , num2))
  elif choice== "3":
    print("result:", multiply(num1, num2))
  elif choice=="4":
    print("result:", add(num1, num2))
  else:
    print("inalid input")



#Program using match case that stimulates a simple calculator
a = int(input("Enter a number: "))
b = int(input("Enter another number "))
c = input("enter the arithemetic operator symbol that you want to use (add,sub,prod,divide,modulo) ")
match c:
      case "add":
        print("The sum is ", a + b)
      case "sub":
       print("The difference of both number is: ", a - b)
      case "prod":
       print("product of the numbers is: ", a * b)

      case "divide":
       print("division of the numbers is quotient: ", a / b)

      case "modulo":
       print("division of the numbers gives the remainder: ", a % b)

      case _:
       print("invalid input")
#calculator.py

operators =['+', "-", "/", "*"]

while True:

    operation = input("What is the operation you'd like to perform?  Please type +, -, /, or *: ")

    if operation == 'done':
        print('Goodbye')
        break
    if not operation in operators: 
        print("That's not an operator you can use")

    else:

        num1 = float(input("What is the first number?: "))
        num2 = float(input("What is the second number?: "))

        if operation == "+":

            print (num1 + num2)

        elif operation == "-":

            print (num1 - num2)

        elif operation == "/":

            print (num1 / num2)

        elif operation == "*":

            print (num1 * num2) 

  


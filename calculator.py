def add(num1 , num2):
    return num1 + num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    return num1 / num2

print("Slect operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    opt_input = input("Choose an opreation (1/2/3/4):")
    if opt_input in ('1', '2' , '3' , '4'):
        first_num = float(input("Enter first number: " ))
        second_num = float(input("Enter second number: " ))
        if opt_input == '1':
            result = add(first_num , second_num)
            print(f"The result is :  {result}")
        elif opt_input == '2':
            result = subtract(first_num , second_num)
            print(f"The result is :  {result}")
        elif opt_input == '3':
            result = multiply(first_num , second_num)
            print(f"The result is :  {result}")
        elif opt_input == '4':
            result = divide(first_num , second_num)
            print(f"The result is :  {result}")
        
        next_operation = input("Let's do next calculation? (y/n):").lower()
        if next_operation == 'n':
            print("Thank you for using the calculator.")
            break
    else:
        print("Invalid Input")
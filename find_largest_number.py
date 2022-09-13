number1 = int(input('Enter First Number : '))
number2 = int(input('Enter Second Number : '))
number3 = int(input('Enter Third Number : '))
number4 = int(input('Enter Fourth Number : '))
def largest(num1, num2, num3, num4):
    if (num1 > num2) and (num1 > num3) and (num1 > num4):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3) and (num2 > num4):
        largest_num = num2
    elif (num3 > num1) and (num3 > num2) and (num3 > num4):
        largest_num = num3
    else:
        largest_num = num4
    print("The largest of the 4 numbers is : ", largest_num)
largest(number1, number2, number3, number4)

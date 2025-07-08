# num = input("Non-negative integer: ")

# if num.isnumeric():
#     if int(num) >= 0:
#         print("True")
#     else:
#         print('False')
# else:
#     print("It's numeric but not a positive integer")
#     print("False")


try:
    num = input("Input integer: ")
    
    if int(num) >= 0:
        print("Valid integer :", int(num))
    else:
        print('False')

except TypeError as e:
    print("We need non-negative integer", e)

except ValueError as e:
    print("Value error")
    print(e)

except EOFError as e:
    print("Terminated")
    print(e)
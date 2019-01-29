def fibonacci(num):
    a = 0
    b = 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b
    print()
    return num

numb = int(input("Enter an n to proceed: "))
#total_sum = sum(fibonacci(num))
#print("The total sum is: {}".format(total_sum))
fibonacci(numb)



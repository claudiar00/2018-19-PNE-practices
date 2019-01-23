def sum(n):
    total = 0
    for i in range(n):
        total = total + i + 1
    return total

#--- Main program

num = int(input("Enter n: "))
total_sum = sum(num)
print("The total sum is: {}".format(total_sum))



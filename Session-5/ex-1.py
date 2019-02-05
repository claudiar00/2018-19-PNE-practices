def count_a(seq):
    counter = 0
    for elem in seq:
        if elem.upper() == 'A':
            counter += 1
    return counter


# main program
s = input('Please enter a valid sequence: ')
number_a = count_a(s)
print('The number of As in the sequence is: ', number_a)

l = len(s)

if l > 0:
    perc = round(100.0 * number_a / l, 1)
else:
    perc = 0

#The percentage of As in the sequence


print('The length of the sequence is: ',l)
print('The percentage of As in the sequence is: ', perc, '%')



def count_a(seq):
    counter = 0
    for elem in seq:
        if elem == 'A':
            counter += 1
    return counter


# main program
s = 'AGTCTAGCAGTAGTAGATAGATAGTACGATCGATCAGTCAGA'
number_a = count_a(s)
print('The number of As in the sequence is: ', number_a)

l = len(s)

print('The length of the sequence is: ',l)

#The percentage of As in the sequence

perc = round(100.0*number_a/l, 1)

print('The percentage of As in the sequence is: ', perc, '%')



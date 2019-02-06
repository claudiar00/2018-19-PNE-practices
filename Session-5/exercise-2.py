def count_bases(seq):
    counter_a = 0
    counter_t = 0
    counter_g = 0
    counter_c = 0
    for letter in seq:
        if letter.upper() == 'A':
            counter_a += 1
        elif letter.upper() == 'T':
            counter_t += 1
        elif letter.upper() == 'G':
            counter_g += 1
        elif letter.upper() == 'C':
            counter_c += 1

    dict = {'A': counter_a, 'T': counter_t, 'G': counter_g, 'C': counter_c}
    return  dict

#main program

seq1 = input('Enter the sequence 1: ')
seq2 = input('Enter the sequence 2: ')

#Sequence 1 analysis

l = len(seq1)
print('The sequence 1 is', l, 'bases in length')
for k in count_bases(seq1).keys():
    if l > 0:
        perc = round(100.0*count_bases(seq1)[k]/l, 1)
        print('Base ',k, '\n', 'Counter: {}'.format(count_bases(seq1)[k]))
        print(' Percentage: {}'.format(perc), '%')

#sequence 2 analysis

l2 = len(seq2)
print('\n')
print('The sequence 2 is', l2, 'bases in length')
for k in count_bases(seq2).keys():
    if l > 0:
        perc = round(100.0*count_bases(seq2)[k]/l2, 1)
        print('Base ',k, '\n', 'Counter: {}'.format(count_bases(seq2)[k]))
        print(' Percentage: {}'.format(perc), '%')








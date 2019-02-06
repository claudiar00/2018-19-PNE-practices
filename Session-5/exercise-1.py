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
seq = input('Enter a valid sequence to analyze: ')
l = len(seq)

for k in count_bases(seq).keys():
    if l > 0:
        perc = round(100.0*count_bases(seq)[k]/l, 1)
        print('This sequence is', len(seq), 'bases in length', '\n')
        print('Base ',k, '\n', 'Counter: {}'.format(count_bases(seq)[k]))
        print(' Percentage: {}'.format(perc), '%')








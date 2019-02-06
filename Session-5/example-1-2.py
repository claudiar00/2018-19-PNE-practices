#We import here the count_bases function from the bases file
from Bases import count_bases


"""Main program of exercise 1"""

seq = input('Enter a valid sequence to analyze: ')
l = len(seq)

for k in count_bases(seq).keys():
    if l > 0:
        perc = round(100.0*count_bases(seq)[k]/l, 1)
        print('This sequence is', l, 'bases in length', '\n')
        print('Base ',k, '\n', 'Counter: {}'.format(count_bases(seq)[k]))
        print(' Percentage: {}'.format(perc), '%')

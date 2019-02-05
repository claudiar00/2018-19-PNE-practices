def count_bases(seq, letter):
    counter = 0
    for elem in seq:
        if elem.upper() == letter:
            counter += 1

    return  {letter:counter}

#main program
s = input('Enter a valid sequence to analyze: ')
print ('This sequence is ', len(s), 'bases in legth')
print('Base A')
number_a = count_bases(s, 'A')
print('The number of As in the sequence is: ', number_a)
print('Base T')
number_t = count_bases(s, 'T')
print('The number of Ts in the sequence is: ', number_t)
print('Base C')
number_c = count_bases(s, 'C')
print('The number of Cs in the sequence is: ', number_c)
print('Base G')
number_g = count_bases(s, 'G')
print('The number of Gs in the sequence is: ', number_g)




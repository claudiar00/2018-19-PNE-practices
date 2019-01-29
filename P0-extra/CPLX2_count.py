with open ('CPLX2.txt', 'r') as f:
    sequence = f.read().partition('\n')
    sequence_ = sequence[2].replace('\n','')
    num_a = sequence_.count('A')
    num_c = sequence_.count('C')
    num_g = sequence_.count('G')
    num_t = sequence_.count('T')


    print("Number of A's in the CPLX2 sequence: ", num_a)
    print("Number of C's in the CPLX2 sequence: ", num_c)
    print("Number of G's in the CPLX2 sequence: ", num_g)
    print("Number of T's in the CPLX2 sequence: ", num_t)
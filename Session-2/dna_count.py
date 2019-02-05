sequence = (input("Insert a dna sequence: "))
print(sequence)

num_a = sequence.count('A')
num_c = sequence.count('C')
num_g = sequence.count('G')
num_t = sequence.count('T')

print("Number of A's in the sequence: ", num_a)
print("Number of C's in the sequence: ", num_c)
print("Number of G's in the sequence: ", num_g)
print("Number of T's in the sequence: ", num_t)

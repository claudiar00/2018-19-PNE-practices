from Seq import Seq

seq1 = Seq('AGTC')
seq2 = Seq('GGT')
seq3 = seq1.complement()
seq4 = seq3.reverse()


"""Main program"""

"""for sequence 1"""
print("Sequence 1: ", seq1.strbase)
print("  Length: ", seq1.len())
print("  Bases count: ", 'A:', seq1.count('A'), 'G:', seq1.count('G'), 'T:', seq1.count('T'), 'C:', seq1.count('C'))
print("  Bases percentages: ", 'A:', seq1.perc('A'), 'G:', seq1.perc('G'), 'T:', seq1.perc('T'), 'C:', seq1.perc('C'))

"""for sequence 2"""
print("Sequence 2: ", seq2.strbase)
print("  Length: ", seq2.len())
print("  Bases count: ", 'A:', seq2.count('A'), 'G:', seq2.count('G'), 'T:', seq2.count('T'), 'C:', seq2.count('C'))
print("  Bases percentages: ", 'A:', seq2.perc('A'), 'G:', seq2.perc('G'), 'T:', seq2.perc('T'), 'C:', seq2.perc('C'))

"""for sequence 3"""
print("Sequence 3: ", seq3.strbase)
print("  Length: ", seq3.len())
print("  Bases count: ", 'A:', seq3.count('A'), 'G:', seq3.count('G'), 'T:', seq3.count('T'), 'C:', seq3.count('C'))
print("  Bases percentages: ", 'A:', seq3.perc('A'), 'G:', seq3.perc('G'), 'T:', seq3.perc('T'), 'C:', seq3.perc('C'))

"""for sequence 4"""
print("Sequence 4: ", seq4.strbase)
print("  Length: ", seq4.len())
print("  Bases count: ", 'A:', seq4.count('A'), 'G:', seq4.count('G'), 'T:', seq4.count('T'), 'C:', seq4.count('C'))
print("  Bases percentages: ", 'A:', seq4.perc('A'), 'G:', seq4.perc('G'), 'T:', seq4.perc('T'), 'C:', seq4.perc('C'))
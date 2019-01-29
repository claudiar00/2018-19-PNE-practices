#The exercise 5 consists on reading several DNA sequences from an external file and counting the number of bases that
#appears in them.

with file(dna_sequence) as f:
    write = f.write('ACTG', '\n', 'ACGT')
#Here we create a program that reads the wanted filename but we have ti create previously a filenme with some DNA
#sequences in order to let the program read it and do what its asked.
with file(dna_sequence) as f:
    read = f.read()



#The exercise 5 consists on reading several DNA sequences from an external file and counting the number of bases that
#appears in them.

with open ('dna.txt', 'w') as f:
    f.write('AGTCAG')
    f.write('ACGTAG')
f.close()

#Here we create a program that reads the wanted filename but we have ti create previously a filenme with some DNA
#sequences in order to let the program read it and do what its asked.
with open ('dna.txt', 'r') as f:
    lenght = len(f.read())
    print("The lenght of the sequence is: ", lenght)
    for elem in f.read():
        print ("hol")




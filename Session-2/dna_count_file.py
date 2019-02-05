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


def read_file_dna(file):
    counter_a = 0
    counter_c = 0
    counter_g = 0
    counter_t = 0
    counter_total = 0
    with open(file) as f:
        for line in f:
            line =line.replace("\n", "")
            line =line.replace(" ", "")
            counter_a += line.count("A")
            counter_c += line.count("C")
            counter_g += line.count("G")
            counter_t += line.count("T")
            counter_total += len(line)
        print(" A : ", counter_a, "\n", "C : ", counter_c, "\n", "G : ", counter_g, "\n", "T : ", counter_t, "\n", "TOTAL LENGTH : " , counter_total)


read_file_dna("dna.txt")

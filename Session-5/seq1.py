class Seq:
    def __init__(self,strbases):
        print('New sequence is created')

        self.strbases = strbases
    def len(self):
        return len(self.strbases)

seq_1 = Seq('ATTCGATCC')
seq_2 = Seq('AAAGG')

str1 = seq_1.strbases
str2 = seq_2.strbases

l1 = seq_1.len()
l2 = seq_2.len()


print('Sequence 1: {}'.format(str1))
print('     Length is: {}'.format(l1))
print('Sequence 2: {}'.format(str2))
print('     Length is: {}'.format(l2))
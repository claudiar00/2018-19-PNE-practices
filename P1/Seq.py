class Seq():
    def __init__ (self, strbase):
        self.strbase = strbase

    def len(self):
        l = len(self.strbase)
        return l

    def complement(self):
        new = ''
        for letter in self.strbase:
            if letter == 'A':
                new += 'T'
            elif letter == 'T':
                new += 'A'
            elif letter == 'C':
                new += 'G'
            elif letter == 'G':
                new += 'C'
        new_seq = Seq(new)
        return new_seq

    def reverse(self):
        reverse1 = self.strbase[::-1]
        reverse = Seq(reverse1)
        return reverse

    def count(self, base):
        return(self.strbase.count(base))


    def perc(self, base):
        total_len = len(self.strbase)
        count = self.strbase.count(base)
        perc = round(100.0*(count/total_len),1)
        return perc










'''
Write a script (or better yet, a library) which reads in and validates a sequence of A, T, G, and C as representing a DNA sequence. 
Add the ability to reverse, complement, and reverse-complement the sequence 
(you will need to find out what it means to 'complement' a DNA sequence).

Adenine(A) pairs with Thynine(T

Cytosine(C) pairs with Guanine
'''
class DNAreader:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    #Assuming "Sequence" is a list
    def complement(self,sequence):
        complemented = ""
        for i in self.sequence:
            if(i == 'A'):
                complemented += 'T'
            elif(i == 'T'):
                complemented += 'A'
            elif(i == 'C'):
                complemented += 'G'
            elif(i == 'G'):
                complemented += 'C'
                
        return complemented
            
    def reverse(self,sequence):
        #print("in")
        reverse = ""
        for i in range(len(self.sequence)-1, -1, -1):
            reverse += self.sequence[i]
        
        return reverse
    
    def reversecomplement(self,sequence):
        reversed = self.reverse(sequence)
        #self.sequence is immutable, therefore the string sequence needs to be set to the reversed sequence
        self.sequence = reversed
        complemented = self.complement(reversed)
        return complemented

        
if __name__=="__main__":
    dna = DNAreader("ATCGGTA")
    print("Sequence:", dna.sequence)
    reversed = dna.reverse(dna.sequence)
    complement = dna.complement(dna.sequence)
    reverse_complement = dna.reversecomplement(dna.sequence)
    print("Reversed Sequence:", reversed)
    print("Complementary Sequence:", complement)
    print("Reverse Complementary Sequence:", reverse_complement)
    
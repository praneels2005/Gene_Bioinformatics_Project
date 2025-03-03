'''
To put functions inside your library, you can place them in the myfunctions.py file
'''

'''
Bioinformatics_Library
    Complememt
    Reverse-Complement
    Reverse
    Transcription(DNA to RNA)
    Translation(RNA to protein)
    Reverse Transcription(RNA to DNA)
    Back-Translation(Protein to DNA or RNA
    Sequence Translation to Binary/Encoded Forms
    K-mer Extraction
    GC-Content Calculation
    Palindrome Checking
    Codon Optimization
    Sequence Alignment and Manipulation
    
'''

#https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/translation/a/the-genetic-code-discovery-and-properties
codon_table = [
    ['AUG', 'Methionine'], ['UUU', 'Phenylalanine'],['UUC', 'Phenylalanine'], ['UUA', 'Leucine'], ['UUG', 'Leucine'],
    ['CUU', 'Leucine'], ['CUC', 'Leucine'], ['CUA', 'Leucine'], ['CUG', 'Leucine'], ['AUU', 'Isoleucine'],
    ['AUC', 'Isoleucine'], ['AUA', 'Isoleucine'], ['GUU', 'Valine'], ['GUC', 'Valine'],
    ['GUA', 'Valine'], ['GUG', 'Valine'], ['UCU', 'Serine'], ['UCC', 'Serine'], ['UCA', 'Serine'], ['UCG', 'Serine'],
    ['CCU', 'Proline'], ['CAU', 'Histidine'], ['CAC', 'Histidine'], ['CCC', 'Proline'], ['CCA', 'Proline'], ['CCG', 'Proline'],
    ['CAA', 'Glutamine'], ['CAG', 'Glutamine'], ['AAU', 'Asparagine'], ['AAC', 'Asparagine'], ['AAA', 'Lysine'], ['AAG', 'Lysine'],
    ['GAU', 'Aspartic acid'], ['GAC', 'Aspartic acid'], ['GAA', 'Glutamic acid'], ['GAG', 'Glutamic acid'],
    ['ACU', 'Threonine'],['ACC', 'Threonine'], ['ACA', 'Threonine'], ['ACG', 'Threonine'], ['GCU', 'Alanine'], ['GCC', 'Alanine'],
    ['GCA', 'Alanine'], ['GCG', 'Alanine'], ['UAU', 'Tyrosine'], ['UAC', 'Tyrosine'], ['UGU', 'Cysteine'],
    ['UGC', 'Cysteine'], ['UGG', 'Tryptophan'], ['CGU', 'Arginine'], ['CGC', 'Arginine'], ['CGA', 'Arginine'],
    ['CGG', 'Arginine'], ['AGU', 'Serine'], ['AGC', 'Serine'], ['AGA', 'Arginine'], ['AGG', 'Arginine'],
    ['GGU', 'Glycine'], ['GGC', 'Glycine'], ['GGA', 'Glycine'], ['GGG', 'Glycine'], ['UAA', 'Stop'],
    ['UAG', 'Stop'], ['UGA','Stop']
]

#print(codon_table.index('AUG'))
#Immutable objects are int, str, tuple - Creating a new object and not affecting the original one
#Mutable objects are list, dict, set - The cahnges will be reflected in the original object outside the function
def complement(sequence):
        complemented = ""
        for i in sequence:
            if(i == 'A'):
                complemented += 'T'
            elif(i == 'T'):
                complemented += 'A'
            elif(i == 'C'):
                complemented += 'G'
            elif(i == 'G'):
                complemented += 'C'
            elif(i == 'U'):
                complemented += 'A'
                
        return complemented
    
def reverse(sequence):
        reverse = ""
        for i in range(len(sequence)-1, -1, -1):
            reverse += sequence[i]
        
        return reverse
    
def reversecomplement(sequence):
        reversed = reverse(sequence)
        #self.sequence is immutable, therefore the string sequence needs to be set to the reversed sequence
        #self.sequence = reversed
        Reverse_Complemented = complement(reversed)
        return Reverse_Complemented

'''
This process involves converting a DNA sequence into its corresponding RNA sequence. In DNA, the base pairs are A-T and C-G, while in RNA, the base pairs are A-U (instead of A-T) and C-G.
DNA Sequence: 5' - ATGCATGC - 3'
RNA Transcript: 5' - AUGCAUGC - 3' (replacing T with U)
'''
def Transcription(sequence):
    complemented = ""
    for i in sequence:
        if(i == 'T'):
            complemented += 'U'
        else:
            complemented += i
                
    return complemented

'''
The process of translating an RNA sequence into a protein sequence (amino acids). This involves using the genetic code, where each triplet of RNA bases (codon) corresponds to a specific amino acid.
RNA Sequence: 5' - AUG GCU UGA - 3'
Protein: Met-Ala-Stop (using codon translation)

Codon: Sequences of 3 nucleotides(bases) that correspond to specific amino acids or stop signals during protein synthesis
Assumes user enters a valid mRNA sequence
Protein-coding RNA sequences(mRNA): its length must be a multiple of 3
'''
def Translation(sequence):
    Sequence = sequence.replace(" ","")
    if(len(Sequence)%3!=0):
        return "Not a valid mRNA sequence"
    
    RNA_SEQ =[]
    for i in range(0,len(Sequence),3):
        RNA_SEQ.append(Sequence[i:i+3])
    #print(RNA_SEQ)
    PROTEIN_SEQ = []
    for i in RNA_SEQ:
        for k in range(len(codon_table)):
            if  i == codon_table[k][0]:
                if(codon_table[k][1] == 'Stop'):
                    return PROTEIN_SEQ
                PROTEIN_SEQ.append(codon_table[k][1])
                break
    
    return PROTEIN_SEQ

def reverse_transcription(sequence):
    Sequence = sequence.replace(" ","")
    Transcription_complement = complement(Sequence)
    Reverse_transcription_complement = reversecomplement(Transcription_complement)
    
    return Reverse_transcription_complement

def Back_Translation(Seq):
    #Seq = Protein_Seq.split("-")
    #print(Seq)
    RNA_SEQ = []
    for i in Seq:
        Elements = []
        for k in range(len(codon_table)):
            if  i == codon_table[k][1]:
                Elements.append(codon_table[k][0])
        RNA_SEQ.append(Elements)
    
    DNA_SEQ = []
    for x in RNA_SEQ:
        temp = []
        for i in x:
            temp.append(complement(i))
        DNA_SEQ.append(temp)
    
    print("RNA Sequence:",RNA_SEQ)
    print("DNA Sequence:",DNA_SEQ)
    

def K_MER(Sequence, k):
    KMERS = []
    for i in range(0,len(Sequence)):
        if(i+k >len(Sequence)):
            break
        KMERS.append(Sequence[i:i+k])
    
    return KMERS

def GC_Content(Sequence):
    #Includes element from sequence if it is either 'G' or 'C'
    Count = [x for x in Sequence if (x == 'G' or x == 'C')]
    return (((float)(len(Count))/len(Sequence))*100)

def Palindrome(Sequence) -> bool:
    return Sequence == reversecomplement(Sequence)
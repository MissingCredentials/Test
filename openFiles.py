!wget --no-check https://d28rh4a8wq0iu5.cloudfront.net/adsl/data/lambda_virus.fa
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:    #opened as read only
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
genome = readGenome('lambda_virus.fa')

counts = {'A':0, 'C':0, 'G':0, 'T':0, 'N':0}
for base in genome:
    counts[base] +=1
print (counts)

import collections
collections.counter(genome)

!wget --no-check https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/SRR835775_1.first1000.fastq
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
seqs, quals = readFastq('SRR835775_1.first1000.fastq')

def phred33ToQ(qual):
    return ord(qual)-33

def createHist(qualities):
    hist = [0]*50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] +=1
    return hist

    %matplotlib inline
    import matplotlib.pyplot as plt
    plt.bar(range(len(h)), h)
    plt.show()

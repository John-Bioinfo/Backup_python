

from Bio.SeqIO.QualityIO import FastqGeneralIterator
import sys

seqlen = 150

for i, seq, qual in FastqGeneralIterator( open( sys.argv[1] ) ):
    record_len = len(seq)
    ## print('@{0} {1}\n{2}\n+\n{3}'.format(i, record_len,  seq, qual ))
    if record_len == seqlen:

        print('@{0}\n{1}\n+\n{2}'.format( i,   seq ,   qual ))

# sp.Load("/data/sentence/opennmt_pretrained/sentencepiece.model")
# python decode_sentencepiece.py /data/sentence/opennmt_pretrained/sentencepiece.model data/opennmtptru_src-val-g.txt data/opennmtptru_src-val-g_decoded.txt

import sys
import codecs
import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.Load(sys.argv[1])

outfile = codecs.open(sys.argv[3], "w", "utf-8")
with codecs.open(sys.argv[2], "r", "utf-8") as input_file:
    for i, line in enumerate(input_file):
        outfile.write(' '.join(sp.DecodePieces(line.split())))